# Python Video Toolkit

A personal Python toolkit for video and audio processing built around FFmpeg.

The project provides reusable Python functions for common video, image, and audio operations without relying on high-level media libraries. FFmpeg is executed directly through Python's `subprocess`.

## Features

### Video Editing

- Resize video
- Crop video
- Trim video
- Remove a segment from video
- Merge multiple videos
- Split video into segments
- Change playback speed
- Reverse video
- Rotate video
- Loop video

### Image to Video

- Convert an image into a video
- Zoom animation
- Pan animation
- Fade in / fade out
- Slide animation
- Rotate image
- Ken Burns style effect

### Video to Image

- Extract a single frame
- Extract frames by interval
- Extract frames by FPS
- Generate thumbnails
- Extract scene frames
- Create contact sheets

### Video Conversion

- Convert video formats
- Change video codec
- Change FPS
- Remux video without re-encoding
- Convert video to GIF

### Video Effects

- Blur
- Sharpen
- Grayscale
- Brightness adjustment
- Contrast adjustment
- Saturation adjustment
- Vignette

### Audio

- Add audio to video
- Replace audio
- Remove audio
- Extract audio from video
- Change volume
- Trim audio
- Fade in / fade out
- Mix multiple audio tracks
- Concatenate audio files
- Normalize audio
- Loop audio

### Metadata

- Inspect video metadata using `ffprobe`

## Requirements

- Python 3.12+
- FFmpeg
- FFprobe

FFmpeg and FFprobe must be available in the system `PATH`.

Check the installation:

```bash
ffmpeg -version
ffprobe -version
