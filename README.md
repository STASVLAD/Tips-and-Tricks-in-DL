# Traffic Light Recognition Using Deep Learning

## Datasets
* [Lisa Traffic Lights Dataset](https://www.kaggle.com/mbornoe/lisa-traffic-light-dataset)
* [DriveU Traffic Light Dataset (DTLD)](https://www.uni-ulm.de/en/in/driveu/projects/driveu-traffic-light-dataset/)

  Download link: https://cloudstore.uni-ulm.de/s/KrGTDX3XRNAY5yX
* [Bosch Small Traffic Lights Dataset](https://hci.iwr.uni-heidelberg.de/content/bosch-small-traffic-lights-dataset)

  Download link: https://hci.iwr.uni-heidelberg.de/node/6132/download/abfbf7d7364bd12c80c252ac4f0bf85d
  
## Resources
* [Traffic Light Detection with ConvolutionalNeural Networks and 2D Camera Data](https://www.mi.fu-berlin.de/inf/groups/ag-ki/Theses/Completed-theses/Bachelor-theses/2020/Hein/BA-Hein.pdf)
* https://github.com/level5-engineers/system-integration/wiki/Traffic-Lights-Detection-and-Classification
* https://arxiv.org/pdf/1906.11886.pdf
* A Deep Analysis of the Existing Datasets for Traffic Light State Recognition

  Download Link: ???
  
## Comments
Датасета с широкой географией я не нашел. Во многих статьях используют именно эти три датасета (обычно в паре), которые у нас и перечислены. Последняя статья в __Resources__ по названию самое то, чтобы понять, какие подводные камни в подборе датасетов, но я чо-т не понял, как скачать её, завтра чекну внимательнее. 
По географии нашел только след. инфу (выдержки из статей в __Resources__): 

```German  traffic  lights  for  example  are  located  at  the beginning of an intersection, while traffic lights in the United States of America are located at the end of an intersection```;

```Problems arise when the objects appear in an orientation that was not present in the training data or when the color changes too dramatically ... Both  BSTLD  and  DTLD  had  their  cameras  perfectly centered and leveled in the car. The cameras of the self-driving car from Freie Universität Berlin are pointed more towards the sky and rotated by a couple degrees, which makes the traffic lights appear diagonal in the image```.

Поэтому получается, что данных датасетов должно хватить, надо будет только как-то случайно трансформить кадры, чтоб имитировать разных угол камер и т.д. И насчет цветов внимательнее почитать, но пока хватит этого. Завтра ещё ту последнюю статью прочитаю и вообще все ясно станет. 
