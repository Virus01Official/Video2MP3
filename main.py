from moviepy.editor import VideoFileClip

# Replace 'path_to_video' with the path to your video file
video_path = 'video.mp4'
# Replace 'output_audio' with the desired output MP3 file path
audio_output = 'output_audio.mp3'

video_clip = VideoFileClip(video_path)
video_clip.audio.write_audiofile(audio_output)
