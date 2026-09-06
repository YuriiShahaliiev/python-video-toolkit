from source.ffmpeg_runner import run_ffmpeg


def add_audio_to_video(
    video_path: str,
    audio_path: str,
    output_path: str,
) -> None:
    run_ffmpeg([
        "-i", video_path,
        "-i", audio_path,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output_path,
    ])
