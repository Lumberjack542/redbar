from scenedetect import open_video, SceneManager, split_video_ffmpeg, VideoManager
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg
import os
import scenedetect.video_splitter as video_splitter
import argparse


def split_video_into_scenes(video_path, output_folder, threshold=64.0):

    video =  VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(
         ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video, show_progress=True)
    scene_list = scene_manager.get_scene_list()
    
    os.makedirs(output_folder, exist_ok=True)
    video_splitter.split_video_ffmpeg([video_path], scene_list, output_folder + "/" + '$VIDEO_NAME-$SCENE_NUMBER' +".mp4", os.path.basename(output_folder) ,suppress_output=True)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("video_path", type=str)
    parser.add_argument("output_folder", type=str)

    args = parser.parse_args()

    split_video_into_scenes(args.video_path,  args.output_folder)