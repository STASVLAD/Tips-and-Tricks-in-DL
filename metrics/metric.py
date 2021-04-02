"""We consider non overlapping sets of intervals only."""

import os
import json
import argparse

import numpy as np

THRESHOLD_IOU = 0.5


def parse_arguments():
    parser = argparse.ArgumentParser(description='Project evaluation metric')
    parser.add_argument(
        '-p',
        '--pred_path',
        required=True,
        type=str,
        help='Path to the prediction .json file',
    )
    parser.add_argument(
        '-gt',
        '--gt_path',
        required=True,
        type=str,
        help='Path to the ground truth .json file',
    )
    return parser.parse_args()


def tl_encode(tl_history):
    res = []
    if len(tl_history) == 1:
        res = [[tl_history[0], tl_history[0]]]
    elif len(tl_history) > 1:
        w = np.where(np.convolve(tl_history, [1, -1]) > 1)[0]
        if len(w) == 0 or w[0] != 0:
            w = np.concatenate(([0], w))
        if w[-1] != len(tl_history):
            w = np.concatenate((w, [len(tl_history)]))
        for i in range(len(w) - 1):
            res.append([tl_history[w[i]], tl_history[w[i + 1] - 1]])
    return res


def read_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def read_prediction(pred_path):
    assert os.path.exists(pred_path), "Pred file does not exist %s" % pred_path
    tl_history = {'green': [], 'yellow': [], 'red': []}
    data = read_json(pred_path)
    for frame_id in sorted(map(int, data.keys())):
        frame_idx_str = str(frame_id)
        for traffic_light_id in data[frame_idx_str]:
            traffic_light = data[frame_idx_str][traffic_light_id]
            if traffic_light['affect'] \
                    and traffic_light['state'] in tl_history.keys():
                tl_history[traffic_light['state']].append(frame_id)

    # Encode to intervals
    for color in tl_history:
        if len(tl_history[color]) > 0:
            tl_history[color] = tl_encode(tl_history[color])

    return tl_history


def calculate_iou(a, b):
    if a[1] >= b[0] and b[1] >= a[0]:
        intersection_int = [max(a[0], b[0]), min(a[1], b[1])]
        union_int = [min(a[0], b[0]), max(a[1], b[1])]
        intersection = intersection_int[1] - intersection_int[0]
        union = union_int[1] - union_int[0]
        if union > 0:
            return intersection / union
    return 0.0


def evaluate_f1(preds, trgs):
    def division(numerator, denominator):
        m = 0.0
        if denominator != 0:
            m = numerator / denominator
        return m

    if len(preds) > 0 or len(trgs) > 0:
        ious = [0.0] * len(preds)
        for i in range(len(preds)):
            for trg in trgs:
                iou = calculate_iou(preds[i], trg)
                if iou > ious[i]:
                    ious[i] = iou
        ious = np.array(ious) > THRESHOLD_IOU

        TP = np.count_nonzero(ious)
        FP = len(preds) - TP
        FN = len(trgs) - TP
        precision = division(TP, (TP + FP))
        recall = division(TP, (TP + FN))
        F1 = division(2 * precision * recall, (precision + recall))
    else:
        F1 = 1.0
    return F1


def metric(pred_path: str, gt_path: str):
    assert os.path.exists(pred_path), "Predictions file does not exist"
    assert os.path.exists(gt_path), "Ground truth file does not exist"
    pred = read_prediction(pred_path)
    gt = read_json(gt_path)
    print("Predicted:", pred)
    print("Ground truth:", gt)
    f1 = []
    print("Color metrics:")
    for tl_state in gt.keys():
        color_metric = evaluate_f1(pred[tl_state], gt[tl_state])
        f1.append(color_metric)
        print(tl_state, color_metric)
    print("Final result:", np.mean(f1))


if __name__ == '__main__':
    args = parse_arguments()
    metric(pred_path=args.pred_path, gt_path=args.gt_path)
