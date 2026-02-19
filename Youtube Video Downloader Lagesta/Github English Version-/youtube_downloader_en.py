# Copyright (c) 2026 Lagesta (https://github.com/Lagesta)
# This project is licensed under the MIT License.

#============================================================
# 📺 PROJECT  : LAGESTA YOUTUBE DOWNLOADER
# 👨‍💻 AUTHOR   : Lagesta
# 🌐 GITHUB   : https://github.com/Lagesta
# 📜 LICENSE  : MIT
# 🛠️ VERSION  : 1.0.0
# ============================================================
# [TR] Bu araç YouTube videolarını kolayca indirmek için yapıldı.
# [EN] This tool was created to download YouTube videos easily.
# ============================================================

import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os

def download_video():
    # Setup GUI for folder selection
    root = tk.Tk()
    root.withdraw()
    
    print("========================================")
    print("   LAGESTA YOUTUBE DOWNLOADER v1.0")
    print("        Created by Lagesta")
    print("   https://github.com/Lagesta")
    print("========================================\n")
    
    link = input("🔗 Paste YouTube Link / Linki Yapıştır: ")
    
    print("\nSelect Quality / Kalite Seçin:")
    print("1 - 1080p (Highest - Requires FFmpeg)")
    print("2 - 720p  (HD - Recommended/Stable)")
    print("3 - 480p  (Fast Download)")
    choice = input("\nEnter choice / Seçim (1/2/3): ")

    # Quality Logic
    if choice == "1":
        quality_format = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
        mode = "1080p"
    elif choice == "2":
        quality_format = 'best[height<=720][ext=mp4]/best'
        mode = "720p"
    elif choice == "3":
        quality_format = 'best[height<=480][ext=mp4]/best'
        mode = "480p"
    else:
        print("⚠️ Invalid choice! Using best available format.")
        quality_format = 'best'
        mode = "Auto"

    print("\n📂 Selecting download directory...")
    download_path = filedialog.askdirectory(title="Select Save Location")
    
    if not download_path:
        print("❌ No folder selected! Exiting...")
        input("\nPress Enter to close...")
        return

    ydl_opts = {
        'format': quality_format,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    try:
        print(f"\n⏳ Downloading in {mode} mode... Please wait.")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"\n✅ SUCCESS! Video saved to: {download_path}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("Hint: If 1080p fails, try 720p or install FFmpeg.")

    print("\n" + "="*40)
    input("Press Enter to exit / Çıkmak için Enter'a basın...")

if __name__ == "__main__":
    download_video()
