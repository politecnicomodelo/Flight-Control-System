from datetime import datetime


class Person(object):

    def __init__(self, name=None, last_name=None, dni=None, date_of_born=None):
        self.name = name
        self.last_name = last_name
        self.date_of_born = date_of_born
        self.dni = dni

    def charge_txt(self, l):
        self.name = l[1]
        self.last_name = l[2]
        self.date_of_born = datetime.strptime(l[3], "%d-%m-%Y").date()
        self.dni = l[4]
