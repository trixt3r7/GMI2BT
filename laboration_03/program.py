import gui
from error_checking import num_in_range
from readwrite import ReadWrite
from search import Search
from movie import Movie


# Declare folder & files
folder = "./data/"
filename = "movies.json"

# Load saved json-data
movie_json = ReadWrite(folder, filename)
movies = movie_json.data


def search_movie():
    gui.search_header()
    movie_search = input("Search movie: ")
    new_search = Search(movie_search)
    # If any movie is found run statement
    if new_search.check_response():
        # List search results and return picked movie
        movie_pick = new_search.select_item("Movie to add and view: ", 6)
        # Append movie to list in memory
        movie_json.append_data(movie_pick)
        # Write list to json
        movie_json.write_data(movies)
        # Show detailed information
        movie = Movie(movies[len(movies) - 1])
        movie.movie_details()
    else:
        print("Movie not Found!")


def show_searches():
    gui.previous_header()
    # Show movies from movies.json in reverse order
    movie_json.show_data("reverse")
    gui.hr_header()


def show_movie_details():
    gui.movie_list_header()
    # Show movies from movies.json sorted by Title in ascending order
    movies_list = movie_json.show_data("asc")
    gui.hr_header()
    movie_nr = num_in_range("Pick movie to view: ", movies_list)
    # Show detailed information
    movie = Movie(movies_list[movie_nr])
    movie.movie_details()


# Menu Loop
while True:
    gui.logo()
    gui.print_menu()
    choice = input("Choose menu item: ")
    if choice == '1':
        search_movie()
    elif choice == '2':
        show_searches()
    elif choice == '3':
        show_movie_details()
    elif choice == '4':
        # Exit Program
        break
    else:
        print("Invalid menu item, please try again.")
