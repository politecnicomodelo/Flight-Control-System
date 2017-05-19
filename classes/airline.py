class Airline(object):

    def __init__(self):
        self.flight_list = []
        self.people_list = []
        self.plane_list = []

    def search_plane(self, list_str):
        final_list = []
        for item in list_str:
            for model in self.plane_list:
                if model.plane_model == item:
                    final_list.append(model)
        return final_list

    def search_person(self, list_str):
        final_list = []
        for item in list_str:
            for person in self.people_list:
                if person.dni == item:
                    final_list.append(person)
        return final_list

    def search_flight(self, od):
        for item in self.flight_list:
            if item.where_to_where[0] == od[0] and item.where_to_where[1] == od[1]:
                return item

    def add_person(self, person):
        self.people_list.append(person)

    def add_flight(self, flight):
        self.flight_list.append(flight)

    def add_plane(self, plane):
        self.plane_list.append(plane)