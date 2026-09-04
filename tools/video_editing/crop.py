from source.ffmpeg_runner import run_ffmpeg


def crop_video(
    input_path: str,
    output_path: str,
    width: int,
    height: int,
) -> None:
    run_ffmpeg([
        "-i", input_path,
        "-vf",
        f"scale={width}:{height}:force_original_aspect_ratio=increase,"
        f"crop={width}:{height}",
        "-an",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_path,
    ])
