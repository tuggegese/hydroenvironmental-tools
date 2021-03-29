from moviepy.editor import *
import os

def mov2gif(INPUT_FILENAME,OUTPUT_FILENAME):
    clip = (VideoFileClip(INPUT_FILENAME)
            .subclip((0,1),(0,4))   # start and end time in s
            .resize(0.3))           # ratio quality to original
    clip.write_gif(OUTPUT_FILENAME, fps=10, fuzz=10)

def get_filepaths(DIRNAME):
    file_paths = []
    for root, directories, files in os.walk(DIRNAME):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def run(DIRNAME):
    for dirs in os.walk(DIRNAME):
        file_path = get_filepaths(dirs[0])
        for file in file_path:
            if file[-4:] == '.MOV':
                INPUT_FILENAME = file
                OUTPUT_FILENAME = file[:-4]+'00.gif'
                mov2gif(INPUT_FILENAME,OUTPUT_FILENAME)
    

# DIRNAME = r'C:\Users\skiller\Documents\PROJECTS\2021_mov2gif'
# run(DIRNAME)