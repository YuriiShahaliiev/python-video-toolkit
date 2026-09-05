from source.ffmpeg_runner import run_ffmpeg


def convert_video(
    input_path: str,
    output_path: str,
    video_codec: str = "libx264",
    audio_codec: str | None = None,
    fps: int | None = None,
) -> None:
    command = [
        "-i", input_path,
    ]

    if video_codec:
        command.extend([
            "-c:v", video_codec,
        ])

    if audio_codec:
        command.extend([
            "-c:a", audio_codec,
        ])
    else:
        command.extend([
            "-an",
        ])

    if fps is not None:
        if fps <= 0:
            raise ValueError("fps must be greater than 0")

        command.extend([
            "-r", str(fps),
        ])

    command.extend([
        "-pix_fmt", "yuv420p",
        output_path,
    ])

    run_ffmpeg(command)
