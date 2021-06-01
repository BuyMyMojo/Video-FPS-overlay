# importing the required modules
import matplotlib.pyplot as plt
import csv
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

if Resolution == 1080:
    DPI = 120
elif Resolution == 1440:
    DPI = 160
elif Resolution == 2160:
    DPI = 240


Xaxis = []
for x in range(PresetFrameRange):
  Xaxis.append(x+1)
# reading CSV file
FpsData = read_csv("FrameView-CSV\\FrameView_Cyberpunk2077.exe_2021_05_31T190026_Log.csv")

# grab all frame times
FullFrameTimes = FpsData['MsBetweenPresents'].tolist()
# convert into fps
FUllFrameRate = [1000/x if x > 0 else x == 0 for x in FullFrameTimes]
# add Frame Range -1 blank values at the start for the animation
for j in range(PresetFrameRange):
    FullFrameTimes.insert(0, 0)
    FUllFrameRate.insert(0, 0)

for i in range(VideoFrames):
    plt.close("all")
    trimRange = PresetFrameRange+i
    

    # add frame times here to be trimmed
    TrimFrameTimes = FullFrameTimes[i:trimRange]


    TrimFrameRate = FUllFrameRate[i:trimRange]


    Yaxis = TrimFrameRate

    plt.close('all')
    # set plot size and limit
    plt.figure(figsize=(16, 4), dpi=DPI)
    plt.ylim([0,120])
    # plotting the points 
    lines = plt.plot(Xaxis, Yaxis)
    
    
    # naming the x axis
    # plt.xlabel('Frame')

    # naming the y axis
    plt.ylabel('FPS')
    
    # giving a title to my graph
    plt.title(Title)

    # change graph settings
    plt.setp(lines, c=colour)

    # save as png
    plt.savefig(OutFolder + "Frame_" + str(i+1) + '.png', transparent=False)
    plt.clf()
    plt.cla()
    plt.close('all')
    
    print('Processed frame ' + str(i+1) + ' of ' + str(VideoFrames) + ' FPS graph')
    del trimRange
    del TrimFrameTimes
    del TrimFrameRate
    del Yaxis
    del lines
    gc.collect()