import requests
from error_checking import num_in_range


class Search:
    url = 'http://www.omdbapi.com/?apikey='
    key = '00000000' #  API key needed from omdbapi.com
    title_tag = '&t='
    year_tag = '&y='
    imdb_id_tag = '&i='
    plot_tag = '&plot=full'
    plot_short_tag = '&plot=short'
    type_tag = '&type=movie'
    s_title = '&s='  # search

    def __init__(self, search):
        self.search = search
        self.data = self.request_api_data()

    def request_api_data(self):
        url = f'{self.url}{self.key}{self.s_title}{self.search}'
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError(f'Error fetching: {response.status_code}, check')
        return response.json()

    def request_movie_data(self, imdb_id):
        url = f'{self.url}{self.key}{self.imdb_id_tag}{imdb_id}{self.plot_tag}'
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError(f'Error fetching: {response.status_code}, check')
        return response.json()

    def check_response(self):
        # If no movie is found return False
        if self.data['Response'] == 'False':
            return False
        else:
            return True

    def filter_results(self, count):
        i = 0
        filtered = []
        for result in self.data['Search']:
            print("{}. {} ({})".format(i + 1, result['Title'], result['Year']))
            data = {'Title': result['Title'], 'Year': result['Year'], 'imdbID': result['imdbID']}
            filtered.append(data)
            i += 1
            if i == count:
                break
        return filtered

    def select_item(self, input_string, count):
        items_list = self.filter_results(count)
        add_item = num_in_range(input_string, items_list)
        item_id = items_list[add_item]['imdbID']
        item_pick = self.request_movie_data(item_id)
        print(f"You picked: {item_pick['Title']} ({item_pick['Year']})")
        return item_pick

