from source.ffmpeg_runner import run_ffmpeg


def resize_video(input_path: str,
                 output_path: str,
                 width: int,
                 height: int
                 ) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-vf", f"scale={width}:{height}",
        output_path,
    ])
