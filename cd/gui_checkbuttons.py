import tkinter
from tkinter import messagebox

class GUI:
    def __init__(self):
        # Maak een main window aan
        self.main_window = tkinter.Tk()

        # Pas de grootte aan van de window die verschijnt
        self.main_window.geometry("1000x200")

        # Maak twee frames aan voor checkbox en knopjes
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Maak drie intvar objecten voor de checkbox
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # Zet de drie intvar objecten naar 0
        self.cb_var1.set(1)
        self.cb_var2.set(1)
        self.cb_var3.set(0)

        # Checkbuttons aanmaken
        self.cb1 = tkinter.Checkbutton(self.top_frame, # Locatie, waar wil je button neerzetten?
                                       text="Kaas", # Text die wordt weergegeven bij de button
                                       variable=self.cb_var1) # Koppel het intvar object eraan
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text="Chocolade",
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text="Tiramisu",
                                       variable=self.cb_var3)

        # Buttons aanmaken (OK button en quit button)
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text="OK",
                                        command=self.showresults)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                        text="QUIT",
                                        command=self.main_window.destroy)

        # Pack values
        ### Frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        ### Checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Ok and quit button
        self.ok_button.pack()
        self.quit_button.pack()
        # Geef de main window weer
        tkinter.mainloop()

    def showresults(self):
        # Zodra er op OK wordt gedrukt moet in een messagebox worden
        # weergegeven welke checkbox is aangevinkt
        self.message = "Uw snack of snacks vanavond:\n"
        if self.cb_var1.get() == 1:
            self.message = self.message + "Kaas\n"
        if self.cb_var2.get() == 1:
            self.message = self.message + "Chocolade\n"
        if self.cb_var3.get() == 1:
            self.message = self.message + "Tiramisu\n"
        tkinter.messagebox.showinfo("Snacks", self.message)

def main():
    gui = GUI()

main()