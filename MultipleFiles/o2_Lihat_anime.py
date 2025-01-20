import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['AnimeDB']

def lihat_anime():
    window = tk.Toplevel()
    window.title("Daftar Anime")

    # Mengambil data anime dari database
    anime_list = db.anime.find()

    for anime in anime_list:
        tk.Label(window, text=f"ID: {anime['_id']}, Judul: {anime['judul']}, Genre: {', '.join(anime['genre'])}, Tahun Rilis: {anime['tahun_rilis']}, Rating: {anime['rating']}, Sinopsis: {anime['sinopsis']}").pack()

# Jika Anda ingin menguji fungsi ini secara langsung
if __name__ == "__main__":
    lihat_anime()