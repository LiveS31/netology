import requests
import pprint
#  https://github.com/tabelsky/iterators_netology
#list = [i*2 for i in range(100)]
# левая сторона (после =) что делать с i
#   правая сторона откуда брать i
# = for i in range (100):
      #   i+=2
class SwapiPeople:

    def __init__(self):
        pass

    def __iter__(self):
        self.next_page = 'https://swapi.dev/api/people'
        self.results = iter([])
        return self

    def __next__(self):
        try:
            character = next(self.results)
        except StopIteration:
            if self.next_page is None:
                raise StopIteration
            response = requests.get(self.next_page).json()
            self.next_page = response['next']
            self.results = iter(response['results'])
            character = next(self.results)
        return character

swapi_people = SwapiPeople()
for item in swapi_people:
    print(item)

#####
import requests


def swapi_people_generator():
    next_page = "https://swapi.dev/api/people"
    while next_page:
        response = requests.get(next_page).json()
        next_page = response["next"]
        results = response["results"]
        for item in results:
            yield item


high_people = (
    item
    for item in swapi_people_generator()
    if item.get("height") != "unknown" and int(item.get("height", 0)) > 190
)


for item in high_people:
    print(item)