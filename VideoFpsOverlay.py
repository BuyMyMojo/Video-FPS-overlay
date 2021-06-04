#!/usr/bin/env python3

# importing the required modules
import argparse as argp
import os
import sys
from time import time
import matplotlib 
from matplotlib import pyplot as plt
from pandas import *
import gc

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
    ymin = args.ymin
    ymax = args.ymax
    TextColour = args.tc
    xsize = args.xinch
    ysize = args.yinch
    centerLine = args.cl
    grid = args.g
    FPSLocation = args.fl
    mode = args.m
    

    if mode == "FPS":
        if args.f == "NV":
            FpsGraphFV(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, ymin, ymax, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode)
        elif args.f == "MS":
            FpsGraphMS(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, ymin, ymax, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode)
        elif args.f == "MH":
            FpsGraphMH(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, ymin, ymax, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode)
        else:
            return(print("Make sure you have the right format set"))
    elif mode == "FT":
        if args.f == "NV":
            FTGraphFV(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, ymin, ymax, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode)
        elif args.f == "MS":
            FTGraphMS(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, ymin, ymax, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode)
        elif args.f == "MH":
            FTGraphMH(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, ymin, ymax, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode)
        else:
            return(print("Make sure you have the right format set"))
    else:
        print("Make sure you have mode set correctly")
        return()


def FpsGraphFV(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, ymin, ymax, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode):

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

    if xsize == None:
        xsize = 16

    if ysize == None:
        ysize = 4

    # run graph
    graph(VideoFrames, PresetFrameRange, ax, FUllFrameRate, colour, LineWidth, ymin, ymax, fig, DPI, Title, TextColour, BackColour, RemoveBox, RemoveNumbers, OutFolder, transparentBackground, xsize, ysize, centerLine, grid, FPSLocation, mode)

def FTGraphFV(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, ymin, ymax, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode):

    # reading CSV file
    FpsData = read_csv(CSVPath)

    # grab all frame times
    FullFrameTimes = FpsData['MsBetweenPresents'].tolist()
    VideoFrames = len(FullFrameTimes)
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(int(PresetFrameRange/2)):
        # FullFrameTimes.insert(0, 0) # to add back in later when implamenting frametime graph
        FullFrameTimes.insert(0, 0)

    # double up data for square graph?
    # SquareFrames = [val for val in FullFrameTimes for _ in (0, 1)]
    # del FullFrameTimes

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

    if xsize == None:
        xsize = 12

    if ysize == None:
        ysize = 4

    if ymax == None:
        ymax = 50

    # run graph
    graph(VideoFrames, PresetFrameRange, ax, FullFrameTimes, colour, LineWidth, ymin, ymax, fig, DPI, Title, TextColour, BackColour, RemoveBox, RemoveNumbers, OutFolder, transparentBackground, xsize, ysize, centerLine, grid, FPSLocation, mode)

def FpsGraphMS(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, ymin, ymax, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode):

    # reading CSV file
    FpsData = read_csv(CSVPath, skiprows=2, usecols=[26], squeeze=True)

    # grab all frame times
    FUllFrameRate = FpsData.tolist()
    FUllFrameRate = FUllFrameRate[31:]
    VideoFrames = len(FUllFrameRate)
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(PresetFrameRange):
        # FullFrameTimes.insert(0, 0) # to add back in later when implamenting frametime graph
        FUllFrameRate.insert(0, 0)

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

    if xsize == None:
        xsize = 16

    if ysize == None:
        ysize = 4

    # run graph
    graph(VideoFrames, PresetFrameRange, ax, FUllFrameRate, colour, LineWidth, ymin, ymax, fig, DPI, Title, TextColour, BackColour, RemoveBox, RemoveNumbers, OutFolder, transparentBackground, xsize, ysize, centerLine, grid, FPSLocation, mode)


def FpsGraphMH(CSVPath, transparentBackground, Resolution, Title, PresetFrameRange, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, ymin, ymax, TextColour, xsize, ysize, centerLine, grid, FPSLocation, mode):

    # reading CSV file
    FpsData = read_csv(CSVPath, skiprows=2, usecols=[0], squeeze=True)

    # grab all frame times
    FUllFrameRate = FpsData.tolist()
    VideoFrames = len(FUllFrameRate)
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(PresetFrameRange):
        # FullFrameTimes.insert(0, 0) # to add back in later when implamenting frametime graph
        FUllFrameRate.insert(0, 0)

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

    if xsize == None:
        xsize = 16

    if ysize == None:
        ysize = 4

    # run graph
    graph(VideoFrames, PresetFrameRange, ax, FUllFrameRate, colour, LineWidth, ymin, ymax, fig, DPI, Title, TextColour, BackColour, RemoveBox, RemoveNumbers, OutFolder, transparentBackground, xsize, ysize, centerLine, grid, FPSLocation, mode)




