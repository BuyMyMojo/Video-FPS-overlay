#!/usr/bin/env python3

# importing the required modules
import argparse as argp
import gc
from time import time

from matplotlib import pyplot as plt
from pandas import read_csv


def fps_graph_fv(csv_path, transparent_background, resolution, title, preset_frame_range, colour, back_colour,
                 out_folder, line_width, remove_box, remove_numbers, ymin, ymax, text_colour, xsize, ysize, center_line,
                 grid, fps_location, mode):
    # reading CSV file
    fps_data = read_csv(csv_path)

    # grab all frame times
    full_frametimes = fps_data['MsBetweenPresents'].tolist()
    times = fps_data['TimeInSeconds'].tolist()
    full_framerate = [1000 / x if x > 0 else x == 0 for x in full_frametimes]
    video_frames = len(full_frametimes)
    del full_frametimes
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    # for j in range(preset_frame_range):
    #     # full_frametimes.insert(0, 0) # to add back in later when implementing frametime graph
    #     full_framerate.insert(0, 0)
    #     times.insert(0, int(times[0])-4)

    # setup graph
    fig, ax = plt.subplots()
    transparency = 1.0
    if transparent_background is True:
        transparency = 0.0

    fig.patch.set_alpha(transparency)

    if resolution == 720:
        dpi = 45
    elif resolution == 1080:
        dpi = 120
    elif resolution == 1440:
        dpi = 160
    elif resolution == 2160:
        dpi = 240

    if xsize is None:
        xsize = 16

    if ysize is None:
        ysize = 4

    # run graph
    graph(video_frames, preset_frame_range, ax, full_framerate, colour, line_width, ymin, ymax, fig, dpi, title,
          text_colour, back_colour, remove_box, remove_numbers, out_folder, transparent_background, xsize, ysize,
          center_line, grid, fps_location, mode, times)


def ft_graph_fv(csv_path, transparent_background, resolution, title, preset_frame_range, ymin, ymax, colour,
                back_colour, out_folder, line_width, remove_box, remove_numbers, text_colour, xsize, ysize, center_line,
                grid, fps_location, mode, ticks):
    # reading CSV file
    fps_data = read_csv(csv_path)

    # grab all frame times
    full_trametimes = fps_data['MsBetweenPresents'].tolist()
    times = fps_data['TimeInSeconds'].tolist()
    video_frames = len(full_trametimes)

    del fps_data
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(int(preset_frame_range)):
        # full_trametimes.insert(0, 0) # to add back in later when implementing frametime graph
        full_trametimes.insert(0, 0)

    # double up data for square graph?
    # SquareFrames = [val for val in full_trametimes for _ in (0, 1)]
    # del full_trametimes

    # setup graph
    fig, ax = plt.subplots()
    transparency = 1.0
    if transparent_background is True:
        transparency = 0.0

    fig.patch.set_alpha(transparency)

    if resolution == 720:
        dpi = 45
    elif resolution == 1080:
        dpi = 120
    elif resolution == 1440:
        dpi = 160
    elif resolution == 2160:
        dpi = 240

    if xsize is None:
        xsize = 9

    if ysize is None:
        ysize = 3

    if ymax is None:
        ymax = 50

    # run graph
    graph(video_frames, preset_frame_range, ax, full_trametimes, colour, line_width, ymin, ymax, fig, dpi, title,
          text_colour, back_colour, remove_box, remove_numbers, out_folder, transparent_background, xsize, ysize,
          center_line, grid, fps_location, mode, times, ticks)


