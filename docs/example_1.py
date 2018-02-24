#small example of using tmdb API
import tmdbsimple
tmdbsimple.API_KEY = '0d77f0dc778bfd9a40a934c56e81b487'
search = tmdbsimple.Search()
a = input()
result = search.movie(query=a)
for s in search.results:
    print(s['title'], s['id'], s['release_date'], s['popularity'])
