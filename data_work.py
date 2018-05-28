import visualisation
import tmdbsimple as tmdb
tmdb.API_KEY = '0d77f0dc778bfd9a40a934c56e81b487'


def analise_data(lst):
    date_list = []
    time_list = []
    budget_list = []
    for film in lst:
        coef = float(film.get('vote_average')) / film.get('popularity')
        date_list.append([film.get('release_date'), coef])
        budget_list.append([film.get('budget'), coef])
        time_list.append([film.get('runtime'), coef])

    def calculate(lst_1):
        c = 0
        result = 0
        for i in lst_1:
            c += float(i[1])
        for i in lst_1:
            lst_1[lst_1.index(i)][1] = (i[1] * 100)/c
        for i in lst_1:
            result += (i[0] / 100) * i[1]
        return result

    def calculate_1(lst_2):
        st = set()
        l = []
        c = 0
        for i in lst_2:
            i[0] = i[0].split('-')
            i[0] = i[0][1:]
            i[0].reverse()
        for i in lst_2:
            c += float(i[1])
        for i in lst_2:
            lst_2[lst_2.index(i)][1] = (i[1] * 100) / c
        for i in lst_2:
            st.add(i[0][1])
        st = list(st)
        for i in st:
            for j in lst_2:
                if i == j[0][1]:
                    if i in l:
                        l[l.index(i) + 1] += j[1]
                    else:
                        l.append(i)
                        l.append(j[1])
        mx = 0
        for i in l:
            if type(i) is int or type(i) is float:
                if i > mx:
                    mx = i
                else:
                    pass
        searched_month = l[l.index(mx) - 1]
        searched_day = ''
        votes_lst = []
        for i in lst_2:
            if i[0][1] == searched_month:
                votes_lst.append(i[1])
        max_vote = max(votes_lst)
        for i in lst_2:
            if i[1] == max_vote:
                searched_day = i[0][0]
        return searched_day + '.' + searched_month

    return 'Optimal runtime: ' + str(int(calculate(time_list))) + ' minutes' + '\n' \
           + 'Optimal budget: ' + '$' + str(int(calculate(budget_list))) + '\n' + 'Optimal release date: ' + \
           str(calculate_1(date_list)) + '\n'


def get_data(n, genres):
    film_dict = dict()
    a = tmdb.Movies().top_rated(page=n)
    b = a.get('results')
    s = ''
    for j in b:
        id = j.get('id')
        movie = tmdb.Movies(id)
        info = movie.info()
        gnr = info.get('genres')
        c = 0
        for l in gnr:
            if l.get('name') in genres:
                if info.get('budget') != 0:
                    film_dict['title'] = info.get('title')
                    film_dict['genres'] = info.get('genres')
                    film_dict['release_date'] = info.get('release_date')
                    film_dict['runtime'] = info.get('runtime')
                    film_dict['vote_average'] = info.get('vote_average')
                    film_dict['vote_count'] = info.get('vote_count')
                    film_dict['budget'] = info.get('budget')
                    film_dict['popularity'] = info.get('popularity')
    if 'genres' in film_dict:
        visualisation.Visualization.films_list.append(film_dict)
    gnr_lst = []
    gnr = film_dict.get('genres')
    try:
        for i in gnr:
            gnr_lst.append(i.get('name'))
    except:
        pass
    film_dict['genres'] = gnr_lst
    if film_dict.get('genres') != []:
        for stat in film_dict:
            s += str(stat) + ': ' + str(film_dict.get(stat)) + '\n'
    else:
        s += '\n' * 12
    s += '\n' * 4
    s += '[]' + '[]' * int((int((n*100) / visualisation.Visualization.num) / 2)) + \
         ' ' * (50 - int((int((n*100) / visualisation.Visualization.num) / 2))) + '\n'
    s += 'Analyzed data: ' + str(int((n*100) / visualisation.Visualization.num)) + ' %'
    return s
