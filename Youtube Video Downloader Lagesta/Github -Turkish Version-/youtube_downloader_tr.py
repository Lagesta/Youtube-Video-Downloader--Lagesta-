# ============================================================
# 📺 PROJE    : LAGESTA YOUTUBE İNDİRİCİ
# 👨‍💻 YAZAR    : Lagesta
# 🌐 GITHUB   : https://github.com/Lagesta
# 📜 LİSANS   : MIT
# 🛠️ VERSİYON : 1.0.0
# ============================================================
# Bu araç YouTube videolarını kolayca indirmek için yapıldı.
# ============================================================

import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os

def video_indir():
    # Klasör seçimi için arayüz hazırlığı
    root = tk.Tk()
    root.withdraw()
    
    print("========================================")
    print("      LAGESTA YOUTUBE INDIRICI v1.0")
    print("           Yazar: Lagesta")
    print("      https://github.com/Lagesta")
    print("========================================\n")
    
    link = input("🔗 YouTube Linkini Yapıştırın: ")
    
    print("\nİndirme Kalitesini Seçin:")
    print("1 - 1080p (En Yüksek - FFmpeg Gerektirebilir)")
    print("2 - 720p  (HD - Önerilen / En Kararlı)")
    print("3 - 480p  (Hızlı İndirme)")
    secim = input("\nSeçiminiz (1/2/3): ")

    # Kalite Mantığı
    if secim == "1":
        kalite_ayari = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
        mod = "1080p"
    elif secim == "2":
        kalite_ayari = 'best[height<=720][ext=mp4]/best'
        mod = "720p"
    elif secim == "3":
        kalite_ayari = 'best[height<=480][ext=mp4]/best'
        mod = "480p"
    else:
        print("⚠️ Geçersiz seçim! Mevcut en iyi kalite seçiliyor.")
        kalite_ayari = 'best'
        mod = "Otomatik"

    print("\n📂 Kaydedilecek klasörü seçmeniz bekleniyor...")
    indirilecek_dizin = filedialog.askdirectory(title="Videonun Kaydedileceği Klasörü Seçin")
    
    if not indirilecek_dizin:
        print("❌ Klasör seçilmedi! Çıkış yapılıyor...")
        input("\nKapatmak için Enter'a basın...")
        return

    ydl_opts = {
        'format': kalite_ayari,
        'outtmpl': os.path.join(indirilecek_dizin, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    try:
        print(f"\n⏳ {mod} modunda indiriliyor... Lütfen bekleyin.")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"\n✅ BAŞARILI! Video şuraya kaydedildi: {indirilecek_dizin}")
    except Exception as e:
        print(f"\n❌ HATA OLUŞTU: {e}")
        print("İpucu: Eğer 1080p hata veriyorsa 720p deneyin veya FFmpeg kurun.")

    print("\n" + "="*40)
    input("Çıkış yapmak için Enter'a basın...")

if __name__ == "__main__":
    video_indir()
