# Drones: Hand and finger recognition
## Introduction
This is a short guide for using the Tello's built-in camera to recognize your hand and count how many fingers you're holding up. We've put together the code for you ahead of time, but there are some suggested activities at the end for you to work on.

To prepare, you'll need to make sure you download the imrec.py Python script, and that you've installed the required libraries:

- NumPy

- OpenCV

- av

- TelloPy

We're only providing a very bare-bones approach, based on [pre-existing finger detection code on GitHub](https://github.com/lzane/Fingers-Detection-using-OpenCV-and-Python) and [the TelloPy API code](https://github.com/hanyazou/TelloPy). The code will connect to the Tello camera, isolate your hand, and count how many fingers you're holding up. In preparing the code I've cut out the included background detection and removal to speed up runtime. 

The instructions to do this are quite simple:

1. Turn on the drone with the small button on the left hand side.

2. Connect to the WiFi network being broadcast by the drone - it will be called something like "TELLO-AB22DD". 

3. Run the Python script:

```shell
python3 imrec.py
```

4. Put your hand into the blue bounding box on screen. In the terminal you should see the amount of fingers you're holding up. 

## Extension
Where can you go from here? The provided code is - intentionally - very barebones. What we've provided you with is a basic way of viewing what the Tello camera is streaming, and doing basic image recognition on that.

Here are a few suggested ways you could build on top of it:

1. Use other Tello API commands within the script: for example, have the drone take off before you start doing image recognition.

2. Use the count of fingers as a command: for example, one finger = take off, two fingers = land, etc...

3. (Hard) Try playing rock paper scissors with the drone: you use hand gestures to choose what to play, and the drone could do its own moves against you. 
