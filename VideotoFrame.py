import cv2
import os

def extract_frames(input_video_path, output_frames_folder, start_time, end_time):
    # Open the video file
    video_capture = cv2.VideoCapture(input_video_path)

    # Get frames per second (fps) and total number of frames
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate start and end frame indices based on the provided time range
    start_frame = int(start_time * fps)
    end_frame = min(int(end_time * fps), total_frames - 1)

    # Create output folder if it doesn't exist
    os.makedirs(output_frames_folder, exist_ok=True)

    # Read and save frames within the specified time range
    frame_count = 0
    while frame_count <= end_frame:
        success, frame = video_capture.read()
        if not success:
            break

        if start_frame <= frame_count <= end_frame:
            frame_filename = os.path.join(output_frames_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the video capture object
    video_capture.release()

# Example usage
input_video_path = 'C:/Users/sonir/OneDrive/Desktop/Research Work/BankRobbery/Train/Fight/311.mp4'
output_frames_folder = 'C:/Users/sonir/OneDrive/Desktop/Research Work/Frames'
start_time_seconds = 10 #start time in seconds
end_time_seconds = 30  # End time in seconds

extract_frames(input_video_path, output_frames_folder, start_time_seconds, end_time_seconds)
