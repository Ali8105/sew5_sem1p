"""
- ein Bash-Script2 mit allen notwendigen Schritten/Befehlen zum Erzeugen der Benutzer3
– ein Bash-Script zum Löschen der angelegten Benutzer
– eine Liste mit Usernamen und Passwörtern zum Verteilen an die unterrichtenden Lehrer
– ein Logfile mit sinnvollen Angaben
"""
import os
import random
import unicodedata

from openpyxl import load_workbook
from unicodedata import normalize
import sys
import argparse
import numpy

__author__ = "Ali Gurbuz"

def read_excel_file(file):
    """

    :param file: Path zum File
    :return:
    """
    workbook = load_workbook(file, read_only=True)
    worksheet = workbook[workbook.sheetnames[0]]
    rows = list()
    first_row = True
    for row in worksheet.iter_rows(values_only=True):
        if first_row:
            first_row = False
            continue
        rows.append(row)
    # Tupples die in der Liste drinnen waren wurden zur liste umgewandelt --> damit man später die Werte bearbeiten kann
    list_users = [list(item) for item in rows]
    replace_umlaute(list_users)


def create_user_skript(list_user):
    """
    Erstellt das Skript fuer die Erstellung von Users
    :param user: Zeilen vom Excel-File
    :return:
    """

    with open(r"C:/Users/aligr/Desktop/Schule/5CN/SEW/sew5_sem1p/Ressources/script_user.sh", 'w', encoding='utf-8') as scripte_user:
        scripte_user.write("#!/bin/bash")

        for user in list_user:
            if user[3] is not None:
                scripte_user.write("\n")
                home_directory = "/home/klassen/k" + user[3].lower()
                # Define the set of characters for Z and R
                z_and_r_characters = "!%&(),._-=^#"

                # Generate Z and R characters randomly
                z_character = random.choice(z_and_r_characters)

                pswd = user[3].lower()  + z_character + "keinAhnung" + z_character + "keineAhnung" + z_character
                scripte_user.write(f"sudo useradd -d {home_directory} -g users -G cdrom,plugdev,sambashare -k /etc/{user[0]} -m -s /bin/bash {user[0]} \n")
                scripte_user.write(f"echo '{user[0]}:{pswd}' | sudo chpasswd")


def replace_umlaute(list_user):
    for i in range(len(list_user)):
        list_user[i][0] = list_user[i][0].replace('ä', 'ae')
        list_user[i][0] = list_user[i][0].replace('ö', 'oe')
        list_user[i][0] = list_user[i][0].replace('ü', 'ue')
        list_user[i][0] = list_user[i][0].replace('ß', 'ss')

        list_user[i][0] = list_user[i][0].replace('Ä', 'AE')
        list_user[i][0] = list_user[i][0].replace('Ö', 'OE')
        list_user[i][0] = list_user[i][0].replace('Ü', 'UE')
        list_user[i][0] = list_user[i][0].replace(' ', '_')
        list_user[i][0] = list_user[i][0].replace('\'', ('_'))
    remove_accent(list_user)


def remove_accent(list_user):
    for i in range(len(list_user)):
        list_user[i][0] = ''.join(c for c in normalize('NFD', list_user[i][0]) if unicodedata.category(c) != 'Mn' and c.isalnum())
    create_user_skript(list_user)




def username(list_user):
    for user in list_user:
        print(user)

def create_user_file(list_user):
    # damit die einträge vom letzten mal weggehen
    with open(r"C:/Users/aligr/Desktop/Schule/5CN/SEW/sew5_sem1p/Ressources/user_list.txt", 'w') as file_user:
        file_user.write("")
        pass

    # damit Append
    with open(r"C:/Users/aligr/Desktop/Schule/5CN/SEW/sew5_sem1p/Ressources/user_list.txt", 'a') as file_user:
       # print(list_user)
        file_user.flush()
        file_user.write(list_user)
        file_user.write('\n')


def parse_command_line_arguments():

    parser = argparse.ArgumentParser(description="Create Bash Scripts")

    parser.add_argument("dateiname", help="Der Name der Eingabedatei")

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Mehr Log-Ausgaben aktivieren"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Weniger Log-Ausgaben aktivieren"
    )

    args = parser.parse_args()

    eingabedatei = args.dateiname

    loglevel = "INFO"  # Standard-Loglevel
    if args.verbose:
        loglevel = "DEBUG"
    elif args.quiet:
        loglevel = "ERROR"

    print(f"Loglevel: {loglevel}")
    read_excel_file(eingabedatei)



parse_command_line_arguments()
