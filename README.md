# Imvideo 

Imvideo helps you create time-lapse videos from camera-generated **image folder** and your **matplotlib** loop.

### Install Imvideo

------

To install this package, type **pip install imvideo** in command prompt.

```None
C:\Users\user>pip install imvideo
Collecting imvideo
  Using cached imvideo-0.0.1-py3-none-any.whl (3.6 kB)
Installing collected packages: imvideo
Successfully installed imvideo-0.0.1
```

### Function Details

------

Class local:	***timelapse(title, fps, folder_path, inspect=True):***

```
timelapse(title, fps, folder_path, inspect=True):
Function constructs time-lapse video from images in a folder.
        Inputs:     title   (string)     video title + .avi
                    fps     (double)     time-lapse video frames per second 
                    folder_path    (raw string)    location of the image folder
                    inspect    (boolean)       True (default)/False
        Output:
                    time-lapse video
```

------

Class memory: 	***savebuff(frame, container):***

```
savebuff(frame, container):
Function saves image in in-memory location
         Inputs:    frame   (matplotlib image)  
                    container   (list)     empty image container
         Output:    container   (list)      image container with added frame location
```

***construct(container, title, fps, inspect=True):***

```
construct(container, title, fps, inspect=True):
Function constructs video from images in the container.
         Inputs:    container   (list)      image container with frame location
                    title   (string)     video title + .avi
                    fps     (double)     time-lapse video frames per second 
                    inspect    (boolean)       True (default)/False
         Output:
                    video
```

### Use Imvideo

------

1. Time-lapse video from a image folder:

```python
import imvideo as imv

imv.local.timelapse('demo.avi', 5,  r".\tests\test_image"))
```

2. Time-lapse video from a matplotlib loop:

```python
import imvideo as imv

def test_matplot_loop(n):
    ''' Input:      n   number of frames'''
    images = []     # empty image container
    plt.figure()    
    for i in range(n):
        plt.plot([np.random.randint(2), np.random.randint(2)])
        plt.title("test" + str(i))
        images = imv.memory.savebuff(plt, images)      # save image in in-memory location
        plt.clf()
    
    imv.memory.construct(images, 'matplot_demo.avi', 5)        # construct video; 5 fps

    return 

test_matplot_loop(100)      # construct a demo video with 100 frames
```

### Sample output

![Solve Laplace](https://github.com/xli2522/LaplaceRelaxation/blob/master/solution.gif?raw=true)
