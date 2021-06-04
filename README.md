# Video FPS overlay
 Create FPS graph overlays like TRDrop and Digital Foundry using FrameView, Mangohud and MSI Afterburner

    



    usage: VideoFpsOverlay.py [-h] [-f Format] [-m Mode] [-r Resolution] [-t Title] [-dr Range] [-lc Colour] [-bc Colour] [-tc Colour] [-tb] [-lw width] [-rb] [-rl] [-cl] [-g] [-ymin min] [-ymax max] [-xinch size] [-yinch size] [-fl Location] [-ft amount] CSV Output
    
    Generates image sequences from FPS/FrameTime information captured by FPS recording software (only Nvidia FrameView support right now). Supported files: .csv and MSI Afterburner .hml
    
    positional arguments:
      CSV            The path to your CSV file
      Output         The path your image sequence will be saved
    
    optional arguments:
      -h, --help     show this help message and exit
      -f Format      Choose what format the csv is in [FV = FrameView, MS = MSI afterburner, MH = MangoHud] [default: FrameView]
      -m Mode        Choose what weather to render FPS or FrameTime graph [FPS = FPS, FT = FrameTime] [default: FPS]
      -r Resolution  Resolution of recording [720, 1080, 1440, 2160] [default: 1080]
      -t Title       Set the title of the graph
      -dr Range      Sets the X length of the graph in data points (example: 90 will have the graph show 90 data values at once) [default : 120]
      -lc Colour     Set the colour of the line [format: matplotlib colors] [default: red]
      -bc Colour     Set the colour of the axis and markers [format: matplotlib colors] [default: black]
      -tc Colour     Set the colour of the text [format: matplotlib colors] [default: black]
      -tb            Set background of the graph to transparent
      -lw width      Set line width [default: 1 for FPS | 4 for FT]
      -rb            Disable box around line
      -rl            Disable numbers around edge
      -cl            Add center line
      -g             Add grid
      -ymin min      Set min y axis range [default: 0]
      -ymax max      Set max y axis range [default: FPS 120 | FT 50]
      -xinch size    Set the width of the graph. This affects output resolution [Defaults: 16 for FPS | 9 for FT]
      -yinch size    Set the height of the graph. This affects output resolution [Defaults: 16 for FPS | 3 for FT]
      -fl Location   Set the location of the FPS numbers (left, right, both) [Default: right]
      -ft amount     Set the ammount of FRAME TIME values to show (3 or 4) [Defaults: 4]

### Features

- PNG overlay export
- Frame time to FPS conversion
- Nvidia FrameView support
- MangoHud support
- MSI Afterburner support

### WIP

- Jpeg export
- Auto overlay on video

| WIP Support | Nvidia FrameView  | MangoHud  | MSI Afterburner  |
| ------------ | ------------ | ------------ | ------------ |
| FPS | Y  | Y  | Y  |
| Frame Time | Y  |  Y |  Y |

#### pip requirements
- pandas
- matplotlib
