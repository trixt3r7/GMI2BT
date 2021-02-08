from tkinter import *


class TKInterApp:
    def __init__(self):
        self.root = self.create_main()

        self.create_menu()

        self.create_button('Stäng applikation', self.quit_app)

        self.label = self.create_label('Input field:')
        self.text_input = self.create_text_input()

        self.listbox = self.create_listbox()

        self.canvas = self.create_canvas()

        self.root.mainloop()

    def create_main(self):
        main_window = Tk()
        main_window.title('This is the main window')
        return main_window

    def create_menu(self):
        mm = Menu(self.root)
        exitmenu = Menu(mm)
        mm.add_cascade(label='Menu', menu=exitmenu)
        exitmenu.add_command(label='Exit', command=self.quit_app)
        # add menu to our main window
        self.root.config(menu=mm)

    def quit_app(self):
        self.root.destroy()

    def create_button(self, title, cmd):
        b = Button(self.root, text=title, command=cmd)
        b.pack()

    def create_text_input(self):
        e = Entry(self.root)
        e.bind('<KeyRelease>', self.text_cb)  # cb = call back
        e.pack()
        e.focus()
        return e

    def text_cb(self, event):
        print(self.text_input.get())

    def create_label(self, text):
        lbl = Label(self.root, text=text)
        lbl.pack()
        return lbl

    def create_listbox(self):
        lb = Listbox(self.root)
        list = ['GIK298', 'GIK289', 'GIK297', 'GIK299']
        i = 0
        for l in list:
            lb.insert(i, l)
            i += 1
        lb.pack()
        return lb

    def create_canvas(self):
        c = Canvas(width=200, height=200, background='red')
        c.bind('<B1-Motion>', self.canvas_button_down)
        c.pack()
        return c

    def canvas_button_down(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, width=0, fill='white')


main_win = TKInterApp()
