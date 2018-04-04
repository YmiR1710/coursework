def search(genre):
    import tmdbsimple as tmdb
    tmdb.API_KEY = '0d77f0dc778bfd9a40a934c56e81b487'
    lst = []
    a = tmdb.Movies().top_rated(page=1)
    num = a.get('total_pages')
    for i in range(1, num):
        film_dict = dict()
        a = tmdb.Movies().top_rated(page=i)
        b = a.get('results')
        for j in b:
            id = j.get('id')
            movie = tmdb.Movies(id)
            info = movie.info()
            gnr = info.get('genres')
            c = 0
            for l in gnr:
                if l.get('name') == genre:
                    c += 1
            if c > 0:
                film_dict['vote_average'] = info.get('vote_average')
                film_dict['budget'] = info.get('budget')
                film_dict['genres'] = info.get('genres')
                film_dict['popularity'] = info.get('popularity')
                film_dict['runtime'] = info.get('runtime')
                film_dict['title'] = info.get('title')
                film_dict['vote_count'] = info.get('vote_count')
            else:
                pass
        print(film_dict)
        lst.append(film_dict)
    return lst


def analise():
    pass
