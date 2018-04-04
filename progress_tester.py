from tkinter import *
import tmdbsimple as tmdb
tmdb.API_KEY = '0d77f0dc778bfd9a40a934c56e81b487'


class Visualization:

    choice_lst = set()
    a = tmdb.Movies().top_rated(page=1)
    num = a.get('total_pages')
    films_list = []

    @staticmethod
    def visualize_1():
        root = Tk()

        def delete():
            try:
                root.destroy()
                root.update()
            except:
                pass

        l1 = Label(root, width=100, height=0)
        b = Button(root, text='COMEDY', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Comedy'))
        b.pack(side="top", fill='both')
        p = Button(root, text='DRAMA', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Drama'))
        p.pack(side="top", fill="both", )
        q = Button(root, text='ROMANCE', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Romance'))
        q.pack(side="top", fill="both", )
        w = Button(root, text='ANIMATION', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Animation'))
        w.pack(side="top", fill="both", )
        e = Button(root, text='ADVENTURE', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Adventure'))
        e.pack(side="top", fill="both", )
        r = Button(root, text='THRILLER', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Thriller'))
        r.pack(side="top", fill="both", )
        t = Button(root, text='FANTASY', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Fantasy'))
        t.pack(side="top", fill="both", )
        y = Button(root, text='FAMILY', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Family'))
        y.pack(side="top", fill="both", )
        u = Button(root, text='ACTION', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Action'))
        u.pack(side="top", fill="both", )
        i = Button(root, text='CRIME', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Crime'))
        i.pack(side="top", fill="both", )
        o = Button(root, text='MYSTERY', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Mystery'))
        o.pack(side="top", fill="both", )
        a = Button(root, text='SCIENCE FICTION', activebackground='blue', fg='black',
                   activeforeground='black', height=3, bg='sky blue',
                   command=lambda: Visualization.choice_lst.add('Science fiction'))
        a.pack(side="top", fill="both", )
        l = Button(text='OK', command=delete, bg='sky blue', activebackground='blue', width=10, height=2)
        l.pack()
        l1.pack()
        root.mainloop()

    @staticmethod
    def visualize_2(text):
        root = Tk()
        var = StringVar()
        label = Label(root, textvariable=var, width=50, height=20)
        var.set(text)
        label.pack()
        root.mainloop()

    @staticmethod
    def func(n, genres):
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
                        film_dict['vote_average'] = info.get('vote_average')
                        film_dict['budget'] = info.get('budget')
                        film_dict['genres'] = info.get('genres')
                        film_dict['popularity'] = info.get('popularity')
                        film_dict['runtime'] = info.get('runtime')
                        film_dict['title'] = info.get('title')
                        film_dict['vote_count'] = info.get('vote_count')
        if 'genres' in film_dict:
            Visualization.films_list.append(film_dict)
        print(Visualization.films_list)
        for stats in film_dict:
            s += str(stats) + ': ' + str(film_dict.get(stats)) + '\n'
        return s

    @staticmethod
    def updater():

        def hard_job():
            for i in range(1, Visualization.num):
                l['text'] = Visualization.func(i, list(Visualization.choice_lst))
                root.update()
        root = Tk()
        l = Label(text='', height=20, width=100)
        root.after(500, hard_job)
        l.pack()
        root.mainloop()
