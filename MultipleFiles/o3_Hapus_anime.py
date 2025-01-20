import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['AnimeDB']

def hapus_anime():
    def delete_anime():
        id_anime = entry_id_anime.get()
        result = db.anime.delete_one({"_id": id_anime})

        if result.deleted_count > 0:
            messagebox.showinfo("Info", "Anime berhasil dihapus!")
            window.destroy()
        else:
            messagebox.showwarning("Warning", "Anime tidak ditemukan.")

    window = tk.Toplevel()
    window.title("Hapus Anime")

    tk.Label(window, text="ID Anime:").grid(row=0, column=0)
    entry_id_anime = tk.Entry(window)
    entry_id_anime.grid(row=0, column=1)

    tk.Button(window, text="Hapus Anime", command=delete_anime).grid(row=1, columnspan=2)

# Jika Anda ingin menguji fungsi ini secara langsung
if __name__ == "__main__":
    hapus_anime()