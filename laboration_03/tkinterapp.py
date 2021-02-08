from tkinter import *


class TKInterApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Filmify')
        self.root.minsize(width=1000, height=600)
        self.root.config(padx=12, pady=12)

        self.top_menu = Frame(self.root, width=800, height=20, bg="#eeeeee")

        self.column1 = Frame(self.root, width=250, bg="#eeeeee")

        self.column2 = Frame(self.root, width=450, bg="#eeeeee", padx=12)

        self.column3 = Frame(self.root, width=150, bg="#eeeeee")

        self.top_menu.grid(row=0, column=0, columnspan=3, sticky="NW")

        self.column1.grid(row=1, column=0, rowspan=2, sticky="NW")
        self.column2.grid(row=1, column=1, sticky="NW")
        self.column3.grid(row=1, column=2, sticky="NW")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # ----------------- SEARCH COLUMN ----------------------
        self.create_button(self.top_menu, 'Quit App', self.quit_app, 0, 0, "W")
        self.create_button(self.top_menu, 'Button 2', self.button2, 1, 0, "E")

        self.create_label(self.column1, 'Search', 0, 0, "W")
        self.create_entry(self.column1, 0, 0, "E")
        self.create_button(self.column1, 'Search', self.button2, 0, 1, "W")

        self.create_label(self.column1, 'Search Results', 0, 2, "W")
        self.listbox = self.create_listbox(self.column1, 0, 3, 6)

        self.create_label(self.column1, 'Previous Searches', 0, 4, "W")
        self.listbox = self.create_listbox(self.column1, 0, 5, 20)
        self.create_button(self.column1, 'Add Movie', self.button2, 0, 6, "W")

        # ----------------- MOVIE COLUMN ----------------------
        self.create_label_title(self.column2, 'Title of Movie Title of Movie (2021)', 0, 0, 'W', ('Arial', 20, 'bold'))
        self.create_label(self.column2, 'Movie Details: runtime, date...', 0, 1, 'W')
        self.create_label(self.column2, 'Director, Writer, Actors', 0, 2, 'W')
        self.create_label_title(self.column2, 'Storyline', 0, 3, 'W', ('Arial', 16))
        self.create_label(self.column2, 'An alien has hit the Earth on an unrelening assault...', 0, 4, 'W')

        # ----------------- POSTER / RATING COLUMN ----------------------
        self.create_label_title(self.column3, 'POSTER GOES HERE', 0, 0, 'W', ('Arial', 16, 'bold'))
        self.create_label_title(self.column3, 'RATINGS GOES HERE', 0, 1, 'W', ('Arial', 12, 'bold'))

        self.root.mainloop()

    def quit_app(self):
        self.root.destroy()

    def button2(self):
        print("Useless Button to press.")

    def create_main(self):
        main_window = Tk()
        main_window.title('Filmify')
        main_window.minsize(width=1000, height=600)
        main_window.config(padx=12, pady=12)
        return main_window

    def create_label(self, frame, title, col, row, pos):
        lbl = Label(frame, text=title)
        lbl.grid(column=col, row=row, sticky=pos)

    def create_label_title(self, frame, title, col, row, pos, font):
        lbl = Label(frame, text=title, font=font)
        lbl.grid(column=col, row=row, sticky=pos)

    def create_entry(self, frame, col, row, pos):
        entry = Entry(frame, width=40)
        entry.insert(END, string="Title of Movie")
        entry.grid(column=col, row=row, sticky=pos)

    def create_button(self, frame, title, cmd, col, row, pos):
        b = Button(frame, text=title, command=cmd)
        b.grid(column=col, row=row, sticky=pos, padx=8, pady=8)

        #b.pack()

    def create_listbox(self, frame, col, row, height):
        lb = Listbox(frame, width=50, height=height)
        movie_list = [
            {'title': 'Edge of Tomorrow',
            'year': '2014',
            'released': "06 Jun 2014",
            'runtime': "113 min"},
            {'title': 'Oblivion',
             'year': '2013',
             'released': "01 Jun 2013",
             'runtime': "124 min"}]
        i = 0
        for movie in movie_list:
            movie_out = "{} ({}), {}".format(movie["title"], movie["year"], movie["runtime"])
            lb.insert(i, movie_out)
            i += 1
        lb.grid(column=col, row=row)
        return lb


if __name__ == "__main__":
    main_win = TKInterApp()
