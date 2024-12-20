import yt_dlp
import tkinter as tk
from tkinter import messagebox
import requests
import os

def download_video_from_youtube(url, custom_title, save_path, username, password):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(save_path, f'{custom_title}.%(ext)s'),
    }

    if username and password:
        ydl_opts['username'] = username
        ydl_opts['password'] = password

    try:
        if url.startswith('http'):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        else:
            messagebox.showerror("오류", "유효한 URL이 아닙니다.")
            return

        messagebox.showinfo("성공", "영상 다운로드가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"다운로드 중 오류가 발생했습니다: {e}")

def download_audio_from_youtube(url, custom_title, save_path, username, password):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_path, f'{custom_title}.%(ext)s'),
    }

    if username and password:
        ydl_opts['username'] = username
        ydl_opts['password'] = password

    try:
        if url.startswith('http'):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        else:
            messagebox.showerror("오류", "유효한 URL이 아닙니다.")
            return

        messagebox.showinfo("성공", "오디오 다운로드가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"오디오 다운로드 중 오류가 발생했습니다: {e}")

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)

        messagebox.showinfo("성공", "이미지 다운로드가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"이미지 다운로드 중 오류가 발생했습니다: {e}")

def create_gui():
    window = tk.Tk()
    window.title("불법 다운로드")

    # 입력 필드들
    url_label = tk.Label(window, text="비디오 또는 오디오 URL을 입력하세요:")
    url_label.pack(pady=5)
    url_entry = tk.Entry(window, width=50)
    url_entry.pack(pady=5)

    title_label = tk.Label(window, text="파일 이름을 입력하세요:")
    title_label.pack(pady=5)
    title_entry = tk.Entry(window, width=50)
    title_entry.pack(pady=5)

    image_url_label = tk.Label(window, text="이미지 URL을 입력하세요:")
    image_url_label.pack(pady=5)
    image_url_entry = tk.Entry(window, width=50)
    image_url_entry.pack(pady=5)

    save_path_label = tk.Label(window, text="저장 경로를 입력하세요:")
    save_path_label.pack(pady=5)
    save_path_entry = tk.Entry(window, width=50)
    save_path_entry.pack(pady=5)

    username_label = tk.Label(window, text="아이디를 입력하세요 (선택):")
    username_label.pack(pady=5)
    username_entry = tk.Entry(window, width=50)
    username_entry.pack(pady=5)

    password_label = tk.Label(window, text="비밀번호를 입력하세요 (선택):")
    password_label.pack(pady=5)
    password_entry = tk.Entry(window, width=50, show="*")
    password_entry.pack(pady=5)

    # 영상 다운로드 버튼 클릭 시 호출될 함수
    def on_video_download_button_click():
        url = url_entry.get().strip()
        custom_title = title_entry.get().strip()
        save_path = save_path_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if url and custom_title and save_path:
            if not username or not password:
                messagebox.showinfo("알림", "아이디와 비밀번호는 선택사항입니다. 필요하면 입력해주세요.")
            download_video_from_youtube(url, custom_title, save_path, username, password)
        else:
            messagebox.showwarning("입력 오류", "URL, 제목 및 저장 경로를 입력해 주세요.")

    # 오디오 다운로드 버튼 클릭 시 호출될 함수
    def on_audio_download_button_click():
        url = url_entry.get().strip()
        custom_title = title_entry.get().strip()
        save_path = save_path_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if url and custom_title and save_path:
            if not username or not password:
                messagebox.showinfo("알림", "아이디와 비밀번호는 선택사항입니다. 필요하면 입력해주세요.")
            download_audio_from_youtube(url, custom_title, save_path, username, password)
        else:
            messagebox.showwarning("입력 오류", "URL, 제목 및 저장 경로를 입력해 주세요.")

    # 이미지 다운로드 버튼 클릭 시 호출될 함수
    def on_image_download_button_click():
        image_url = image_url_entry.get().strip()
        save_path = save_path_entry.get().strip()

        if image_url and save_path:
            download_image(image_url, os.path.join(save_path, os.path.basename(image_url)))
        else:
            messagebox.showwarning("입력 오류", "이미지 URL 및 저장 경로를 입력해 주세요.")

    # 다운로드 버튼들
    video_download_button = tk.Button(window, text="영상 다운로드", command=on_video_download_button_click)
    video_download_button.pack(pady=10)

    audio_download_button = tk.Button(window, text="오디오 다운로드", command=on_audio_download_button_click)
    audio_download_button.pack(pady=10)

    image_download_button = tk.Button(window, text="이미지 다운로드", command=on_image_download_button_click)
    image_download_button.pack(pady=10)

    window.mainloop()

# GUI 실행
create_gui()
