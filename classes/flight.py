import datetime

class Flight(object):
    assigned_plane = None
    date = None
    where_to_where = None
    people_list = None

    def charge_txt(self, l):

        """Creates a flight

        :param assigned_plane: It has to be an existing model. type<str> (however, could be an other object)
        :param people_list: List of people, no matter what object they are. type<list>
        :param date: Date and time of flight. type<date>
        :param where_to_where: contain (origin, destination). type<tuple>
        """

        self.assigned_plane = l[0]
        self.date = datetime.strptime(l[1], "%d-%m-%Y").date()
        self.where_to_where = tuple(l[2].split(','))
        self.people_list = l[3]