def ft_graph_ms(csv_path, transparent_background, resolution, title, preset_frame_range, ymin, ymax, colour,
                back_colour, out_folder, line_width, remove_box, remove_numbers, text_colour, xsize, ysize, center_line,
                grid, fps_location, mode, ticks):
    # reading CSV file
    fps_data = read_csv(csv_path, skiprows=2, usecols=[27], squeeze=True)

    # grab all frame times
    full_frametimes = fps_data.tolist()
    full_frametimes = full_frametimes[31:]
    video_frames = len(full_frametimes)

    del fps_data
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(int(preset_frame_range)):
        # full_frametimes.insert(0, 0) # to add back in later when implementing frametime graph
        full_frametimes.insert(0, 0)

    # setup graph
    fig, ax = plt.subplots()
    transparency = 1.0
    if transparent_background is True:
        transparency = 0.0

    fig.patch.set_alpha(transparency)

    if resolution == 720:
        dpi = 45
    elif resolution == 1080:
        dpi = 120
    elif resolution == 1440:
        dpi = 160
    elif resolution == 2160:
        dpi = 240

    if xsize is None:
        xsize = 9

    if ysize is None:
        ysize = 3

    if ymax is None:
        ymax = 50

    # run graph
    graph(video_frames, preset_frame_range, ax, full_frametimes, colour, line_width, ymin, ymax, fig, dpi, title,
          text_colour, back_colour, remove_box, remove_numbers, out_folder, transparent_background, xsize, ysize,
          center_line, grid, fps_location, mode, ticks)


def ft_graph_mh(csv_path, transparent_background, resolution, title, preset_frame_range, ymin, ymax, colour,
                back_colour, out_folder, line_width, remove_box, remove_numbers, text_colour, xsize, ysize, center_line,
                grid, fps_location, mode, ticks):
    # reading CSV file
    fps_data = read_csv(csv_path, skiprows=2, usecols=[1], squeeze=True)

    # grab all frame times
    full_frametimes = fps_data.tolist()
    video_frames = len(full_frametimes)
    full_frametimes = [x / 1000 for x in full_frametimes]

    del fps_data
    del full_frametimes
    gc.collect()
    # add blank values at the start for the animation
    for j in range(int(preset_frame_range)):
        full_frametimes.insert(0, 0)

    # setup graph
    fig, ax = plt.subplots()
    transparency = 1.0
    if transparent_background is True:
        transparency = 0.0

    fig.patch.set_alpha(transparency)

    if resolution == 720:
        dpi = 45
    elif resolution == 1080:
        dpi = 120
    elif resolution == 1440:
        dpi = 160
    elif resolution == 2160:
        dpi = 240

    if xsize is None:
        xsize = 9

    if ysize is None:
        ysize = 3

    if ymax is None:
        ymax = 50

    # run graph
    graph(video_frames, preset_frame_range, ax, full_frametimes, colour, line_width, ymin, ymax, fig, dpi, title,
          text_colour, back_colour, remove_box, remove_numbers, out_folder, transparent_background, xsize, ysize,
          center_line, grid, fps_location, mode, ticks)


def fps_graph_ms(csv_path, transparent_background, resolution, title, preset_frame_range, colour, back_colour,
                 out_folder, line_width, remove_box, remove_numbers, ymin, ymax, text_colour, xsize, ysize, center_line,
                 grid, fps_location, mode):
    # reading CSV file
    fps_data = read_csv(csv_path, skiprows=2, usecols=[26], squeeze=True)

    # grab all frame times
    full_framerate = fps_data.tolist()
    full_framerate = full_framerate[31:]
    video_frames = len(full_framerate)
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(preset_frame_range):
        # FullFrameTimes.insert(0, 0) # to add back in later when implementing frametime graph
        full_framerate.insert(0, 0)

    # setup graph
    fig, ax = plt.subplots()
    transparency = 1.0
    if transparent_background is True:
        transparency = 0.0

    fig.patch.set_alpha(transparency)

    if resolution == 720:
        dpi = 45
    elif resolution == 1080:
        dpi = 120
    elif resolution == 1440:
        dpi = 160
    elif resolution == 2160:
        dpi = 240

    if xsize is None:
        xsize = 16

    if ysize is None:
        ysize = 4

    # run graph
    graph(video_frames, preset_frame_range, ax, full_framerate, colour, line_width, ymin, ymax, fig, dpi, title,
          text_colour, back_colour, remove_box, remove_numbers, out_folder, transparent_background, xsize, ysize,
          center_line, grid, fps_location, mode)


