import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['AnimeDB']

def update_anime():
    def save_update():
        id_anime = entry_id_anime.get()
        judul = entry_judul.get()
        genre = entry_genre.get().split(",")
        tahun_rilis = entry_tahun_rilis.get()
        rating = entry_rating.get()
        sinopsis = entry_sinopsis.get()

        result = db.anime.update_one(
            {"_id": id_anime},
            {
                "$set": {
                    "judul": judul,
                    "genre": genre,
                    "tahun_rilis": int(tahun_rilis),
                    "rating": float(rating),
                    "sinopsis": sinopsis
                }
            }
        )

        if result.modified_count > 0:
            messagebox.showinfo("Info", "Anime berhasil diperbarui!")
            window.destroy()
        else:
            messagebox.showwarning("Warning", "Anime tidak ditemukan atau tidak ada perubahan.")

    window = tk.Toplevel()
    window.title("Update Anime")

    tk.Label(window, text="ID Anime:").grid(row=0, column=0)
    entry_id_anime = tk.Entry(window)
    entry_id_anime.grid(row=0, column=1)

    tk.Label(window, text="Judul:").grid(row=1, column=0)
    entry_judul = tk.Entry(window)
    entry_judul.grid(row=1, column=1)

    tk.Label(window, text="Genre (pisahkan dengan koma):").grid(row=2, column=0)
    entry_genre = tk.Entry(window)
    entry_genre.grid(row=2, column=1)

    tk.Label(window, text="Tahun Rilis:").grid(row=3, column=0)
    entry_tahun_rilis = tk.Entry(window)
    entry_tahun_rilis.grid(row=3, column=1)

    tk.Label(window, text="Rating:").grid(row=4, column=0)
    entry_rating = tk.Entry(window)
    entry_rating.grid(row=4, column=1)

    tk.Label(window, text="Sinopsis:").grid(row=5, column=0)
    entry_sinopsis = tk.Entry(window)
    entry_sinopsis.grid(row=5, column=1)

    tk.Button(window, text="Simpan Perubahan", command=save_update).grid(row=6, columnspan=2)

# Jika Anda ingin menguji fungsi ini secara langsung
if __name__ == "__main__":
    update_anime()