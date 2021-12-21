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
        self.label1 = tkinter.Label(self.bottom_frame,               # 1. Waar komt dit label te staan?,
                                    text="Bijna kerstvakantie!")    # 2. Welke tekst komt in het label te staan?
        self.label1.pack()
        self.label2 = tkinter.Label(self.top_frame,
                                    text="Bijna 2022!")
        self.label2.pack()
        # Roep de main window aan
        tkinter.mainloop()

def main():
    gui = GUI()

main()