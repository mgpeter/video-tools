from moviepy.editor import VideoFileClip
import argparse

def crop_video_to_aspect_ratio(input_file_path, output_file_path, target_aspect_ratio=4/5):
    # Load the video file
    video = VideoFileClip(input_file_path)
    
    # Original dimensions
    original_width = video.size[0]
    original_height = video.size[1]
    original_aspect_ratio = original_width / original_height
    
    # Determine dimensions of the new crop
    if original_aspect_ratio > target_aspect_ratio:
        # The video is wider than the target aspect ratio, need to crop width
        new_width = int(original_height * target_aspect_ratio)
        new_height = original_height
    else:
        # The video is taller than the target aspect ratio, need to crop height
        new_width = original_width
        new_height = int(original_width / target_aspect_ratio)
    
    # Calculate crop dimensions
    crop_x_center = original_width / 2
    crop_y_center = original_height / 2
    
    x1 = crop_x_center - new_width / 2
    y1 = crop_y_center - new_height / 2
    
    # Perform the crop
    cropped_video = video.crop(x1=x1, y1=y1, width=new_width, height=new_height)
    
    # Write the output file
    cropped_video.write_videofile(output_file_path, codec="libx264", audio_codec="aac")
    
    # Release resources
    video.close()

def main():
    parser = argparse.ArgumentParser(description="Crop a video to a 4:5 aspect ratio focusing on the central part.")
    parser.add_argument("--input-file-path", required=True, help="Path to the input video file.")
    parser.add_argument("--output-file-path", required=True, help="Path to the output cropped video file.")
    
    args = parser.parse_args()
    
    crop_video_to_aspect_ratio(args.input_file_path, args.output_file_path)

if __name__ == "__main__":
    main()
