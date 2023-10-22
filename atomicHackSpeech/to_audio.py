import subprocess
import os
import sys

def convert_video_to_audio_ffmpeg(video_file, output_ext="wav"):
    """Преобразует видео в аудио напрямую с помощью команды `ffmpeg`
    с помощью модуля подпроцесса"""
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

if __name__ == "__main__":
    vf = sys.argv[1]
    convert_video_to_audio_ffmpeg(vf)