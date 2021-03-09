import cv2
import numpy as np
import pandas as pd
from pathlib import Path
from torch.utils.data import Dataset

CLASS_LABEL_MAP = {
    "stop": 1,        # red
    "warning": 2,     # yellow
    "go": 3,          # green
    "goForward": 4,   # unknown
    "goLeft": 4,      # unknown
    "warningLeft": 4,  # unknown
    "stopLeft": 4,    # unknown
}

LABEL_CLASS_MAP = {
    1: "red",
    2: "yellow",
    3: "green",
    4: "unknown",
}


def createDataFrame(files):
    df_all = []

    for f in files:
        df = pd.read_csv(str(f), ";")

        # change 'Filename' value to absolute path
        def abs_path(filename, f_path):
            f_path_split = f_path.parts
            Annotations_idx = f_path_split.index('Annotations')
            root_dir = Path(*f_path_split[:Annotations_idx])
            type_dir = f_path_split[Annotations_idx + 2]  # dayTrain, daySequence1, ...
            clip_dir = f_path_split[Annotations_idx + 3:-1]  # dayClip1
            img_name = filename.split("/")[-1]

            return str(root_dir.joinpath(*[type_dir]*2,
                                         *clip_dir,
                                         "frames",
                                         img_name))

        df["Filename"] = df["Filename"].apply(abs_path, args=(f,))
        df_all.append(df)

    df_all_concat = pd.concat(df_all, ignore_index=True)
    df_all_concat.drop_duplicates(inplace=True, ignore_index=True)

    return df_all_concat


class LISADataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform

        # load all annotation files
        root_dir = Path(root_dir)
        search_dir = root_dir.joinpath("Annotations", "Annotations")
        annotationFiles = search_dir.glob("day*/**/*BOX.csv")
        self.annotations = createDataFrame(annotationFiles)

        # images
        self.imgs = self.annotations["Filename"].unique()

        # groupby_frame
        self.annotations_groupby_frame = self.annotations.groupby("Filename")

    def getAnnotation(self, img_path):
        annotation = self.annotations_groupby_frame.get_group(img_path)
        return annotation[
            [
                "Filename",
                "Annotation tag",
                "Upper left corner X",
                "Upper left corner Y",
                "Lower right corner X",
                "Lower right corner Y",
            ]
        ]

    def __getitem__(self, idx):
        # load image at that index
        img_path = self.imgs[idx]
        image = cv2.imread(img_path)
        if image is None:
            raise FileNotFoundError('Incorrect path')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        annotation = self.getAnnotation(img_path)

        # get bounding box coordinates for each traffic light
        coords = []
        state = []
        affect = []
        for _, row in annotation.iterrows():
            xmin = row["Upper left corner X"]
            xmax = row["Lower right corner X"]
            ymin = row["Upper left corner Y"]
            ymax = row["Lower right corner Y"]
            coords.append([xmin, ymin, xmax, ymax])
            state.append(CLASS_LABEL_MAP[row["Annotation tag"]])
            if CLASS_LABEL_MAP[row["Annotation tag"]] > 3:
                affect.append(False)
            else:
                affect.append(True)

        # coords = torch.as_tensor(coords, dtype=torch.float32)
        sample = {
            "image": image,
            "coords": np.array(coords),
            # "state": state,
            # "affect": np.array(affect)
        }

        if self.transform:
            sample = self.transform(sample)
        return sample

    def __len__(self):
        return len(self.imgs)