def fps_graph_mh(csv_path, transparent_background, resolution, title, preset_frame_range, colour, back_colour,
                 out_folder, line_width, remove_box, remove_numbers, ymin, ymax, text_colour, xsize, ysize, center_line,
                 grid, fps_location, mode):
    # reading CSV file
    fps_data = read_csv(csv_path, skiprows=2, usecols=[0], squeeze=True)

    # grab all frame times
    full_framerate = fps_data.tolist()
    video_frames = len(full_framerate)
    gc.collect()
    # add Frame Range -1 blank values at the start for the animation
    for j in range(preset_frame_range):
        # FullFrameTimes.insert(0, 0) # to add back in later when implamenting frametime graph
        full_framerate.insert(0, 0)

    # setup graph
    fig, ax = plt.subplots()
    transparency = 1.0
    if transparent_background is True:
        transparency = 0.0

    fig.patch.set_alpha(transparency)

    if resolution == 720:
        dpi = 45
    elif resolution == 1080:
        dpi = 120
    elif resolution == 1440:
        dpi = 160
    elif resolution == 2160:
        dpi = 240

    if xsize is None:
        xsize = 16

    if ysize is None:
        ysize = 4

    # run graph
    graph(video_frames, preset_frame_range, ax, full_framerate, colour, line_width, ymin, ymax, fig, dpi, title,
          text_colour, back_colour, remove_box, remove_numbers, out_folder, transparent_background, xsize, ysize,
          center_line, grid, fps_location, mode)


def graph(video_frames, preset_frame_range, ax, data, colour, line_width, ymin, ymax, fig, dpi, title, text_colour,
          back_colour, remove_box, remove_numbers, out_folder, transparent_background, xsize, ysize, center_line, grid,
          fps_location, mode, times, ticks=4):
    # generate graph frames
    start = time()
    for i in range(video_frames):
        trimrange = preset_frame_range

        print("Range for time = [" + str(i) + ":" + str(trimrange + i) + "]")

        xaxis = []
        xaxis = xaxis_times(i, mode, times, trimrange, xaxis)

        plot_mode(ax, colour, data, i, line_width, mode, trimrange, xaxis)

        axis_limits(ax, i, times, trimrange, ymax, ymin)
        fig.dpi = dpi
        fig.set_size_inches(xsize, ysize)
        ax.set_title(title, {'color': text_colour})
        ax.xaxis.label.set_color(text_colour)
        ax.yaxis.label.set_color(text_colour)
        ax.tick_params(axis='both', colors=back_colour, bottom=remove_box, top=remove_box, left=remove_box,
                       right=remove_box, labelleft=remove_numbers, labelbottom=False)
        set_yticks(mode, ticks, ymax)
        set_fps_location(ax, fps_location)
        set_visible(ax, remove_box)
        set_color(ax, back_colour)
        if center_line is True:
            ax.axvline(x=find_middle(times, i, trimrange + i), ymin=0, ymax=1, color=back_colour)
        if grid is True:
            ax.grid(b=None, which='major', axis='y')

        # save as png
        plt.xticks(times[i:trimrange + i])
        save_graph(ax, i, out_folder, transparent_background)

        print('Processed frame ' + str(i + 1) + ' of ' + str(video_frames) + " " + str((i + 1) * 100 / video_frames)[
                                                                                   0:5] + "%" + ' FPS graph')

    complete_graph(start)


def save_graph(ax, i, out_folder, transparent_background):
    plt.savefig(out_folder + "Frame_" + str(i + 1) + '.png', transparent=transparent_background, backend='Agg')
    ax.cla()


def complete_graph(start):
    print("Completed!")
    time_taken = time() - start
    time_taken = str(time_taken)
    print(f'Time taken: {time_taken[0:5]}')


def xaxis_times(i, mode, times, trimrange, xaxis):
    if mode == "FPS":
        xaxis = times[i:trimrange + i]
    elif mode == "FT":
        xaxis = times[i:trimrange + i]
    return xaxis


