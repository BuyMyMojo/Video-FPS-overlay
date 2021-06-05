from os import times
from pandas import read_csv
import math

Data = read_csv("FrameView-CSV\\FrameView_ds.exe_2021_06_04T224922_Log.csv")

Times = Data['TimeInSeconds'].tolist()
SetRange = float(2) #range in seconds

EndRange = None
for j in range(1700):
    
    for i in range(len(Times)):
        
        Math = float(Times[i])-float(Times[j])
        outMath = math.trunc(Math)
        if outMath == SetRange:
            EndRange = i
            break

    print("Range for time = ["+ str(j) +":"+ str(EndRange) +"]")
    
