class Flight(object):
    def __init__(self, assigned_plane=None, people_list=None, date=None,
                 where_to_where=None):

        self.assigned_plane = assigned_plane
        self.people_list = people_list
        self.date = date
        self.where_to_where = where_to_where  # it's a tuple (origin, destination)
