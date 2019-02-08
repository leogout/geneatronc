from tkinter import Tk, Label, Button, Frame, Entry
from PIL import Image, ImageTk
from random import randint

class App:
    def __init__(self, master):
        self.fullscreen = False

        self.master = master

        self.master.title("A simple GUI")

        self.master.attributes("-fullscreen", self.fullscreen)
        self.master.bind("<F11>", self.toggle_fullscreen)

        self.label = Label(self.master, text="Geneatronc")
        self.label.pack()

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()

        self.person_button = Button(self.master, text="Person", command=self.on_person_button_press)
        self.person_button.pack()

        self.cards = [
            Card("Lena", "Brooke", "Top Model", "04 79 84 79 30", "img/lena.png"),
            Card("Bob", "Brooke", "Etudiant", "06 86 84 30 25", "img/bob.png"),
            Card("Robert", "Brooke", "Retraité", "06 98 62 34 97", "img/robert.png"),
            Card("Tom", "Hardy", "Manager", "07 52 46 23 21", "img/tom.png"),
            Card("Alexa", "Amazon", "Doubleuse", "06 30 21 51 54", "img/alexa.png"),
        ]

        self.card = None

    def on_person_button_press(self, event=None):
        if self.card is not None:
            self.card.destroy()

        self.card = CustomWidget(self.master, self.cards[randint(0,4)])
        self.card.pack()

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.master.attributes("-fullscreen", self.fullscreen)


class CustomWidget(Frame):
    def __init__(self, parent, card):
        Frame.__init__(self, parent)

        self.name = Label(self, text="{} {}".format(card.first_name, card.last_name), padx=10)
        self.phone = Label(self, text=card.phone, padx=10)
        self.profession = Label(self, text=card.profession, padx=10)

        self.photo = Label(self, image=card.photo)
        self.photo.image = card.photo

        self.name.grid(row=0, column=3)
        self.phone.grid(row=1, column=3, pady=4)
        self.profession.grid(row=2, column=3, pady=4)
        self.photo.grid(row=0, column=0, columnspan=3, rowspan=3, padx=5)


class Card:
    def __init__(self, first_name, last_name, profession, phone, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession
        self.phone = phone
        image = Image.open(photo)
        image.thumbnail((200, 200))
        self.photo = ImageTk.PhotoImage(image)


root = Tk()
my_gui = App(root)
root.mainloop()