def plot_mode(ax, colour, data, i, line_width, mode, trimrange, xaxis):
    if mode == "FPS":
        lines = ax.plot(xaxis, data[i:trimrange + i], color=colour, linewidth=line_width)
    elif mode == "FT":
        lines = ax.plot(xaxis, data[i:trimrange + i], color=colour, linewidth=line_width, drawstyle='steps-pre')


def axis_limits(ax, i, times, trimrange, ymax, ymin):
    ax.set_ylim(ymin, ymax)
    ax.set_xlim(times[i], times[trimrange + i])


def set_color(ax, back_colour):
    ax.spines['left'].set_color(back_colour)
    ax.spines['right'].set_color(back_colour)
    ax.spines['top'].set_color(back_colour)
    ax.spines['bottom'].set_color(back_colour)


def set_visible(ax, remove_box):
    ax.spines['left'].set_visible(remove_box)
    ax.spines['right'].set_visible(remove_box)
    ax.spines['bottom'].set_visible(remove_box)
    ax.spines['top'].set_visible(remove_box)


def set_fps_location(ax, fps_location):
    if fps_location == "left":
        ax.tick_params(axis='y', labelleft=True, labelright=False)
    elif fps_location == "right":
        ax.tick_params(axis='y', labelleft=False, labelright=True)
    elif fps_location == "both":
        ax.tick_params(axis='y', labelleft=True, labelright=True)


def set_yticks(mode, ticks, ymax):
    if mode == "FT":
        if ticks == 3:
            plt.yticks([0, ymax / 2, ymax])
        elif ticks == 4:
            plt.yticks([0, ymax / 3, ymax / 3 * 2, ymax])


def find_middle(times, i, end_range):
    ttte = times[i:end_range]
    tttl = len(ttte)

    sss = sum(times[i:end_range])
    return int(int(sss) / int(tttl))


def wip_error():
    print("This feature has been put in WIP, check back in a future version")
    exit()


def main(args):
    # settings
    csv_path = args.CSV
    mode = args.m
    resolution = args.r
    preset_frame_range = args.dr
    title = args.t
    if args.Output[-1] == "\\":
        out_folder = args.Output
    elif args.Output[-1] == "/":
        out_folder = args.Output
    else:
        print("Make sure the output path ends in either a \\ or a /")
        exit()
    colour = args.lc
    back_colour = args.bc
    transparent_background = args.tb
    if args.lw is not None:
        line_width = args.lw
    else:
        if mode == "FPS":
            line_width = 1
        elif mode == "FT":
            line_width = 2
    remove_box = not args.rb
    remove_numbers = not args.rl
    ymin = args.ymin
    ymax = args.ymax
    text_colour = args.tc
    xsize = args.xinch
    ysize = args.yinch
    center_line = args.cl
    grid = args.g
    fps_location = args.fl
    ticks = args.ft

    if mode == "FPS":
        if args.f == "FV":
            fps_graph_fv(csv_path, transparent_background, resolution, title, preset_frame_range, colour, back_colour,
                         out_folder, line_width, remove_box, remove_numbers, ymin, ymax, text_colour, xsize, ysize,
                         center_line, grid, fps_location, mode, )
        elif args.f == "MS":
            # FpsGraphMS(csv_path, transparent_background, resolution, title, preset_frame_range, colour, back_colour, out_folder, line_width, remove_box, remove_numbers, ymin, ymax, text_colour, xsize, ysize, center_line, grid, fps_location, mode)
            wip_error()
        elif args.f == "MH":
            # FpsGraphMH(csv_path, transparent_background, resolution, title, preset_frame_range, colour, back_colour, out_folder, line_width, remove_box, remove_numbers, ymin, ymax, text_colour, xsize, ysize, center_line, grid, fps_location, mode)
            wip_error()
        else:
            return print("Make sure you have the right format set")
    elif mode == "FT":
        if args.f == "FV":
            ft_graph_fv(csv_path, transparent_background, resolution, title, preset_frame_range, ymin, ymax, colour,
                        back_colour, out_folder, line_width, remove_box, remove_numbers, text_colour, xsize, ysize,
                        center_line, grid, fps_location, mode, ticks)
        elif args.f == "MS":
            # FTGraphMS(csv_path, transparent_background, resolution, title, preset_frame_range, ymin, ymax, colour, back_colour, out_folder, line_width, remove_box, remove_numbers, text_colour, xsize, ysize, center_line, grid, fps_location, mode, ticks)
            wip_error()
        elif args.f == "MH":
            # FTGraphMH(csv_path, transparent_background, resolution, title, preset_frame_range, ymin, ymax, colour, back_colour, out_folder, line_width, remove_box, remove_numbers, text_colour, xsize, ysize, center_line, grid, fps_location, mode, ticks)
            wip_error()
        else:
            return print("Make sure you have the right format set")
    else:
        print("Make sure you have mode set correctly")
        return ()


