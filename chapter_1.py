import cv2
import os
import argparse


def extract_frames(video_path, num_frames1, num_frames2, output_folder):

    cap = cv2.VideoCapture(video_path)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(width, 'x', height)  
    
     
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    
    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break 

        frame_count += 1
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        if num_frames2 >= frame_count >= num_frames1:
            cv2.imwrite(frame_filename, frame)
        
   
    print(f"{frame_count} frames extracted and saved to {output_folder}")

    
    cap.release()
    cv2.destroyAllWindows()
   



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    parser.add_argument("num_frames1", type=int, help="Number 1 of frames to extract.")
    parser.add_argument("num_frames2", type=int, help="Number 2 of frames to extract.")
    parser.add_argument("output_folder", type=str, help="Path to save the extracted frames.")

    args = parser.parse_args()

    extract_frames(args.video_path, args.num_frames1, args.num_frames2,  args.output_folder)