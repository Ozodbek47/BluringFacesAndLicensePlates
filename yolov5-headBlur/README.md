##  Head & Person Detection Model 

### Download model trained on crowd human using yolov5(m) architeture
Download Link:  [YOLOv5m-crowd-human](https://drive.google.com/file/d/1gglIwqxaH2iTvy6lZlXuAcMpd_U0GCUb/view?usp=sharing)

## To blur the heads of people:

```bash
python3 detect.py --weights crowdhuman_yolov5m.pt --source _test/ --heads
```

<br/>

**Output (Crowd Human Model)**

![image](output.png)

<br/>



## Test

```bash
$ python detect.py --weights crowdhuman_yolov5m.pt --source _test/ --view-img

```
  
  
## Test (Only Person Class)

```bash
python3 detect.py --weights crowdhuman_yolov5m.pt --source _test/ --view-img  --person
```

## Reference:
https://github.com/deepakcrk/yolov5-crowdhuman