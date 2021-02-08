import json
import os


class ReadWrite:
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.data = self.read_data()

    def folder_file(self):
        return self.folder + self.filename

    def write_data(self, data):
        # Save to json-file
        try:
            with open(self.folder_file(), "w", encoding="utf-8") as file_obj:
                json.dump(data, file_obj, ensure_ascii=False)
                self.data = data
        except FileNotFoundError as err:
            print(f"File not found {err}")

    def read_data(self):
        # Read from json-file
        try:
            with open(self.folder_file(), "r", encoding="utf-8") as file_obj:
                content = json.load(file_obj)
                return content
        except IOError:
            if not os.path.exists(self.folder):
                os.makedirs(self.folder)
            print(f"File not accessible, creating {self.filename}")
            with open(self.folder_file(), "w", encoding="utf-8") as file_obj:
                json.dump([], file_obj, ensure_ascii=False)

    def append_data(self, data):
        self.data.append(data)

    def show_data(self, order=""):
        # Show entries from json file with reversed order controller
        i = 1
        if order == "reverse":
            movies = list(reversed(self.data))
        elif order == "asc":
            movies = sorted(self.data, key=lambda k: k['Title'])
        else:
            movies = self.data
        for movie in movies:
            print("{:>2s}. {} ({})".format(str(i), movie['Title'], movie['Year']))
            i += 1
            if order == "reverse" and i > 10:
                break
        return movies
