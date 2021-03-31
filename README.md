# Traffic Light Recognition Using Deep Learning

## Рассмотренные датасеты:
* [Lisa Traffic Lights Dataset](https://www.kaggle.com/mbornoe/lisa-traffic-light-dataset)
* * Был использован как основной датасет, т.к. не требовал большой работы по очистке и преобразованию данных, понятных нейросети
* [DriveU Traffic Light Dataset (DTLD)](https://www.uni-ulm.de/en/in/driveu/projects/driveu-traffic-light-dataset/)
* * Отказались по причине необходимости писать парсинги для извлечения tiff-файлов и калибрации
* [Bosch Small Traffic Lights Dataset](https://hci.iwr.uni-heidelberg.de/content/bosch-small-traffic-lights-dataset)
* * Отсутствие внятной документации
  
## Статьи
* [Traffic Light Detection with ConvolutionalNeural Networks and 2D Camera Data](https://www.mi.fu-berlin.de/inf/groups/ag-ki/Theses/Completed-theses/Bachelor-theses/2020/Hein/BA-Hein.pdf)
* https://github.com/level5-engineers/system-integration/wiki/Traffic-Lights-Detection-and-Classification
* https://arxiv.org/pdf/1906.11886.pdf
* A Deep Analysis of the Existing Datasets for Traffic Light State Recognition
  
## Комментарии, эксперименты, процесс работы
1. В сравнении кодеров-декодеров видео очевидно более быстрой оказалась утилита ffmpeg, в папку modules были добавлен data unpacker.
2. LISA была размечена при помощи pandas, были убраны все ненужные параметры (например, на какое видео ссылается кадр). Итоговый датафрейм состоял из frame_id, уникального идентификатора кадра, путь к кадру, бокс светофора, и его состояние (можно найти в meta.csv)
3. Первоначальной идеей для модели предсказания было взять уже предобученную CNN, используя Torch Hub. Изучив SOTA в отношении детекции обьектов, мы решили обратить внимание на R-CNN, а конкретно, Faster R-CNN, она имелась в хабе, а значит ее несложно было заимплементить в общий проект, к тому же, была одной из лучших по томчности предсказаний. Также, запасным вариантом была YOLO, т.к. была достаточно быстрой и практически везде всплывала. Был дописан переход от боксов Lisa к YOLO. $$ (x_min, y_min, x_max, y_max) \implies (x, y, width, height)$$
 
