import argparse
from moviepy.editor import VideoFileClip
import os

def split_video_into_chunks(input_file_path, output_dir, chunk_length=15):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load the video file
    video = VideoFileClip(input_file_path)
    
    # Calculate the number of chunks
    num_chunks = int(video.duration // chunk_length) + (1 if video.duration % chunk_length else 0)
    
    # Split and save each chunk
    for i in range(num_chunks):
        start_time = i * chunk_length
        end_time = min((i + 1) * chunk_length, video.duration)
        chunk = video.subclip(start_time, end_time)
        chunk_file_path = os.path.join(output_dir, f"chunk_{i+1:03d}.mp4")
        chunk.write_videofile(chunk_file_path, codec="libx264", audio_codec="aac")
        
        print(f"Chunk {i+1} saved: {chunk_file_path}")
    
    # Release resources
    video.close()

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Split an MP4 file into chunks of up to 15 seconds each.")
    
    # Add the arguments as optional
    parser.add_argument("--input-file-path", required=True, help="Path to the input MP4 file.")
    parser.add_argument("--output-dir", required=True, help="Directory where the output chunks will be saved.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Execute the function with the provided arguments
    split_video_into_chunks(args.input_file_path, args.output_dir)

if __name__ == "__main__":
    main()
