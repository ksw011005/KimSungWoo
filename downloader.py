import yt_dlp
import tkinter as tk
from tkinter import messagebox
import requests
import os

def download_video_from_youtube(url, custom_title, username, password):
    # 영상과 오디오를 모두 다운로드
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # 영상과 오디오 모두 다운로드
        'outtmpl': f'C:/Users/PC/Desktop/pro/{custom_title}.%(ext)s',  # 저장 위치
        'username': username,
        'password': password
    }

    try:
        if url.startswith('http'):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])  # URL을 다운로드
        else:
            messagebox.showerror("오류", "유효한 URL이 아닙니다.")
            return

        messagebox.showinfo("성공", "영상 다운로드가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"다운로드 중 오류가 발생했습니다: {e}")

def download_audio_from_youtube(url, custom_title, username, password):
    # 오디오만 다운로드
    ydl_opts = {
        'format': 'bestaudio/best',  # 오디오만 다운로드
        'outtmpl': f'C:/Users/PC/Desktop/pro/{custom_title}.%(ext)s',  # 저장 위치
        'username': username,
        'password': password
    }

    try:
        if url.startswith('http'):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])  # URL을 다운로드
        else:
            messagebox.showerror("오류", "유효한 URL이 아닙니다.")
            return

        messagebox.showinfo("성공", "오디오 다운로드가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"오디오 다운로드 중 오류가 발생했습니다: {e}")

def download_image(image_url, save_path):
    try:
        # 이미지 URL에서 파일명 추출
        response = requests.get(image_url)
        response.raise_for_status()  # 오류가 발생하면 예외를 발생시킴
        
        # 이미지 저장
        with open(save_path, 'wb') as file:
            file.write(response.content)

        messagebox.showinfo("성공", "이미지 다운로드가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"이미지 다운로드 중 오류가 발생했습니다: {e}")

def create_gui():
    window = tk.Tk()
    window.title("YouTube 다운로드 및 텍스트 추출")

    # URL 입력 필드
    url_label = tk.Label(window, text="URL을 입력하세요:")
    url_label.pack(pady=5)
    url_entry = tk.Entry(window, width=50)
    url_entry.pack(pady=5)

    # 저장할 제목 입력 필드
    title_label = tk.Label(window, text="파일 이름을 입력하세요:")
    title_label.pack(pady=5)
    title_entry = tk.Entry(window, width=50)
    title_entry.pack(pady=5)

    # 사용자 아이디 입력 필드
    username_label = tk.Label(window, text="아이디를 입력하세요:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(window, width=50)
    username_entry.pack(pady=5)

    # 사용자 비밀번호 입력 필드
    password_label = tk.Label(window, text="비밀번호를 입력하세요:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(window, width=50, show="*")  # 비밀번호 숨기기
    password_entry.pack(pady=5)

    # 이미지 URL 입력 필드
    image_url_label = tk.Label(window, text="이미지 URL을 입력하세요:")
    image_url_label.pack(pady=5)
    image_url_entry = tk.Entry(window, width=50)
    image_url_entry.pack(pady=5)

    # 영상 다운로드 버튼 클릭 시 호출될 함수
    def on_video_download_button_click():
        url = url_entry.get().strip()
        custom_title = title_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        
        if url and custom_title and username and password:
            download_video_from_youtube(url, custom_title, username, password)
        else:
            messagebox.showwarning("입력 오류", "URL, 제목, 아이디 및 비밀번호를 모두 입력해 주세요.")

    # 오디오 다운로드 버튼 클릭 시 호출될 함수
    def on_audio_download_button_click():
        url = url_entry.get().strip()
        custom_title = title_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        
        if url and custom_title and username and password:
            download_audio_from_youtube(url, custom_title, username, password)
        else:
            messagebox.showwarning("입력 오류", "URL, 제목, 아이디 및 비밀번호를 모두 입력해 주세요.")

    # 이미지 다운로드 버튼 클릭 시 호출될 함수
    def on_image_download_button_click():
        image_url = image_url_entry.get().strip()
        
        if image_url:
            # 이미지 파일 저장 경로 지정
            save_path = os.path.join('C:/Users/PC/Desktop/pro', os.path.basename(image_url))  # 예시 경로
            download_image(image_url, save_path)
        else:
            messagebox.showwarning("입력 오류", "이미지 URL을 입력해 주세요.")

    # 영상 다운로드 버튼
    video_download_button = tk.Button(window, text="영상 다운로드", command=on_video_download_button_click)
    video_download_button.pack(pady=10)

    # 오디오 다운로드 버튼
    audio_download_button = tk.Button(window, text="오디오 다운로드", command=on_audio_download_button_click)
    audio_download_button.pack(pady=10)

    # 이미지 다운로드 버튼
    image_download_button = tk.Button(window, text="이미지 다운로드", command=on_image_download_button_click)
    image_download_button.pack(pady=10)

    # Tkinter 윈도우 실행
    window.mainloop()

# GUI 실행
create_gui()
