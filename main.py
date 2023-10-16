from tkinter import *
import tkinter as tk


def center_window(window):
    window.update_idletasks()
    main(window)


def create_to_do(bestand, user_input):
    with open(bestand, "a") as file_data:
        file_data.write(f"{user_input.get()}\n")
        user_input.delete(0, tk.END)


def show_create_to_do(bestand, main_window):
    for widget in main_window.winfo_children():
        widget.destroy()
    create_to_do_label = Label(main_window, text="Maak een nieuwe To-do!", font=('Helvetica bold', 26))
    create_to_do_label.pack()
    gebruikers_input = Entry(main_window, width=50)
    gebruikers_input.pack()
    maak_to_do_button = Button(main_window, text="Create to-do list", width=30, height=2, borderwidth=4,
                                 command=lambda: create_to_do(bestand, gebruikers_input))
    maak_to_do_button.place(x=445, y=300)
    terug_knop = Button(main_window, text="Terug", width=30, height=2, borderwidth=4,
                                 command=lambda: main(main_window))
    terug_knop.place(x=745, y=300)


def show_all_to_do(bestand, main_window):
    for widget in main_window.winfo_children():
        widget.destroy()
    scrollbar = Scrollbar(main_window)
    scrollbar.pack(side=RIGHT, fill=Y)
    with open(bestand, "r") as file_data:
        counter = 0
        waarom = Listbox(main_window, yscrollcommand=scrollbar.set)
        for lines in file_data:
            counter += 1
            waarom.insert(END, f"{counter}. {lines}")
            # show_all = Label(main_window, text=f"{counter}. {lines}")
            delete_to_do_button = Button(main_window, text="Delete", width=10, height=1,
                                         command=lambda line=counter: delete_to_do(bestand, main_window, line))
            delete_to_do_button.pack()

            scrollbar.config(command=waarom.yview)
            waarom.pack(side=LEFT, fill=BOTH)

    terug_knop = Button(main_window, text="Main menu", command=lambda: main(main_window))
    terug_knop.pack()


def delete_to_do(bestand, main_window, lijn_nummer):
    with open(bestand, "r") as file_data:
        lines = file_data.readlines()
        if lijn_nummer <= len(lines):
            del lines[lijn_nummer - 1]
            with open(bestand, "w") as bestand_data:
                for line in lines:
                    bestand_data.write(line)
            show_all_to_do(bestand, main_window)
        else:
            lijn_bestaat_niet = Label(main_window, text=f"De lijn {lijn_nummer} bestaat niet")
            lijn_bestaat_niet.pack()


def sluiten(main_window):
    main_window.destroy()


def main(main_window):
    for widget in main_window.winfo_children():
        widget.destroy()

    background_image = tk.PhotoImage(file="background.png")

    background_label = tk.Label(main_window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    bestand = "to-do_list.txt"
    show_create_to = Button(main_window, text="Create to-do list", width=30, height=2, borderwidth=4,
                      command=lambda: show_create_to_do(bestand, main_window))
    show_create_to.place(x=445, y=100)

    show_all = Button(main_window, text="Show all to-do lists", width=30, height=2, borderwidth=4,
                      command=lambda: show_all_to_do(bestand, main_window))
    show_all.place(x=445, y=200)

    sluit_knop = Button(main_window, text="Sluiten", width=30, height=2, borderwidth=4,
                                 command=lambda: sluiten(main_window))
    sluit_knop.place(x=445, y=400)
