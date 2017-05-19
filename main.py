import os
from datetime import datetime
from classes import *

airline = Airline()

def main_menu():
    """Displays the main program menu"""
    print("1: Passenger list")
    print("2: Youngest passenger")
    print("3: Minimum crew required")
    print("4: Non-authorized crew members listy")
    print("5: More than 1 daily flight per crew list")
    print("6: VIP passengers list")
    print("7: Exit")


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
            line.rstrip('\n')
            l = line.split('|')
            new_flight = Flight()
            l[3] = airline.search_person(l[3].split(','))
            new_flight.charge_txt(l)
            airline.add_flight(new_flight)


def read_people_txt():
    """
    Given similar txt:
    <line1> Pilot|Name|Last Name|10-05-1955|12000000|A1,A2,A3
    <line2> FlightAttendant|Name|Last Name|19-10-1975|44554255|A3,A4|English
    <line3> Passenger|Name|Last Name|24-04-2011|55987541|1|Vegan
    select the first part: Passenger|Pilot|FlightAttendant and create an object of that.
    set the values depending on which type of object is
    """
    with open('people', 'r') as the_file:
        l = []
        for line in the_file:
            line.rstrip('\n')
            l = line.split('|')

            the_object = eval(l[0])  # transform the str (Passenger|Pilot|FlightAttendant) to a real object.
            new_person = the_object()  # create the object
            if new_person is not Passenger:
                l[5] = airline.search_plane(l[5].split(','))
            new_person.charge_txt(l)
            airline.add_person(new_person)


def read_planes_txt():
    """
    Given similar txt:
    <line> Model|Passenger capacity|Minimum crew required
    """

    with open('planes', 'r') as the_file:
        l = []
        for line in the_file:
            line.rstrip('\n')
            l = line.split('|')
            new_plane = Plane()
            new_plane.charge_txt(l)
            airline.add_plane(new_plane)


def read_all_txt():
    read_flights_txt()
    read_people_txt()
    read_planes_txt()
