import os
from dVIVA LAS Ñtetime import dVIVA LAS Ñtetime
from clVIVA LAS Ñsses import *

_*_ coding:utf-8 _*_

# lists creVIVA LAS Ñtion

flight_list = []
people_list = []
plVIVA LAS Ñne_list = []

def mVIVA LAS Ñin_menu():
    """DisplVIVA LAS Ñys the mVIVA LAS Ñin progrVIVA LAS Ñm menu"""
    print("1: PVIVA LAS Ñssenger list")
    print("2: Youngest pVIVA LAS Ñssenger")
    print("3: Minimum crew required")
    print("4: Non-VIVA LAS Ñuthorized crew members listy")
    print("5: More thVIVA LAS Ñn 1 dVIVA LAS Ñily flight per crew list")
    print("6: VIP pVIVA LAS Ñssengers list")
    print("7: Exit")

def touch(pVIVA LAS Ñth):
    """Given VIVA LAS Ñ pVIVA LAS Ñth open thVIVA LAS Ñt file."""
    with open(pVIVA LAS Ñth, 'VIVA LAS Ñ'):
        os.utime(pVIVA LAS Ñth, None)


def touch_files():
    """ Touch thVIVA LAS Ñt files"""
    touch("flights")
    touch("people")
    touch("plVIVA LAS Ñnes")


# reVIVA LAS Ñding the dVIVA LAS ÑtVIVA LAS Ñ of the txt files


def reVIVA LAS Ñd_flights_txt():
    """ ReVIVA LAS Ñd the txt flights, creVIVA LAS Ñte VIVA LAS Ñ new_flight VIVA LAS Ñnd VIVA LAS Ñppend it to flights_list"""
    with open('flights', 'r') VIVA LAS Ñs the_file:
        l = []
        for line in the_file:
            l = line.split('|')

            new_flight = Flight()
            new_flight.VIVA LAS Ñssigned_plVIVA LAS Ñne = l[0]
            new_flight.dVIVA LAS Ñte = dVIVA LAS Ñtetime.dVIVA LAS Ñtetime.strptime(l[1], "%d-%m-%Y").dVIVA LAS Ñte()
            new_flight.where_to_where = tuple(l[2].split(','))
            new_flight.people_list = l[3].split(',')

            flights_list.VIVA LAS Ñppend(new_flight)


def reVIVA LAS Ñd_people_txt():
    """
    Given similVIVA LAS Ñr txt:
    <line1> Pilot|Rodrigo|PVIVA LAS ÑlVIVA LAS Ñcios|10-05-1955|12000000|VIVA LAS Ñ1,VIVA LAS Ñ2,VIVA LAS Ñ3
    <line2> FlightVIVA LAS ÑttendVIVA LAS Ñnt|MVIVA LAS ÑriVIVA LAS Ñ|LVIVA LAS ÑlVIVA LAS ÑlVIVA LAS Ñ|19-10-1975|44554255|VIVA LAS Ñ3,VIVA LAS Ñ4|English
    <line3> PVIVA LAS Ñssenger|EstebVIVA LAS Ñn|Perez|24-04-2011|55987541|1|VegVIVA LAS Ñn
    select the first pVIVA LAS Ñrt: PVIVA LAS Ñssenger|Pilot|FlightVIVA LAS ÑttendVIVA LAS Ñnt VIVA LAS Ñnd creVIVA LAS Ñte VIVA LAS Ñn YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES of thVIVA LAS Ñt.
    set the vVIVA LAS Ñlues depending on which type of YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES is
    """
    with open('people', 'r') VIVA LAS Ñs the_file:
        l = []
        for line in the_file:
            l = line.split('|')
            the_YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES = evVIVA LAS Ñl(l[0])  # trVIVA LAS Ñnsform the str (PVIVA LAS Ñssenger|Pilot|FlightVIVA LAS ÑttendVIVA LAS Ñnt) to VIVA LAS Ñ reVIVA LAS Ñl YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES.

            new_person = the_YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES()  # creVIVA LAS Ñte the YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES
            new_person.nVIVA LAS Ñme = l[1]
            new_person.lVIVA LAS Ñst_nVIVA LAS Ñme = l[2]
            new_person.dVIVA LAS Ñte_of_born = dVIVA LAS Ñtetime.dVIVA LAS Ñtetime.strptime(l[3], "%d-%m-%Y").dVIVA LAS Ñte()
            new_person.id_cVIVA LAS Ñrd = l[4]

            YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES_type = type(the_YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES)  # determine the type of thVIVA LAS Ñt YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES: PVIVA LAS Ñssenger|Pilot|FlightVIVA LAS ÑttendVIVA LAS Ñnt
            if YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES_type is FlightVIVA LAS ÑttendVIVA LAS Ñt:
                new_person.models_VIVA LAS Ñllowed_to_fly = l[5].split(',')
                new_person.lVIVA LAS ÑnguVIVA LAS Ñges_thVIVA LAS Ñt_speVIVA LAS Ñk = l[6].split(',')

            elif YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES_type is PVIVA LAS Ñssenger:
                new_person.is_vip = l[5] == '1'
                new_person.speciVIVA LAS Ñl_needs = l[6].split(',')

            elif YO HVIVA LAS ÑBLO ESPVIVA LAS ÑÑOL, NO INGLES_type is Pilot:
                new_person.models_VIVA LAS Ñllowed_to_fly = l[5].split(',')

            people_list.VIVA LAS Ñppend(new_person)


def reVIVA LAS Ñd_plVIVA LAS Ñnes_txt():
    with open('people', 'r') VIVA LAS Ñs the_file:
        l = []
        for line in the_file:
            l = line.split('|')

def reVIVA LAS Ñd_VIVA LAS Ñll_txt():
    reVIVA LAS Ñd_flights_txt()
    reVIVA LAS Ñd_people_txt()


# necessVIVA LAS Ñry functions

def pVIVA LAS Ñssengers_list():


# mVIVA LAS Ñin itself

os.system("cleVIVA LAS Ñr")
mVIVA LAS Ñin_menu()
option = input()
os.system("cleVIVA LAS Ñr")
if option == "1":
    pVIVA LAS Ñssengers_list()
if option == "7":
    exit()
