import customtkinter as ctk

import threading
import os
from tkinter import messagebox

from downloader import download


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #set appearance mode
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("500x600")
        self.wm_minsize(300, 300)
        self.title("YouTube audio downloader")

        #create frames
        self.frame = ctk.CTkFrame(self, fg_color="transparent", width=500)
        self.frame.pack(anchor="n", side="top", expand=True)        

        #add the input
        self.input = ctk.CTkEntry(self.frame, placeholder_text="enter a url", width=350)
        self.input.pack(anchor="center", pady=(200, 50), expand=True)

        #create the buttons
        for i in range(2):
            button = ctk.CTkButton(self.frame, text="Download" if i == 0 else "Choose a folder", width=100,
                                   command = self.download if i == 0 else self.choose_folder)
            button.pack(anchor="n", side = "left" if i == 0 else "right", expand=True)

    def choose_folder(self):
        try:
            dir_ = ctk.filedialog.askdirectory(title="Choose a folder")
            os.chdir(dir_)
        except Exception as e:
            pass

    def download(self):
        try:
            dl = threading.Thread(target=download, args=(self.input.get(),), name="dl")
            dl.start()
            info = messagebox.showinfo(message="please wait...")
        except Exception as e:
            pass

if __name__ == "__main__":
    app = App()
    app.mainloop()