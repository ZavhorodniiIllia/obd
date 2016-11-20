import pickle

class Model:

    def __init__(self, file_name):
        self.__director_lst = []
        self.__film_lst = []
        self.load(file_name)

    def load(self, file_name):
        try:
            with open(file_name, 'rb') as f:
                self.__director_lst, self.__film_lst = pickle.load(f)
        except:
            self.__director_lst = []
            self.__film_lst = []


    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump([self.__director_lst, self.__film_lst], f)


    def delete_film(self, key, value):
        self.__film_lst = filter(lambda element: element['key'] != value, self.__film_lst)

    def del_film_rec(self, album_id, name):
        self.__film_lst = filter(lambda x: x['director_id'] != album_id and x['name'] != name, self.__film_lst)

    def del_film(self, id):
        self.__film_lst = filter(lambda x: x['id'] != id, self.__film_lst)


    def delete_director(self, id):
        self.delete_film('director_id', id)
        self.__director_lst = filter(lambda element: element['id'] != id, self.__director_lst)


    def add_director(self, name, fimsnumber):
        if self.__director_lst == []:
            id = 0
        else:
            id = self.__director_lst[-1]['id'] + 1

        self.__director_lst.append({'id': id, 'name': name, 'fimsnumber': fimsnumber})


    def add_film(self, name, country, year, director_id):
        is_director_exist = filter(lambda element: element['id'] == director_id, self.__director_lst)
        if is_director_exist == []:
            raise Exception('Incorrect director id.')

        if self.__film_lst == []:
            id = 0
        else:
            id = self.__film_lst[-1]['id'] + 1

        self.__film_lst.append({'id': id, 'name': name, 'country': country, 'year': year, 'director_id': director_id})

    def film_country(self, country):
        UkraineFilm = filter(lambda element: str(element['country']) == country, self.__film_lst)
        #return [i for i in self.__director_lst for j in self.__film_lst if i['id'] == j['director_id']& j['country']== 'Ukraine']
        return [j for i in self.__film_lst if i['country']=='Ukraine' for j in self.__director_lst if j['id']==i['director_id']]

    def is_exist(self, id, lst):
        item = filter(lambda x: x['id'] == id, lst)
        if item:
            return True
        return False

    def __find(self, id, lst):
        for item in lst:
            if item['id'] == id:
                return lst.index(item)

    def director_update(self, id, key, value):
        indx = self.__find(id, self.__director_lst)
        self.__director_lst[indx][key] = value

    def film_update(self, id, key, value):
        indx = self.__find(id, self.__session_lst)
        self.__film_lst[indx][key] = value

    def get_director(self):
        return self.__director_lst

    def get_film(self):
        return self.__film_lst

    def is_time_correct(self, time):
        if ':' not in time:
            raise Exception('Incorrect record')

        try:
            hour = int(time.split(':')[0])
            minutes = int(time.split(':')[1])
        except ValueError:
            raise Exception('Incorrect record')

        if (hour >= 0 and hour <= 23) and (minutes >= 0 and minutes <= 59 ):
            return True
        else:
            raise Exception('Incorrect record')
