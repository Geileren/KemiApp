from tkinter import *

class Menu():
    def __init__(self, root):
        self.root = root
        self.start_up()

    def start_up(self):
        Button(self.root, text="Åben Bjerrumdiagram-tegner").grid(column=1, row=1)

def tegn_menu():
    root = Tk()
    root.geometry("500x500")
    Menu(root)
    root.mainloop()




if __name__ == '__main__':
    tegn_menu()

