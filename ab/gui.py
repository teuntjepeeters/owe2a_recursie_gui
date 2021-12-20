import tkinter
from tkinter import messagebox


class GUI:

    def __init__(self, string):
        # Declare variables
        self.string = string

        # Maak de main window aan
        self.main_window = tkinter.Tk()


        # Maak twee frames aan (top and bottom)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bottom_frame.pack()

        # Maak labels aan
        #self.label2 = tkinter.Label(self.bottom_frame,
        #                            text="Hello bottom frame!")
        #self.label2.pack()

        self.label1 = tkinter.Label(self.top_frame,
                                    text="Hello top frame!")
        self.label1.pack()

        # Maak knopjes aan
        self.knopje = tkinter.Button(self.bottom_frame,     # Waar komt de knop?
                                     text="Klik hier!",     # Welke tekst wordt weergegeven?
                                     command=self.do_something)  # Wat moet er gebeuren als er op de knop wordt gedrukt?

        self.knopje.pack()
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="quit",
                                          command=self.main_window.destroy)
        self.quit_button.pack()
        # Geef de main window weer
        tkinter.mainloop()

    def do_something(self):
        print(self.string)
        tkinter.messagebox.showinfo("Response",
                                    "Bedankt voor het klikken!")


def main():
    gui = GUI("Hello world!")
    print("Hello world!")

main()