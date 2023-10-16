from tkinter import *
import tkinter as tk
from main import center_window


def start_window():
    main_window = tk.Tk()
    main_window.geometry("1400x700")
    main_window.title("To-do list")
    center_window(main_window)
    main_window.mainloop()


if __name__ == '__main__':
    start_window()
