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
import argparse

def main(args):

    # settings
    CSVPath = args.CSV
    Resolution = args.r
    PresetFrameRange = args.dr
    Title = args.t
    if args.Output[-1] == "\\":
        OutFolder = args.Output
    elif args.Output[-1] == "/":
        OutFolder = args.Output
    else:
        print("Make sure the output path ends in either a \\ or a /")
        exit()
    colour = args.lc
    BackColour = args.bc
    transparentBackground = args.tb
    LineWidth = args.lw
    RemoveBox = not args.rb
    RemoveNumbers = not args.rl


    # reading CSV file
    FpsData = read_csv(CSVPath)

    # grab all frame times
    FullFrameTimes = FpsData['MsBetweenPresents'].tolist()
    FUllFrameRate = [1000/x if x > 0 else x == 0 for x in FullFrameTimes]
    VideoFrames = len(FullFrameTimes)
    del FullFrameTimes
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(PresetFrameRange):
        # FullFrameTimes.insert(0, 0) # to add back in later when implamenting frametime graph
        FUllFrameRate.insert(0, 0)
    
    FpsGraphNvidiaFrameview(transparentBackground, Resolution, VideoFrames, Title, PresetFrameRange, FUllFrameRate, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers)


def FpsGraphNvidiaFrameview(transparentBackground, Resolution, VideoFrames, Title, PresetFrameRange, FUllFrameRate, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers):

    # setup graph
    fig, ax = plt.subplots()
    Transparency = 1.0
    if transparentBackground == True:
        Transparency = 0.0


    fig.patch.set_alpha(Transparency)


    if Resolution == 720:
        DPI = 45
    elif Resolution == 1080:
        DPI = 120
    elif Resolution == 1440:
        DPI = 160
    elif Resolution == 2160:
        DPI = 240


    # generate graph frames
    for i in range(VideoFrames):
        trimRange = PresetFrameRange+i

        Xaxis = []
        Xaxis = [t for t in range(PresetFrameRange)]

        lines = ax.plot(Xaxis, FUllFrameRate[i:trimRange], color=colour, linewidth=LineWidth)

        ax.set_ylim(0, 120)
        fig.dpi = DPI
        fig.set_size_inches(16, 4)
        ax.set_ylabel('FPS')
        ax.set_title(Title)
        ax.tick_params(axis='both', colors=BackColour, bottom=RemoveBox, top=RemoveBox, left=RemoveBox, right=RemoveBox, labelleft=RemoveNumbers, labelbottom=RemoveNumbers)
        ax.spines['left'].set_visible(RemoveBox)
        ax.spines['right'].set_visible(RemoveBox)
        ax.spines['bottom'].set_visible(RemoveBox)
        ax.spines['top'].set_visible(RemoveBox)
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

# setup argparse
parser = argparse.ArgumentParser(description='Generates image sequences from FPS/FrameTime information captured by Nvidia FrameView.', allow_abbrev=False)

# add arguments
parser.add_argument('CSV', metavar='CSV', type=str, help='The path to your CSV file')
parser.add_argument('Output', metavar='Output', type=str, help='The path your image sequence will be saved')
parser.add_argument('-r', metavar='Resolution', type=int, help='Resolution of recording [720, 1080, 1440, 2160] [default: 1080]', default=1080)
parser.add_argument('-t', metavar='Title', type=str, help='Set the title of the graph', default=" ")
parser.add_argument('-dr', metavar='Range', type=int, help='Sets the X length of the graph in data points (example: 90 will have the graph show 90 data values at once) ', default=90)
parser.add_argument('-lc', metavar='Colour', type=str, help='Set the colour of the line [format: matplotlib colors] [default: red]', default="r")
parser.add_argument('-bc', metavar='Colour', type=str, help='Set the colour of the axis and markers [format: matplotlib colors] [default: black]', default="black")
parser.add_argument('-tb', metavar='bool', type=bool, help='Set background of the graph to transparent [default: True]', default=True)
parser.add_argument('-lw', metavar='width', type=int, help='Set line width [default: 1]', default=1)
parser.add_argument('-rb', metavar='bool', type=bool, help='Disable box around line [default: False]', default=False)
parser.add_argument('-rl', metavar='bool', type=bool, help='Disable numbers around edge [default: False]', default=False)


args = parser.parse_args()

if len(sys.argv) != 1:
    main(args)
