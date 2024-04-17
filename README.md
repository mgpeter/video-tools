# Peter's Instagram Video Tools

A set of CLI tools useful to quickly split and crop clips for use with Instagram stories.

## Installation

Make sure you install necessary libraries:

```
pip install moviepy
pip install argparse
```

For ease of use, included *.bat files for Windows users so far. Add the video-tools directory to your PATH.

## Usage

### Split video into 15-second chunks

```
./split-video --input-file-path path-to-the-file-to-split.mp4 --output-dir ./directory/to/put/divided/files/in/
```

### Crop video into 4:5 aspect ratio focusing on the centre

```
./crop-video --input-file-path ./path-to-the-file-to-split.mp4 --output-file-path ./path-where-to-save-the-cropped-output.mp4
```

### 


## Acknowledgements and notes

MIT License
Done solely to help with my side project at https://shop.usualexpat.com and https://www.instagram.com/usualexpat.apparel
Feel free to use, no prolonged support can be expected ;-)
