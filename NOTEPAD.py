import os
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("600x400")

        self.text_area = Text(self.root)
        self.text_area.pack(expand=YES, fill=BOTH)

        self.scrollbar = Scrollbar(self.text_area)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit_application)

        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About Notepad", command=self.show_about)

        self.file_path = None

    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.file_path = None
        self.text_area.delete(1.0, END)

    def open_file(self):
        file_path = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file_path:
            self.file_path = file_path
            self.root.title(os.path.basename(file_path) + " - Notepad")
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, END)
            self.text_area.insert(INSERT, content)

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, END))
        else:
            file_path = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file_path:
                self.file_path = file_path
                self.root.title(os.path.basename(file_path) + " - Notepad")
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, END))

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def show_about(self):
        showinfo("Notepad", "Mrinal Verma")

    def quit_application(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    notepad.run()
