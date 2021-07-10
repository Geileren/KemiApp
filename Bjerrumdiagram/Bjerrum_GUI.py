from tkinter import *
import sys
import Bjerrum_logik
class Bjerrum:

    def __init__(self):
        self.root = Tk()
        self.acids = []
        self.start()
        self.root.mainloop()

    def start(self):

        self.start_frame = Frame()
        self.start_frame.grid(column=1, row=1)

        Button(self.start_frame, text="Luk Bjerrumdiagram-tegner", command=self.root.destroy).grid(column=1, row=5)
        Label(self.start_frame, text="Hvor mange syrer optræder i din opløsning?").grid(column=0, row=1)
        Label(self.start_frame, text="(polyhydrone syrer optræder som flere syrer)").grid(column=0, row=2)
        #entry antal hydroner
        self.hydroner = Entry(self.start_frame, width=4)
        self.hydroner.grid(column=1, row=1)
        #knap til at åbne næste
        Button(self.start_frame, text="Næste", command=self.midstate1).grid(column=3, row=1)


    def midstate1(self):
        self.amount = int(self.hydroner.get())
        self.start_frame.destroy()
        self.input_()

    def input_(self):
        self.input_frame = Frame()
        self.input_frame.grid(column=1, row=1)
        for i in range(1,self.amount+1):
            print(i)
            Label(self.input_frame, text=f"pk_s af den {i}. syre:").grid(column=1, row=i)
            self.acids.append(Entry(self.input_frame))
            self.acids[i-1].grid(column=2, row=i)

        Button(self.input_frame, text="Tegn Diagram", command=self.midstate2).grid(column=3, row=99)

    # i næste
    # entry, med labels, svarende til antal hydroner
    # tegn og hvis diagram med logik
    def midstate2(self):
        for i in range(len(self.acids)):
            self.acids[i] = float(self.acids[i].get())
        self.input_frame.destroy()
        self.draw()

    def draw(self):
        Bjerrum_logik.draw_Graph(self.acids, self.amount)
        self.result = PhotoImage(file=rf"{sys.path[0]}\Bjerrumsaves\save.png")
        self.result_frame = Frame(self.root, bg="white")
        self.result_frame.grid(column=1, row=1)
        display_label = Label(self.result_frame, image=self.result)
        display_label.grid(column=1, row=1, columnspan=2)

        Button(self.result_frame, text="Gem som .png", command=self.save_popup).grid(column=1, row=2, sticky="E")
        Button(self.result_frame, text="Tegn nyt diagram", command=self.midstate3).grid(column=2, row=2, sticky="W")

    def save_popup(self):
        print("kør")
        self.save_top = Toplevel()
        self.save_top.grab_set()


        Label(self.save_top, text="Navngiv billedfilen:").grid(column=1, row=1, columnspan=3)

        Button(self.save_top, text="Annulér", command=self.save_top.destroy).grid(column=1, row=2)
        self.name_entry = Entry(self.save_top)
        self.name_entry.grid(column=2, row=2)

        Button(self.save_top, text="Gem", command=self.save).grid(column=3, row=2)

    def save(self):
        self.filename = self.name_entry.get()
        self.save_top.grab_release()
        self.save_top.destroy()
        Bjerrum_logik.save(self.filename)


        pass

    def midstate3(self):
        pass


Bjerrum()
