import tkinter
from tkinter import messagebox


class GUI:

    def __init__(self):
        # Maak een window aan
        self.main_window = tkinter.Tk()

        # Maak twee frames aan (top and bottom)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Maak labels aan
        self.label1 = tkinter.Label(self.top_frame,               # 1. Waar komt dit label te staan?,
                                    text="Bijna kerstvakantie!")    # 2. Welke tekst komt in het label te staan?
        self.label1.pack()
        self.label2 = tkinter.Label(self.top_frame,
                                    text="Bijna 2022!")
        self.label2.pack()

        # Maak knoppen aan
        self.knopje = tkinter.Button(self.bottom_frame, # Waar komt de button te staan?
                                     text="Klik hier!", # Tekst die weergegeven wordt op de button
                                     command=self.action)  # Functie die wordt aangeroepen als er op de knop wordt gedrukt
        self.knopje.pack()
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="QUIT",
                                          command=self.main_window.destroy)
        self.quit_button.pack()

        # Roep de main window aan
        tkinter.mainloop()

    def action(self):
        tkinter.messagebox.showinfo("Response",
                                    "Bedankt voor het klikken!")
        print("Hello world!")


def main():
    gui = GUI()

main()