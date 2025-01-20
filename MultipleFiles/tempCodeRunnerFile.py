import tkinter as tk
from tkinter import messagebox
from o1_Tambah_anime import tambah_anime
from o2_Lihat_anime import lihat_anime
from o3_Hapus_anime import hapus_anime
from o4_Update_anime import update_anime

class AnimeDatabaseApp:
    def __init__(self, master):
        self.master = master
        self.master.title("List Nonton Anime")
        self.center_window(400, 300)
        self.master.configure(bg="#0e0e0e")  # Set background color

        self.frame_utama = tk.Frame(self.master, bg="#0e0e0e")
        self.frame_utama.pack(pady=20)

        self.tampilkan_menu()

    def center_window(self, width, height):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def tampilkan_menu(self):
        for widget in self.frame_utama.winfo_children():
            widget.destroy()

        tk.Label(self.frame_utama, text="Simpan List Anime", font=("Arial", 20, "bold"),fg="white", bg="#0e0e0e").pack(pady=10)

        # Button Style
        button_style = {
            'font': ("Arial", 12),
            'bg': "#4CAF50",  
            'fg': "white",    
            'activebackground': "#45a049",
            'width': 20,
            'padx': 10,
            'pady': 5
        }

        tk.Button(self.frame_utama, text="Tambah Anime", command=tambah_anime, **button_style).pack(pady=5)
        tk.Button(self.frame_utama, text="Lihat Anime", command=lihat_anime, **button_style).pack(pady=5)
        tk.Button(self.frame_utama, text="Hapus Anime", command=hapus_anime, **button_style).pack(pady=5)
        tk.Button(self.frame_utama, text="Update Anime", command=update_anime, **button_style).pack(pady=5)
        tk.Button(self.frame_utama, text="Keluar", command=self.exit_program, **button_style).pack(pady=10)

    def exit_program(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimeDatabaseApp(root)
    root.mainloop()