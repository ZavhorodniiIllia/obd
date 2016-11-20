class View:
    @staticmethod
    def data_base_menu():
        print 'Data base menu\n--------------'
        print 'Choose one of the following menu items:'
        print '1) Director menu'
        print '2) Film menu'
        print '3) Exit'

    @staticmethod
    def display(lst):
        for element in lst:
            print '\n'.join(map(lambda key: key + ' : ' + str(element[key]), element.keys()))
            print '\n'


    @staticmethod
    def director_menu():
        print 'Director menu'
        print '1) Add director\n2) Delete director\n3) Change\n4) Display Ukrainian film\n5) Display\n6) Back\n'

    @staticmethod
    def film_menu():
        print 'Film menu'
        print '1) Add film\n2) Delete film\n3) Change\n4) Display\n5) Back\n'

    @staticmethod
    def director_update_menu():
        print 'Director change menu'
        print '1) Name\n2) Film`s number\n3) Back\n'

    @staticmethod
    def film_update_menu():
        print 'Film change menu'
        print '1) Name\n2) Countyr\n3) Year\n4) Back\n'

    @staticmethod
    def success_message(message):
        print message + '\n'

    @staticmethod
    def error_message(message):
        print '[ERROR]: ' + message + '\n'
