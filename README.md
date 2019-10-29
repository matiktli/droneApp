# Flying Drone from scratch - Weekend Project

## Idea:
* Fly drone via script file :heavy_check_mark:
* Fly drone via ps4 controller :heavy_check_mark:
* Detec faces via drone camera:
  * CV2 Model :heavy_check_mark:
  * Own ML Model :construction:
* Fly drone via AI Model :heavy_check_mark:

## Technology stack:
* Python
* OpenCv, PsDrone
* Parrot Drone 2.0
* PS4 Controller

## MiniBlog:
* First Flight (drone camera):
https://youtu.be/9-TKB-jhHuk
* Face Detection with OpenCV (drone camera):
https://youtu.be/b6aHsCXbwkg

---
###  Run:
* Pre-requirements:
  * Parrot AR Drone 2.0 - connected
  * PS4 Controller - connected
  * Lib: OpenCv
* Run commands:
  * Normal run: `python app.py`
  * Dev mode (engines, recording disabled): `python app.py dev`
  
### Key binding:
* L_toggle -> left,right,forward,backward
* R_toggle -> turn_left,turn_right,up,down
* Triangle -> AI Mode
* Square -> Switch camera
* Circle -> Land
* X -> TakeOff
* Options -> shutdown
