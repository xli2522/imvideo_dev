import matplotlib.pyplot as plt
import numpy as np

# test local
from imvideo import local

local.timelapse('demo.avi', 5,  r".\tests\test_image")  

# test memory
from imvideo import memory

def test_matplot_loop(n):
    '''This function tests the function
        Input:      n   number of frames
    '''
    images = []     # empty image container
    plt.figure()    # initialize matplotlib figure
    for i in range(n):
        plt.plot([np.random.randint(2), np.random.randint(2)])      # generate random plots for demo
        plt.title("test" + str(i))
        images = memory.savebuff(plt, images)      # save image in in-memory location
        plt.clf()
    
    memory.construct(images, 'matplot_demo.avi', 5)        # construct video; 5 fps

    return 

test_matplot_loop(100)      # construct a demo video with 100 frames