def graph(VideoFrames, PresetFrameRange, ax, Data, colour, LineWidth, ymin, ymax, fig, DPI, Title, TextColour, BackColour, RemoveBox, RemoveNumbers, OutFolder, transparentBackground, xsize, ysize, centerLine, grid, FPSLocation, mode):
    # generate graph frames
    start = time()
    for i in range(VideoFrames):
        if mode == "FPS":
            trimRange = PresetFrameRange+i
        elif mode == "FT":
            trimRange = PresetFrameRange/2+i
        

        Xaxis = []
        if mode == "FPS":
            Xaxis = [t for t in range(PresetFrameRange)]
        elif mode == "FT":
            Xaxis = [t for t in range(int(PresetFrameRange/2))]
        

        if mode == "FPS":
            lines = ax.plot(Xaxis, Data[i:trimRange], color=colour, linewidth=LineWidth)
        elif mode == "FT":
            lines = ax.plot(Xaxis, Data[i:int(trimRange)], color=colour, linewidth=LineWidth, drawstyle='steps-pre')

        ax.set_ylim(ymin, ymax)
        ax.set_xlim(0, PresetFrameRange/2)
        fig.dpi = DPI
        fig.set_size_inches(xsize, ysize)
        ax.set_title(Title, {'color': TextColour})
        ax.xaxis.label.set_color(TextColour)
        ax.yaxis.label.set_color(TextColour)
        ax.tick_params(axis='both', colors=BackColour, bottom=RemoveBox, top=RemoveBox, left=RemoveBox, right=RemoveBox, labelleft=RemoveNumbers, labelbottom=RemoveNumbers)
        if FPSLocation == "left":
            ax.tick_params(axis='y', labelleft=True, labelright=False)
        elif FPSLocation == "right":
            ax.tick_params(axis='y', labelleft=False, labelright=True)
        elif FPSLocation == "both":
            ax.tick_params(axis='y', labelleft=True, labelright=True)
        ax.spines['left'].set_visible(RemoveBox)
        ax.spines['right'].set_visible(RemoveBox)
        ax.spines['bottom'].set_visible(RemoveBox)
        ax.spines['top'].set_visible(RemoveBox)
        ax.spines['left'].set_color(BackColour)
        ax.spines['right'].set_color(BackColour)
        ax.spines['top'].set_color(BackColour)
        ax.spines['bottom'].set_color(BackColour)
        if centerLine == True:
            ax.axvline(x=PresetFrameRange/2, ymin=0, ymax=1, color=BackColour)
        if grid == True:
            ax.grid(b=None, which='major', axis='y')

        # save as png
        plt.savefig(OutFolder + "Frame_" + str(i+1) + '.png', transparent=transparentBackground, backend='Agg')
        ax.cla()

        print('Processed frame ' + str(i+1) + ' of ' + str(VideoFrames) + " " + str((i+1)*100/VideoFrames)[0:5] + "%" + ' FPS graph')

        del trimRange
        del Xaxis
        del lines
        gc.collect()

    print("Completed!")
    print(f'Time taken: {time() - start}')

# setup argparse
parser = argp.ArgumentParser(description='''Generates image sequences from FPS/FrameTime information captured by FPS recording software (only Nvidia FrameView support right now).
Supported files: .csv and MSI Afterburner .hml''', allow_abbrev=False)

# add arguments
parser.add_argument('CSV', metavar='CSV', type=str, help='The path to your CSV file')
parser.add_argument('-f', metavar='Format', type=str, help='Choose what format the csv is in [FV = FrameView, MS = MSI afterburner, MH = MangoHud] [default: FrameView]', default="FV")
parser.add_argument('-m', metavar='Mode', type=str, help='Choose what weather to render FPS or FrameTime graph [FPS = FPS, FT = FrameTime] [default: FPS]', default="FPS")
parser.add_argument('Output', metavar='Output', type=str, help='The path your image sequence will be saved')
parser.add_argument('-r', metavar='Resolution', type=int, help='Resolution of recording [720, 1080, 1440, 2160] [default: 1080]', default=1080)
parser.add_argument('-t', metavar='Title', type=str, help='Set the title of the graph', default=" ")
parser.add_argument('-dr', metavar='Range', type=int, help='Sets the X length of the graph in data points (example: 90 will have the graph show 90 data values at once) [default : 120]', default=120)
parser.add_argument('-lc', metavar='Colour', type=str, help='Set the colour of the line [format: matplotlib colors] [default: red]', default="r")
parser.add_argument('-bc', metavar='Colour', type=str, help='Set the colour of the axis and markers [format: matplotlib colors] [default: black]', default="black")
parser.add_argument('-tc', metavar='Colour', type=str, help='Set the colour of the text [format: matplotlib colors] [default: black]', default="black")
parser.add_argument('-tb', action='store_true', help='Set background of the graph to transparent')
parser.add_argument('-lw', metavar='width', type=int, help='Set line width [default: 1]', default=1)
parser.add_argument('-rb', action='store_true', help='Disable box around line')
parser.add_argument('-rl', action='store_true', help='Disable numbers around edge')
parser.add_argument('-cl', action='store_true', help='Add center line')
parser.add_argument('-g', action='store_true', help='Add grid')
parser.add_argument('-ymin', metavar='min', type=int, help='Set min y axis range [default: 0]', default=None)
parser.add_argument('-ymax', metavar='max', type=int, help='Set max y axis range [default: FPS 120 | FT 50]', default=None)
parser.add_argument('-xinch', metavar='size', type=int, help='Set the width of the graph. This affects output resolution [Defaults: 16 for FPS | 12 for FT]', default=None)
parser.add_argument('-yinch', metavar='size', type=int, help='Set the height of the graph. This affects output resolution [Defaults: 4 for FPS | 4 for FT]', default=None)
parser.add_argument('-fl', metavar='Location', type=str, help='Set the location of the FPS numbers (left, right, both) [Default: right]', default="right")


args = parser.parse_args()

if len(sys.argv) != 1:
    main(args)
