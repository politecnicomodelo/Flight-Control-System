flight_list = []
people_list = []
plane_list = []

import os
from datetime import datetime
from classes import *

# touch files


def touch(path):
    """Given a path open that file."""
    with open(path, 'a'):
        os.utime(path, None)


def touch_files():
    """ Touch that files"""
    touch("flights")
    touch("people")
    touch("planes")


# reading the data of the txt files


def read_flights_txt():
    """ Read the txt flights, create a new_flight and append it to flights_list"""
    with open('flights', 'r') as the_file:
        l = []
        for line in the_file:
            l = line.split('|')

            new_flight = Flight()
            new_flight.assigned_plane = l[0]
            new_flight.date = datetime.datetime.strptime(l[1], "%d-%m-%Y").date()
            new_flight.where_to_where = tuple(l[2].split(','))
            new_flight.people_list = l[3].split(',')

            flights_list.append(new_flight)


def read_people_txt():
    """
    Given similar txt:
    <line1> Pilot|Rodrigo|Palacios|10-05-1955|12000000|A1,A2,A3
    <line2> FlightAttendant|Maria|Lalala|19-10-1975|44554255|A3,A4|English
    <line3> Passenger|Esteban|Perez|24-04-2011|55987541|1|Vegan
    select the first part: Passenger|Pilot|FlightAttendant and create an object of that.
    set the values depending on which type of object is
    """
    with open('people', 'r') as the_file:
        l = []
        for line in the_file:
            l = line.split('|')
            the_object = eval(l[0])  # transform the str (Passenger|Pilot|FlightAttendant) to a real object.

            new_person = the_object()  # create the object
            new_person.name = l[1]
            new_person.last_name = l[2]
            new_person.date_of_born = datetime.datetime.strptime(l[3], "%d-%m-%Y").date()
            new_person.dni = l[4]

            object_type = type(the_object)  # determine the type of that object: Passenger|Pilot|FlightAttendant
            if object_type is FlightAttendat:
                new_person.models_allowed_to_fly = l[5].split(',')
                new_person.languages_that_speak = l[6].split(',')

            elif object_type is Passenger:
                new_person.is_vip = bool(l[5])
                new_person.special_needs = l[6].split(',')

            elif object_type is Pilot:
                new_person.models_allowed_to_fly = l[5].split(',')

            people_list.append(new_person)


def read_all_txt():
    read_flights_txt()
    read_people_txt()