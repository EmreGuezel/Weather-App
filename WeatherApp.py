import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    appid = '9c58fd44c33f99e74b4d71901f8d1464'
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=tr&appid={appid}'
    try:
        r = requests.get(URL)
        r.raise_for_status()
        res = r.json()
        condition = res['weather'][0]['main']
        description = res['weather'][0]['description']
        temp = res['main']['temp']
        return condition, description, temp
    except requests.exceptions.HTTPError as err:
        return None, None, f"HTTP Error: {err}"
    except requests.exceptions.RequestException as err:
        return None, None, f"Request Error: {err}"

root = tk.Tk()
root.title("Hava Durumu Uygulaması")
root.geometry("400x300")

entry = tk.Entry(root)
entry.pack(pady=10)

def button_click():
    city = entry.get()
    condition, description, temp = get_weather(city)
    if condition and description:
        messagebox.showinfo("Bilgi", f"Şehir: {city}\nDurum: {condition}\nAçıklama: {description}\nSıcaklık: {temp}°C")
    else:
        messagebox.showinfo("Bilgi", f"Şehir: {city}\nHata: {temp}")

button = tk.Button(root, text="Hadi Öğrenelim", command=button_click)
button.pack(pady=10)

root.mainloop()
