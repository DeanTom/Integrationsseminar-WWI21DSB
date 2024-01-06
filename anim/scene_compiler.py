import os
import subprocess

# helping function for concat_video
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



def create_video() -> None:
    try:
        # get all pyscripts from the anim folder
        files = os.listdir(os.path.join(os.path.dirname(__file__), "..", "anim"))
        files = [file for file in files if file.endswith(".py")]
        
        # compile all the files
        for file in files:
            subprocess.run(["manim", "-ql", file, "-a"], cwd=os.path.join(os.path.dirname(__file__), "..", "anim"))

    except Exception as e:
        print(f"An error occurred: {e}")
    
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
        subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", tmp_compile_file, "-c", "copy", "output.mp4"], cwd=os.path.join(os.path.dirname(__file__), "..", "anim"))
        os.remove(tmp_compile_file)
    except Exception as e:
        print(f"An error occurred: {e}") 

create_video()
concat_videos()
