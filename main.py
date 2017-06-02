import os
from classes import *

airline = Airline()


# reading the data of the txt files


def read_flights_txt():
    """ Read the txt flights, create a new_flight and append it to flights_list"""
    with open('flights', 'r') as the_file:
        l = []
        for line in the_file:
            line = line.rstrip('\n')
            l = line.split('|')
            new_flight = Flight()
            l[0] = airline.search_plane(l[0])
            l[4] = airline.search_person(l[4].split(','))
            l[5] = airline.search_person(l[5].split(','))
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
            line = line.rstrip('\n')
            l = line.split('|')

            the_object = eval(l[0])  # transform the str (Passenger|Pilot|FlightAttendant) to a real object.
            new_person = the_object()  # create the object
            if type(new_person) is not Passenger:
                l[5] = airline.search_planes(l[5].rstrip('\n').split(','))  # extracted the '\n' and split it
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
            line = line.rstrip('\n')
            l = line.split('|')
            new_plane = Plane()
            new_plane.charge_txt(l)
            airline.add_plane(new_plane)


def read_all_txt():
    read_people_txt()
    read_planes_txt()
    read_flights_txt()


def ask_flight():
    os.system('clear')
    origin = input('Insert the origin: ').title()
    destination = input('Insert the destination: ').title()
    os.system('clear')
    return origin, destination


def show_passengers(list):
    print_table_head()
    for item in list:
        text = [item.name, item.last_name, str(item.date_of_born), item.dni]
        print('{: <20} | {: <20} | {: <20} | {: <11} |'.format(*text))
    print_any_key()


def print_any_key():
    print('\n')
    print('Press enter to continue...')
    input()


def show_special_passengers(list):
    text = ['   Name ', '    Last Name', '    Date of Born ', '     Dni    ', '      Is vip? ',
            '      Special_needs           ']
    print('\x1b[2;30;41m {: <19} | {: <20} | {: <20} | {: <20} | {: <20} | {: <10} | \x1b[0m'.format(*text))
    for item in list:
        if item.special_needs[0] is not None:
            needs = ", ".join(item.special_needs)
        else:
            needs = "Does not have special needs"
        text = [item.name, item.last_name, str(item.date_of_born), item.dni, item.is_vip, needs]
        print('{: <20} | {: <20} | {: <20} | {: <20} | {: <20} | {: <30} |'.format(*text))
    print_any_key()


def show_vip_and_special(origin, destination):
    flight_ = airline.search_flight((origin, destination))
    passengers_list = []
    for item in flight_.passenger_list:
        if item.is_vip or item.special_needs[0] is not None:
            passengers_list.append(item)
    return passengers_list


def passengers_per_flight(origin, destination):
    flight_ = airline.search_flight((origin, destination))
    while not flight_:
        print('Wrong option selection. Enter any key to try again...')
        input()
        os.system('clear')
    show_passengers(flight_.passenger_list)


def print_table_head():
    text = ['   Name ', '    Last Name', '    Date of Born ', '    Dni    ']
    print('\x1b[2;30;41m {: <19} | {: <20} | {: <20} | {: <1} | \x1b[0m'.format(*text))


def print_flight_table_head():
    text = ['   Origin ', '    Destination', '    Flight Date ', '    Hour   ']
    print('\x1b[2;30;41m {: <19} | {: <20} | {: <20} | {: <1} | \x1b[0m'.format(*text))


def youngest_passenger(origin, destination):
    flight_ = airline.search_flight((origin, destination))
    ages = []
    for item in flight_.passenger_list:
        ages.append(item.date_of_born)
    youngest_date = max(ages)
    print_table_head()
    for item in flight_.passenger_list:
        if item.date_of_born == youngest_date:
            text = [item.name, item.last_name, str(item.date_of_born), item.dni]
            print('{: <20} | {: <20} | {: <20} | {: <11} |'.format(*text))
    print_any_key()


def minimum_crew():
    list = airline.unrequired_crew()
    os.system('clear')
    print_flight_table_head()
    for item in list:
        text = [item.where_to_where[0], item.where_to_where[1], str(item.date), item.hour]
        print('{: <20} | {: <20} | {: <20} | {: <11} |'.format(*text))
    print_any_key()


def wrong_flights():
    list = airline.unable_crew()
    os.system('clear')
    print_flight_table_head()
    for item in list:
        text = [item.where_to_where[0], item.where_to_where[1], str(item.date), item.hour]
        print('{: <20} | {: <20} | {: <20} | {: <11} |'.format(*text))
    print_any_key()


def print_welcome():
    print("""
         _________________________          _____
        |                         \          \ U \__      _____
        | WELCOME TO OUR AIRLINE   \__________\   \/_______\___\_____________
        |        YEAAAAAH          /          < /_/   .....................  `-.
        |_________________________/            `-----------,----,--------------'
                                                         _/____/
    """)


def main_menu():
    """Displays the main program menu"""
    print(30 * '-', "MENU", 30 * '-')
    print("""

    1............................ Passenger list
    2........................ Youngest passenger
    3..................... Minimum crew required
    4.......... Non-authorized crew members list
    5.... More than 1 daily flight per crew list
    6....................... VIP passengers list
    7...................................... Exit

    """)
    print(67 * '-')

    return input()


def main():
    os.system('clear')
    print_welcome()
    option = main_menu()
    if option == '1':
        origin, destination = ask_flight()
        passengers_per_flight(origin, destination)
    elif option == '2':
        origin, destination = ask_flight()
        youngest_passenger(origin, destination)
    elif option == '3':
        minimum_crew()
    elif option == '4':
        wrong_flights()
    elif option == '5':
        os.system('clear')
        show_passengers(airline.tired_crew())
    elif option == '6':
        origin, destination = ask_flight()
        list = show_vip_and_special(origin, destination)
        show_special_passengers(list)
    elif option == '7':
        exit()
    else:
        print('Wrong option selection. Enter any key to try again...')
        input()
        os.system('clear')

# main itself

if __name__ == '__main__':
    read_all_txt()
    while True:
        print_welcome()
        main()
