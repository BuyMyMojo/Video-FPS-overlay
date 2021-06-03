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


def main():

    # settings
    PresetFrameRange = 90
    VideoFrames = 41128
    Title = "Test1"
    Resolution = 1440
    CSVPath = "FrameView-CSV\FrameView_Cyberpunk2077.exe_2021_05_31T190026_Log.csv"
    OutFolder = "test video\\"
    colour = "r"
    BackColour = "white"
    transparentBackground = True


    # reading CSV file
    FpsData = read_csv(CSVPath)

    # grab all frame times
    FullFrameTimes = FpsData['MsBetweenPresents'].tolist()
    # convert into fps
    FUllFrameRate = [1000/x if x > 0 else x == 0 for x in FullFrameTimes]
    del FullFrameTimes
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(PresetFrameRange):
        # FullFrameTimes.insert(0, 0) # to add back in later when implamenting frametime graph
        FUllFrameRate.insert(0, 0)
    
    FpsGraphNvidiaFrameview(transparentBackground, Resolution, VideoFrames, Title, PresetFrameRange, FUllFrameRate, colour, BackColour, OutFolder)

def help():
    print("""
    AnimPlot1.py: AnimPlot1.py [CSV path] [-F]
                  AnimPlot1.py [-h]
    Generates image sequences from FPS/FrameTime information captured by Nvidia FrameView.

    Options:
      -F        CSV is from Nvidia FrameView
      -h        Shows this page
        CSV path

    Arguments:
      CSV path   Location of the CSV you are generating the graph from""")
    

def FpsGraphNvidiaFrameview(transparentBackground, Resolution, VideoFrames, Title, PresetFrameRange, FUllFrameRate, colour, BackColour, OutFolder):

    # setup graph
    fig, ax = plt.subplots()
    Transparency = 1.0
    if transparentBackground == True:
        Transparency = 0.0


    fig.patch.set_alpha(Transparency)


    if Resolution == 720 or 1280:
        DPI = 45
    elif Resolution == 1080 or 1920:
        DPI = 120
    elif Resolution == 1440 or 2560:
        DPI = 160
    elif Resolution == 2160 or 3840:
        DPI = 240

    fig.dpi = DPI
    fig.set_size_inches(16, 4)
    ax.set_ylabel('FPS')
    ax.set_title(Title)


    # generate graph frames
    for i in range(VideoFrames):
        trimRange = PresetFrameRange+i

        Xaxis = []
        Xaxis = [t for t in range(PresetFrameRange)]

        lines = ax.plot(Xaxis, FUllFrameRate[i:trimRange], color=colour)

        ax.set_ylim(0, 120)
        ax.tick_params(axis='both', colors=BackColour)
        ax.spines['left'].set_color(BackColour)
        ax.spines['right'].set_color(BackColour)
        ax.spines['top'].set_color(BackColour)
        ax.spines['bottom'].set_color(BackColour)

        # save as png
        plt.savefig(OutFolder + "Frame_" + str(i+1) + '.png', transparent=transparentBackground)
        ax.cla()

        print('Processed frame ' + str(i+1) + ' of ' + str(VideoFrames) + " " + str((i+1)*100/VideoFrames) + "%" + ' FPS graph')

        del trimRange
        del Xaxis
        del lines
        gc.collect()

    print("Completed!")


if len(sys.argv) == 1:
    help()
elif len(sys.argv) == 2 and sys.argv[1] == "-h":
    help()
elif len(sys.argv) != 1:
    main()