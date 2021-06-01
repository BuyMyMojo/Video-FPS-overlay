#!/usr/bin/env python3

# importing the required modules
import argparse as argp
import os
import statistics
import sys

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from pandas import *
import gc

# settings
# x axis values (30 frame range for testing)
PresetFrameRange = 80
VideoFrames = 41128
Title = "Test1"
Resolution = 1440
CSVPath = "FrameView-CSV\FrameView_Cyberpunk2077.exe_2021_05_31T190026_Log.csv"
OutFolder = "test video\\"
colour = "r"


# reading CSV file
FpsData = read_csv("FrameView-CSV\\FrameView_Cyberpunk2077.exe_2021_05_31T190026_Log.csv")

# grab all frame times
FullFrameTimes = FpsData['MsBetweenPresents'].tolist()
# convert into fps
FUllFrameRate = [1000/x if x > 0 else x == 0 for x in FullFrameTimes]
del FullFrameTimes
gc.collect()
# add Frame Range -1 blank values at the start for the animation
for j in range(PresetFrameRange):
    # FullFrameTimes.insert(0, 0)
    FUllFrameRate.insert(0, 0)

# setup graph
fig, ax = plt.subplots()
fig.patch.set_alpha(0.0)
if Resolution == 720:
    DPI = 45
elif Resolution == 1080:
    DPI = 120
elif Resolution == 1440:
    DPI = 160
elif Resolution == 2160:
    DPI = 240

fig.dpi = DPI
fig.set_size_inches(16, 4)
ax.set_ylim(0, 120)
ax.set_ylabel('FPS')
ax.set_title(Title)

for i in range(VideoFrames):
    plt.close("all")
    trimRange = PresetFrameRange+i

    Xaxis = []
    Xaxis = [t for t in range(PresetFrameRange)]
    # plt.xlim(Xaxis[0] - Xaxis[60], Xaxis[60])

    lines = ax.plot(Xaxis, FUllFrameRate[i:trimRange], color="red")
    # lines.set_data(Xaxis, FUllFrameRate[i:trimRange])

    # save as png
    plt.savefig(OutFolder + "Frame_" + str(i+1) + '.png', transparent=False)
    ax.cla()
    plt.close('all')

    print('Processed frame ' + str(i+1) + ' of ' + str(VideoFrames) + ' FPS graph')

    del trimRange
    del Xaxis
    del lines
    gc.collect()