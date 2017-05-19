class Flight(object):
    def __init__(self, assigned_plane=None, date=None, where_to_where=None,
                 people_list=None):

        """Creates a flight


        :param assigned_plane: It has to be an existing model. type<str> (however, could be an other object)
        :param people_list: List of people, no matter what object they are. type<list>
        :param date: Date and time of flight. type<date>
        :param where_to_where: contain (origin, destination). type<tuple>
        """

        self.assigned_plane = assigned_plane
        self.date = date
        self.where_to_where = where_to_where
        self.people_list = people_list
