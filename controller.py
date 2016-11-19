from view import View
from model import Model

class Controller:

    def __init__(self, data_base):
        self.model = data_base

    def __director_controller(self):
        choice = -1
        while choice != 6:
            View.director_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                name = raw_input('Enter director name:\n')
                filmsnumber = raw_input('Enter films`n umber:\n')
                self.model.add_director(name, filmsnumber)
                View.success_message('Item successfuly added!!!')
            elif choice == 2:
                try:
                    id = int(raw_input('Enter id:\n'))
                except ValueError:
                    View.error_message('Incorrect value\n')

                if not  self.model.is_exist(id, self.model.get_director()):
                    View.error_message('Incorrect id')
                    return

                self.model.delete_director(id)
                View.success_message('Item successfuly deleted!!!')

            elif choice == 3:
                self.__director_update_controller()

            elif choice == 4:
                View.display(self.model.film_country('Ukraine'))

            elif choice == 5:
                View.display(self.model.get_director())

        raw_input('Press -->Enter...\n')

    def __film_controller(self):
        choice = -1
        while choice != 5:
            View.film_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                try:
                    name = raw_input('Enter film name:\n')
                    country = str(raw_input('Enter film`s country:\n'))
                    director_id = int(raw_input('Enter director id:\n'))
                    year = raw_input('Enter year:\n')
                    self.model.add_film(name, country, year, director_id)
                    View.success_message('Item successfuly added!!!')
                except ValueError:
                    View.error_message('Incorrect value')
                except Exception as e:
                    View.error_message(e.message)

            elif choice == 2:
                try:
                    id = int(raw_input('Enter id:\n'))
                except ValueError:
                    View.error_message('Incorrect value')

                if not self.model.is_exist(id, self.model.get_film()):
                    View.error_message('Incorrect id')
                    return

                self.model.del_film(id)
                View.success_message('Item successfuly deleted!!!')

            elif choice == 3:
                self.__film_update_controller()

            elif choice == 4:
                View.display(self.model.get_film())

        raw_input('Press -->Enter...\n')

    def __director_update_controller(self):
        choice = -1
        try:
            id = int(raw_input('Enter id:\n'))
        except ValueError:
            View.error_message('Incorrect value')

        if  not self.model.is_exist(id, self.model.get_director()):
            View.error_message('Incorrect id')
            return

        while choice != 3:
            View.director_update_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                name = raw_input('Enter new director name:\n')
                self.model.director_update(id, 'name', name)
                View.success_message('Item successfuly updated!!!')

            elif choice == 2:
                filmsnumber = raw_input('Enter new films`n umber:\n')
                self.model.director_update(id, 'filmsnumber', filmsnumber)
                View.success_message('Item successfuly updated!!!')

            raw_input('Press -->Enter...\n')

    def __film_update_controller(self):
        choice = -1
        try:
            id = int(raw_input('Enter id:\n'))
        except ValueError:
            View.error_message('Incorrect value')

        if  not self.model.is_exist(id, self.model.get_film()):
            View.error_message('Incorrect id')
            return

        while choice != 4:
            View.film_update_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                name = raw_input('Enter new film name:\n')
                self.model.film_update(id, 'name', name)
                View.success_message('Item successfuly updated!!!')

            elif choice == 2:
                try:
                    time = raw_input('Enter country:\n')
                    self.model.film_update(id, 'country', country)
                    View.success_message('Item successfuly updated!!!')
                except Exception as e:
                    View.error_message(e.message)

            elif choice == 3:
                try:
                    year = float(raw_input('Enter year:\n'))
                    self.model.film_update(id, 'year', year)
                    View.success_message('Item successfuly updated!!!')
                except ValueError:
                    View.error_message('Incorrect value')

            raw_input('Press -->Enter...\n')

    def run(self):
        choice = -1
        while choice != 3:
            View.data_base_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                self.__director_controller()

            elif choice == 2:
                self.__film_controller()

        raw_input('Press -->Enter...')
        self.model.save('data.txt')
