from time import time
import matplotlib.pyplot as plt
from matplotlib import animation
from pandas import *
from datetime import datetime

con = 0

def main():
    CSVPath = "F:\\Documents\\GitHub\\Video-FPS-overlay\\FrameView-CSV\\FrameView_ds.exe_2021_06_04T224922_Log.csv"
    Title = "Time graph test"
    OutFolder = "F:\\Documents\\GitHub\\Video-FPS-overlay\\time Graph Test\\"
    PresetFrameRange = 240

    FpsGraphFV(CSVPath, Title, PresetFrameRange, colour="r", BackColour="black", OutFolder=OutFolder, LineWidth=1.5, RemoveBox=None, RemoveNumbers=None, ymin=0, ymax=250, TextColour="white", centerLine=True, grid=True, FPSLocation=None, mode="FPS")

def FpsGraphFV(CSVPath, Title, PresetFrameRange, colour, BackColour, OutFolder, LineWidth, RemoveBox, RemoveNumbers, ymin, ymax, TextColour, centerLine, grid, FPSLocation, mode):

    # reading CSV file
    FpsData = read_csv(CSVPath)

    # grab all frame times
    FullFrameTimes = FpsData['MsBetweenPresents'].tolist()
    FUllFrameRate = [1000/x if x > 0 else x == 0 for x in FullFrameTimes]
    VideoFrames = len(FullFrameTimes)
    TimeInSeconds = FpsData['TimeInSeconds'].tolist()

    # for i in FpsData['TimeInSeconds'].tolist().count():
    #     if i != 0:
    #         x = FpsData['TimeInSeconds'].tolist()[i-1]
    #     else:
    #         x = FpsData['TimeInSeconds'].tolist()[i]
    
    # del FullFrameTimes
    # add Frame Range -1 blank values at the start for the animation 
    # for j in range(PresetFrameRange):
    #     # FullFrameTimes.insert(0, 0) # to add back in later when implamenting frametime graph
    #     FUllFrameRate.insert(0, 0)

    # setup graph
    fig, ax = plt.subplots()
    Transparency = 1.0


    fig.patch.set_alpha(Transparency)

    DPI = 240

    xsize = 16

    ysize = 9

    transparentBackground = False

    RemoveBox = False

    # run graph
    graph(VideoFrames, PresetFrameRange, ax, FUllFrameRate, colour, LineWidth, ymin, ymax, fig, DPI, Title, TextColour, BackColour, RemoveBox, RemoveNumbers, OutFolder, transparentBackground, xsize, ysize, centerLine, grid, FPSLocation, mode, TimeInSeconds, ticks=4)

def graph(VideoFrames, PresetFrameRange, ax, Data, colour, LineWidth, ymin, ymax, fig, DPI, Title, TextColour, BackColour, RemoveBox, RemoveNumbers, OutFolder, transparentBackground, xsize, ysize, centerLine, grid, FPSLocation, mode, TimeInSeconds,ticks=4, ):
    # generate graph frames
    start = time()
    for i in range(1):
        if mode == "FPS":
            trimRange = PresetFrameRange+i
        elif mode == "FT":
            trimRange = PresetFrameRange+i
        

        Xaxis = []
        if mode == "FPS":
            Xaxis = TimeInSeconds
        elif mode == "FT":
            Xaxis = [t for t in range(int(PresetFrameRange))]
        

        if mode == "FPS":
            lines = ax.plot(Xaxis, Data, color=colour, linewidth=LineWidth)
        elif mode == "FT":
            lines = ax.plot(Xaxis, Data[i:int(trimRange)], color=colour, linewidth=LineWidth, drawstyle='steps-pre')

        ax.set_ylim(ymin, ymax)
        ax.set_xlim(0, PresetFrameRange)
        fig.dpi = DPI
        fig.set_size_inches(xsize, ysize)
        ax.set_title(Title, {'color': TextColour})
        ax.xaxis.label.set_color(TextColour)
        ax.yaxis.label.set_color(TextColour)
        ax.tick_params(axis='both', colors=BackColour, bottom=RemoveBox, top=RemoveBox, left=RemoveBox, right=RemoveBox, labelleft=RemoveNumbers, labelbottom=RemoveNumbers)
        if mode == "FT":
            if ticks == 3:
                plt.yticks([0, ymax/2, ymax])
            elif ticks == 4:
                plt.yticks([0, ymax/3, ymax/3*2, ymax])
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

    print("Completed!")
    timeTaken = time() - start
    timeTaken = str(timeTaken)
    print(f'Time taken: {timeTaken[0:5]}')


main()