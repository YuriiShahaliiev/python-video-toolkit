from source.ffmpeg_runner import run_ffmpeg


def resize_video(input_path, output_path, width, height):
    run_ffmpeg([
        "-i", input_path,
        "-vf", f"scale={width}:{height}",
        output_path,
    ])
