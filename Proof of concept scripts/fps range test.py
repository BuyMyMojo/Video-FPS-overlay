# importing the required modules
import matplotlib.pyplot as plt
import csv
import numpy
from pandas import *

# settings
# x axis values (30 frame range for testing)
PresetFrameRange = 60
Title = "Frame range: 60"
Resolution = 1440
CSVPath = "FrameView-CSV\FrameView_Cyberpunk2077.exe_2021_05_31T190026_Log.csv"

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
FpsData = read_csv(CSVPath)

FullFrameTimes = FpsData['MsBetweenPresents'].tolist()
TrimFrameTimes = FullFrameTimes
del TrimFrameTimes[PresetFrameRange:]
TrimFrameRate = [1000/x for x in TrimFrameTimes]
FullFrameRate = [1000/x for x in FullFrameTimes]
Yaxis = FullFrameRate[0:PresetFrameRange]

# set plot size
plt.figure(figsize=(16, 4), dpi=DPI)

# plotting the points 
lines = plt.plot(Xaxis, Yaxis)
  
# naming the x axis
# plt.xlabel('Frame')

# naming the y axis
plt.ylabel('FPS')
  
# giving a title to my graph
plt.title('Fps from FrameView CSV test 1')

# function to show the plot
plt.show()
