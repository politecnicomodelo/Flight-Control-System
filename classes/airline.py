class Airline(object):

    def __init__(self):
        self.flight_list = []
        self.people_list = []
        self.plane_list = []

    def search_plane(self, str):
        for model in self.plane_list:
            if model.plane_model == str:
                return model

    def search_planes(self, list_str):
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

    def unrequired_crew(self):
        flights = []
        for flight in self.flight_list:
            if len(flight.crew_list) < flight.assigned_plane.crew_required:
                flights.append(flight)
        return flights

    def unable_crew(self):
        flights = []
        for flight in self.flight_list:
            for crew in flight.crew_list:
                if flight.assigned_plane not in crew.models_allowed_to_fly and flight not in flights:
                    flights.append(flight)
        return flights

    def tired_crew(self):
        crew_tired = []
        for flight in self.flight_list:
            for flight2 in self.flight_list:
                if flight.date == flight2.date:
                    for crew in flight.crew_list:
                        for crew2 in flight2.crew_list:
                            if crew == crew2 and crew not in crew_tired:
                                crew_tired.append(crew)
        return crew_tired


    def add_person(self, person):
        self.people_list.append(person)

    def add_flight(self, flight):
        self.flight_list.append(flight)

    def add_plane(self, plane):
        self.plane_list.append(plane)
