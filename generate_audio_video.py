from gtts import gTTS
from moviepy.editor import TextClip, CompositeVideoClip
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv("YOUR_API_KEY")

# Generate Audio
def generate_audio(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    print(f"Audio saved as {filename}")

# Generate Video
def generate_video(text, audio_file, video_file="output.mp4"):
    # Create a text clip
    text_clip = TextClip(text, fontsize=70, color='white', size=(1280, 720))
    text_clip = text_clip.set_duration(10)  # 10 seconds

    # Add audio to the video
    video = CompositeVideoClip([text_clip])
    video.write_videofile(video_file, fps=24, codec="libx264", audio=audio_file)
    print(f"Video saved as {video_file}")

# Example Usage
if __name__ == "__main__":
    text = "Hello, this is a generated audio and video example."
    audio_file = "output.mp3"
    video_file = "output.mp4"

    generate_audio(text, audio_file)
    generate_video(text, audio_file, video_file)