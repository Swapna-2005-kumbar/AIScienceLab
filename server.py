from flask import Flask, request, jsonify, send_from_directory
from gtts import gTTS
from moviepy.editor import TextClip, CompositeVideoClip
import os

app = Flask(__name__)

# ✅ Home route (MUST be outside)
@app.route("/")
def home():
    return "AI Science Lab Server is running 🚀"


# 🎧 Generate Audio
@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.get_json()
    text = data.get('text', 'Default text')

    audio_file = 'output.mp3'
    tts = gTTS(text)
    tts.save(audio_file)

    return jsonify({'audioUrl': f'/audio/{audio_file}'})


# 🎬 Generate Video
@app.route('/generate-video', methods=['POST'])
def generate_video():
    data = request.get_json()
    text = data.get('text', 'Default text')

    audio_file = 'output.mp3'
    video_file = 'output.mp4'

    # Generate audio
    tts = gTTS(text)
    tts.save(audio_file)

    # Generate video
    text_clip = TextClip(text, fontsize=70, color='white', size=(1280, 720))
    text_clip = text_clip.set_duration(10)

    video = CompositeVideoClip([text_clip])
    video.write_videofile(video_file, fps=24, codec="libx264", audio=audio_file)

    return jsonify({'videoUrl': f'/video/{video_file}'})


# 📁 Serve audio files
@app.route('/audio/<filename>')
def get_audio(filename):
    return send_from_directory('.', filename)


# 📁 Serve video files
@app.route('/video/<filename>')
def get_video(filename):
    return send_from_directory('.', filename)


if __name__ == '__main__':
    app.run(debug=True)