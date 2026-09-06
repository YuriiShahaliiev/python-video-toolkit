from source.ffmpeg_runner import run_ffmpeg


def convert_video_to_gif(
    input_path: str,
    output_path: str,
    fps: int = 15,
    width: int = 480,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-vf", f"fps={fps},scale={width}:-1:flags=lanczos",
        output_path,
    ])
