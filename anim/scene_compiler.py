# Done by Christopher Wolf, WWI21DSB

import os
import subprocess
import shutil

def create_video(quality: str) -> None:
    quality_flag = ""
    if quality == "low":
        quality_flag = "-ql"
    elif quality == "medium":
        quality_flag = "-qm"
    elif quality == "high":
        quality_flag = "-qh"
    elif quality == "ultra":
        quality_flag = "-qk"
    else: 
        print("Invalid quality flag. Using default quality flag.")
        quality_flag = "-ql"
    try:
        # get all pyscripts from the anim folder
        files = os.listdir(os.path.join(os.path.dirname(__file__), "..", "anim"))
        files = [file for file in files if file.endswith(".py")]
        
        # compile all the files
        for file in files:
            subprocess.run(["manim", quality_flag, file, "-a"], cwd=os.path.join(os.path.dirname(__file__), "..", "anim"))

    except Exception as e:
        print(f"An error occurred: {e}")

def get_all_videos(): 
    cwd = os.getcwd()
    anim_video_folder = os.path.join(cwd, "anim", "media", "videos")
    mp4_files = []

    for root, dirs, files in os.walk(anim_video_folder):
        for file in files:
            if file.endswith(".mp4"):
                # cut the path of file until anim
                file = os.path.join(root, file).split("anim")[1]
                if "partial_movie_files" not in file:
                    mp4_files.append(file)
    return mp4_files
    
# concatenate the videos 
def concat_videos () -> None:
    try:
        files = get_all_videos()
        anim_folder = os.path.join(os.path.dirname(__file__), "..", "anim")
        tmp_compile_file = os.path.join(anim_folder, "tmp.txt")

        with open(tmp_compile_file, "w") as f:
            for file in files:
                f.write(f"file '{file}'\n")
        # run the ffmpeg command
                
        # if anim/output.mp4 exists, delete it
        if os.path.exists(os.path.join(anim_folder, "output.mp4")):
            os.remove(os.path.join(anim_folder, "output.mp4"))

        subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", tmp_compile_file, "-c", "copy", "output.mp4"], cwd=os.path.join(os.path.dirname(__file__), "..", "anim"))
        os.remove(tmp_compile_file)
    except Exception as e:
        print(f"An error occurred: {e}") 

def play_video() -> None:
    video_height = 800
    video_width = 1200
    try:
        subprocess.run(["ffplay", "-x", str(video_width), "-y", str(video_height), "output.mp4"], cwd=os.path.join(os.path.dirname(__file__), "..", "anim"))
    except Exception as e:
        print(f"An error occurred: {e}")


def check_media_folder() -> None:
        if os.path.exists(os.path.join(os.path.dirname(__file__), "..", "anim", "media")):
            shutil.rmtree(os.path.join(os.path.dirname(__file__), "..", "anim", "media"))

def build_video(quality: str) -> None:
    try:
        create_video(quality=quality)
        concat_videos()
    except Exception as e:
        print(f"An error occurred: {e}")

create_video("high")
concat_videos()
play_video()
