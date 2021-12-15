from pytube import YouTube
from flask import Flask, render_template, redirect, url_for, request, send_from_directory, send_file
import os
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nasigorengkesukaansaya'

song_title=  []

@app.route('/')
def home():
    list_file = os.listdir('static/video')
    if list_file != []: 
        for i in list_file:
            os.remove(f"static/video/{i}")
    return render_template('index.html')

@app.route('/take_link', methods=['GET', 'POST'])
def take_link():
    link = request.form.get('link')
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').first().download("static/video")
    data = yt.streams.filter(progressive=True, file_extension='mp4').first()
    os.rename(f'static/video/{data.default_filename}', 'static/video/video.mp4')
    # song_title.append(title)
    return redirect(url_for('download_video'))

@app.route('/download_video', methods=['GET', 'POST'])
def download_video():
    file_list = os.listdir('static/video')
    # title = song_title[-1]
    print(file_list)
    take = request.args.get('take')
    if take: 
        path = f"static/video/video.mp4"
        # print(path)
        return send_file(path, as_attachment=True)
    return render_template('download.html')


if __name__ == "__main__":
    app.run(debug=True)