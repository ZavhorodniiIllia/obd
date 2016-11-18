import pickle

class Model:

    def __init__(self, file_name):
        self.__albom_lst = []
        self.__photo_lst = []
        self.load(file_name)

    def load(self, file_name):
        try:
            with open(file_name, 'rb') as f:
                self.__albom_lst, self.__photo_lst = pickle.load(f)
        except:
            self.__albom_lst = []
            self.__photo_lst = []


    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump([self.__albom_lst, self.__photo_lst], f)


    def delete_photo(self, key, value):
        self.__photo_lst = filter(lambda element: element['key'] != value, self.__photo_lst)

    def del_photo_rec(self, album_id, name):
        self.__photo_lst = filter(lambda x: x['albom_id'] != album_id and x['name'] != name, self.__photo_lst)

    def del_photo(self, id):
        self.__photo_lst = filter(lambda x: x['id'] != id, self.__photo_lst)


    def delete_albom(self, id):
        self.delete_photo('albom_id', id)
        self.__albom_lst = filter(lambda element: element['id'] != id, self.__albom_lst)


    def add_albom(self, name, autor):
        if self.__albom_lst == []:
            id = 0
        else:
            id = self.__albom_lst[-1]['id'] + 1

        self.__albom_lst.append({'id': id, 'name': name, 'autor': autor})


    def add_photo(self, name, format, cost, albom_id):
        is_albom_exist = filter(lambda element: element['id'] == albom_id, self.__albom_lst)
        if is_albom_exist == []:
            raise Exception('Incorrect albom_id.')

        if self.__photo_lst == []:
            id = 0
        else:
            id = self.__photo_lst[-1]['id'] + 1

        self.__photo_lst.append({'id': id, 'name': name, 'format': format, 'cost': cost, 'albom_id': albom_id})

    def photo_format(self, format):
        evening_sessions = filter(lambda element: str(element['format']) > format, self.__photo_lst)
        return [i for i in self.__albom_lst for j in self.__photo_lst if i['id'] == j['albom_id']]

    def is_exist(self, id, lst):
        item = filter(lambda x: x['id'] == id, lst)
        if item:
            return True
        return False

    def __find(self, id, lst):
        for item in lst:
            if item['id'] == id:
                return lst.index(item)

    def albom_update(self, id, key, value):
        indx = self.__find(id, self.__albom_lst)
        self.__albom_lst[indx][key] = value

    def photo_update(self, id, key, value):
        indx = self.__find(id, self.__session_lst)
        self.__photo_lst[indx][key] = value

    def get_albom(self):
        return self.__albom_lst

    def get_photo(self):
        return self.__photo_lst

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
