from view import View
from model import Model

class Controller:

    def __init__(self, data_base):
        self.model = data_base

    def __albom_controller(self):
        choice = -1
        while choice != 6:
            View.albom_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                name = raw_input('Enter albom name:\n')
                autor = raw_input('Enter autor:\n')
                self.model.add_albom(name, autor)
                View.success_message('Item successfuly added!!!')
            elif choice == 2:
                try:
                    id = int(raw_input('Enter id:\n'))
                except ValueError:
                    View.error_message('Incorrect value\n')

                if not  self.model.is_exist(id, self.model.get_albom()):
                    View.error_message('Incorrect id')
                    return

                self.model.delete_albom(id)
                View.success_message('Item successfuly deleted!!!')

            elif choice == 3:
                self.__albom_update_controller()

            elif choice == 4:
                View.display(self.model.photo_format('bmp'))

            elif choice == 5:
                View.display(self.model.get_albom())

        raw_input('Press -->Enter...\n')

    def __photo_controller(self):
        choice = -1
        while choice != 5:
            View.photo_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                try:
                    name = raw_input('Enter photo name:\n')
                    format = str(raw_input('Enter photo format:\n'))
                    albom_id = int(raw_input('Enter albom_id:\n'))
                    cost = raw_input('Enter cost:\n')
                    self.model.add_photo(name, format, cost, albom_id)
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

                if not self.model.is_exist(id, self.model.get_photo()):
                    View.error_message('Incorrect id')
                    return

                self.model.del_photo(id)
                View.success_message('Item successfuly deleted!!!')

            elif choice == 3:
                self.__photo_update_controller()

            elif choice == 4:
                View.display(self.model.get_photo())

        raw_input('Press -->Enter...\n')

    def __albom_update_controller(self):
        choice = -1
        try:
            id = int(raw_input('Enter id:\n'))
        except ValueError:
            View.error_message('Incorrect value')

        if  not self.model.is_exist(id, self.model.get_albom()):
            View.error_message('Incorrect id')
            return

        while choice != 3:
            View.albom_update_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                name = raw_input('Enter new albom name:\n')
                self.model.albom_update(id, 'name', name)
                View.success_message('Item successfuly updated!!!')

            elif choice == 2:
                autor = raw_input('Enter new autor:\n')
                self.model.albom_update(id, 'autor', autor)
                View.success_message('Item successfuly updated!!!')

            raw_input('Press -->Enter...\n')

    def __photo_update_controller(self):
        choice = -1
        try:
            id = int(raw_input('Enter id:\n'))
        except ValueError:
            View.error_message('Incorrect value')

        if  not self.model.is_exist(id, self.model.get_photo()):
            View.error_message('Incorrect id')
            return

        while choice != 4:
            View.photo_update_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                name = raw_input('Enter new photo name:\n')
                self.model.photo_update(id, 'name', name)
                View.success_message('Item successfuly updated!!!')

            elif choice == 2:
                try:
                    time = raw_input('Enter format:\n')
                    self.model.photo_update(id, 'format', format)
                    View.success_message('Item successfuly updated!!!')
                except Exception as e:
                    View.error_message(e.message)

            elif choice == 3:
                try:
                    cost = float(raw_input('Enter cost:\n'))
                    self.model.photo_update(id, 'cost', cost)
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
                self.__albom_controller()

            elif choice == 2:
                self.__photo_controller()

        raw_input('Press -->Enter...')
        self.model.save('data.txt')
