import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['AnimeDB']

def lihat_anime():
    window = tk.Toplevel()
    window.title("Daftar Anime")

    # Membuat frame untuk Treeview
    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    # Membuat Treeview
    columns = ('ID', 'Judul', 'Genre', 'Tahun Rilis', 'Rating', 'Sinopsis')
    tree = ttk.Treeview(frame, columns=columns, show='headings')
    
    # Mengatur lebar kolom
    tree.column('ID', width=50)
    tree.column('Judul', width=200)
    tree.column('Genre', width=100)
    tree.column('Tahun Rilis', width=100)
    tree.column('Rating', width=70)
    tree.column('Sinopsis', width=300)

    # Menambahkan judul kolom
    for col in columns:
        tree.heading(col, text=col)

    # Mengambil data anime dari database dan menambahkannya ke Treeview
    anime_list = db.anime.find()
    for anime in anime_list:
        tree.insert('', 'end', values=(anime['_id'], anime['judul'], ', '.join(anime['genre']), anime['tahun_rilis'], anime['rating'], anime['sinopsis']))

    # Menampilkan Treeview
    tree.pack()

# Jika Anda ingin menguji fungsi ini secara langsung
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Anime Database")
    lihat_anime()
    root.mainloop()