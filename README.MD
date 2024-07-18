# video-tools-lite

## Overview

**video-tools-lite** is a lightweight toolkit designed to streamline common video processing tasks. If you're dealing with video editing, this tool can save you time by handling tasks like cutting, merging, and batch renaming.

- **Dependencies**: Primarily relies on `ffmpeg`, so ensure it's installed and your environment variables are configured.

## Features

- Video Cutting
- Video Merging
- Batch File Renaming

## Usage

### Configuration

To simplify the process, all parameters are configured through a JSON file. Here's an example of what the configuration might look like:

```json
{
    "ffmpeg_path": "ffmpeg",
    "cutting": {
        "duration": 10,
        "output_path": "./output/"
    },
    "merge": {
        "extname": "mp4",
        "output_path": "./output2/"
    }
}
```

- `ffmpeg_path`: Path to the `ffmpeg` executable. Ensure it's either in your PATH or specify the full path.
- `cutting`: Configuration for video cutting
  - `duration`: Duration of each cut, in seconds.
  - `output_path`: Directory where the output files will be saved.
- `merge`: Configuration for video merging
  - `extname`: File extension of the input files.
  - `output_path`: Directory where the merged video will be saved.

### Installation

Clone the repository and navigate into the project directory:

```powershell
git clone https://github.com/zoujiejun/video-tools-lite.git
cd video-tools-lite
```

### Video Cutting

To cut a video, run the following command:

```powershell
python3 .\video_cutting.py .\config.json .\input\demo.mp4
```

- **Arguments**:
  - `config.json`: Path to the configuration file.
  - `demo.mp4`: Path to the input video file.

### Video Merging

To merge videos, execute:

```powershell
python3 .\video_merge.py .\config.json .\output\demo\
```

- **Arguments**:
  - `config.json`: Path to the configuration file.
  - `demo/`: Directory containing the video files to merge.

### Batch File Renaming

To rename files in a directory, use:

```powershell
python3 .\batch_rename.py .\output\demo\
```

- **Argument**:
  - `demo/`: Directory containing the files to rename.

## License

This project is licensed under the MIT License.

