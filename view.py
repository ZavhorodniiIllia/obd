class View:
    @staticmethod
    def data_base_menu():
        print 'Data base menu\n--------------'
        print 'Choose one of the following items:'
        print '1) Albom menu'
        print '2) Photo menu'
        print '3) Exit'

    @staticmethod
    def display(lst):
        for element in lst:
            print '\n'.join(map(lambda key: key + ' : ' + str(element[key]), element.keys()))
            print '\n'


    @staticmethod
    def albom_menu():
        print 'Albom menu'
        print '1) Add albom\n2) Delete albom\n3) Update\n4) Display albom with  photo_name.BMP\n5) Display\n6) Back\n'

    @staticmethod
    def photo_menu():
        print 'Photo menu'
        print '1) Add photo\n2) Delete photo\n3) Update\n4) Display\n5) Back\n'

    @staticmethod
    def albom_update_menu():
        print 'Albom update menu'
        print '1) Name\n2) Autor\n3) Back\n'

    @staticmethod
    def photo_update_menu():
        print 'Photo update menu'
        print '1) Name\n2) Time\n3) Cost\n4) Back\n'

    @staticmethod
    def success_message(message):
        print message + '\n'

    @staticmethod
    def error_message(message):
        print '[ERROR]: ' + message + '\n'
