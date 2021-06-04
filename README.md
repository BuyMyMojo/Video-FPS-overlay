# Video FPS overlay
 Create FPS graph overlays like TRDrop and Digital Foundry using FrameView, Mangohud and MSI Afterburner

    

    usage: VideoFpsOverlay.py [-h] [-f Format] [-r Resolution] [-t Title] [-dr Range] [-lc Colour] [-bc Colour] [-tc Colour] [-tb bool] [-lw width] [-rb bool] [-rl bool] [-ymin min] [-ymax max] CSV Output
    
    Generates image sequences from FPS/FrameTime information captured by FPS recording software (only Nvidia FrameView support right now). Supported files: .csv and MSI Afterburner .hml
    
    positional arguments:
      CSV            The path to your CSV file
      Output         The path your image sequence will be saved
    
    optional arguments:
      -h, --help     show this help message and exit
      -f Format      Choose what format the csv is in [FV = FrameView, MS = MSI afterburner, MH = MangoHud] [default: FrameView]
      -r Resolution  Resolution of recording [720, 1080, 1440, 2160] [default: 1080]
      -t Title       Set the title of the graph
      -dr Range      Sets the X length of the graph in data points (example: 90 will have the graph show 90 data values at once) [default : 120]
      -lc Colour     Set the colour of the line [format: matplotlib colors] [default: red]
      -bc Colour     Set the colour of the axis and markers [format: matplotlib colors] [default: black]
      -tc Colour     Set the colour of the text [format: matplotlib colors] [default: black]
      -tb bool       Set background of the graph to transparent [default: True]
      -lw width      Set line width [default: 1]
      -rb bool       Disable box around line [default: False]
      -rl bool       Disable numbers around edge [default: False]
      -ymin min      Set min y axis range [default: 0]
      -ymax max      Set max y axis range [default: 120]

### Features

- PNG overlay export
- Frame time to FPS conversion
- Nvidia FrameView support
- MangoHud support
- MSI Afterburner support

### WIP

- Mangohud Support
- MSI Afterburner support
- Jpeg export
- Auto overlay on video

| WIP Support | Nvidia FrameView  | MangoHud  | MSI Afterburner  |
| ------------ | ------------ | ------------ | ------------ |
| FPS | Y  | Y  | Y  |
| Frame Time | N  |  N |  N |

#### pip requirements
- pandas
- matplotlib
