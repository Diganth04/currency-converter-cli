import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]/best',  # Single-file format, no merging needed
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
        return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started downloading...")
        download_video(video_url, save_dir)
    else:
        print("No save location selected.")