# setup argparse
parser = argp.ArgumentParser(description='''Generates image sequences from FPS/FrameTime information captured by FPS recording software (only Nvidia FrameView support right now).
Supported files: .csv and MSI Afterburner .hml''', allow_abbrev=False)

# add arguments
parser.add_argument('CSV', metavar='CSV', type=str, help='The path to your CSV file')
parser.add_argument('-f', metavar='Format', type=str,
                    help='Choose what format the csv is in [FV = FrameView, MS = MSI afterburner, MH = MangoHud] [default: FrameView]',
                    default="FV")
parser.add_argument('-m', metavar='Mode', type=str,
                    help='Choose what weather to render FPS or FrameTime graph [FPS = FPS, FT = FrameTime] [default: FPS]',
                    default="FPS")
parser.add_argument('Output', metavar='Output', type=str, help='The path your image sequence will be saved')
parser.add_argument('-r', metavar='resolution', type=int,
                    help='resolution of recording [720, 1080, 1440, 2160] [default: 1080]', default=1440)
parser.add_argument('-t', metavar='title', type=str, help='Set the title of the graph', default=" ")
parser.add_argument('-dr', metavar='Range', type=int,
                    help='Sets the X length of the graph in seconds [default: FPS 120 | FT 60]', default=120)
parser.add_argument('-lc', metavar='Colour', type=str,
                    help='Set the colour of the line [format: matplotlib colors] [default: red]', default="r")
parser.add_argument('-bc', metavar='Colour', type=str,
                    help='Set the colour of the axis and markers [format: matplotlib colors] [default: black]',
                    default="white")
parser.add_argument('-tc', metavar='Colour', type=str,
                    help='Set the colour of the text [format: matplotlib colors] [default: black]', default="white")
parser.add_argument('-tb', action='store_true', help='Set background of the graph to transparent')
parser.add_argument('-lw', metavar='width', type=int, help='Set line width [default: 1 for FPS | 4 for FT]',
                    default=None)
parser.add_argument('-rb', action='store_true', help='Disable box around line')
parser.add_argument('-rl', action='store_true', help='Disable numbers around edge')
parser.add_argument('-cl', action='store_true', help='Add center line')
parser.add_argument('-g', action='store_true', help='Add grid')
parser.add_argument('-ymin', metavar='min', type=int, help='Set min y axis range [default: 0]', default=0)
parser.add_argument('-ymax', metavar='max', type=int, help='Set max y axis range [default: FPS 120 | FT 50]',
                    default=250)
parser.add_argument('-xinch', metavar='size', type=int,
                    help='Set the width of the graph. This affects output resolution [Defaults: 16 for FPS | 9 for FT]',
                    default=None)
parser.add_argument('-yinch', metavar='size', type=int,
                    help='Set the height of the graph. This affects output resolution [Defaults: 16 for FPS | 3 for FT]',
                    default=None)
parser.add_argument('-fl', metavar='Location', type=str,
                    help='Set the location of the FPS numbers (left, right, both) [Default: right]', default="right")
parser.add_argument('-ft', metavar='amount', type=int,
                    help='Set the ammount of FRAME TIME values to show (3 or 4) [Defaults: 4]', default=4)

main(parser.parse_args())
