from moviepy.editor import *
import os

def mov2gif(INPUT_MOV_FILENAME,OUTPUT_GIF_FILENAME):
    clip = (VideoFileClip(INPUT_MOV_FILENAME)
            .subclip((0,1),(0,4))
            .resize(0.3))
    clip.write_gif(OUTPUT_GIF_FILENAME, fps=10, fuzz=10)

def get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


# directory = r'C:\Users\skiller\Documents\PROJECTS\2021_mov2gif'
directory = r'M:\IWB\Projekte\2020_Purbach_Judenburg_364.00_D153\Bilder\Auftragnehmer\20210325_Ausgebaute_Mauern\Lastfall_D4'
for dirs in os.walk(directory):
    file_path = get_filepaths(dirs[0])
    for file in file_path:
        if file[-4:] == '.MOV':
            INPUT_FILENAME = file
            OUTPUT_FILENAME = file[:-4]+'00.gif'
            mov2gif(INPUT_FILENAME,OUTPUT_FILENAME)