# ANONYMIZING HEADS, FACES & LICENSE PLATES IN A VIDEO, IMAGE OR WEBCAM STREAM

Mass License Plate & Head blurring / pixelation using Yolov5 | Simple face blurring using Mediapipe

## HOW DOES IT WORK?
<br>
<img src="Steps.png" />
<br>

## For bluring heads, go to "yolov5-headBlur" folder, download the model and run:

```bash
python3 detect.py --weights crowdhuman_yolov5m.pt --source [your-video.mp4 / 0 for webcam / your-image.jpg] --heads
```

## For bluring license plates, go to "yolov5-lpBlur" folder, download the model and run:

```bash
python3 detect.py --weights detection_best.pt --source [your-video.mp4 / 0 for webcam / your-image.jpg] --view-img
```

## For simple webcam face bluring:

```bash
python3 faceBlur.py
```

### SAMPLE OUTPUTS

Blurring Result:
<br><br>
<img src="yolov5-headBlur/output.png" width="400"/> <img src="yolov5-lpBlur/output.png" width="400"/>
<br><br>
Pixelation Result:
<br><br>
<img src="pixelation.png" width="800" />