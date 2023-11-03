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

    # Löscht die Inhalte von der Datei 
    clear_list_user()
    create_user_skript(rows)

def clear_list_user():
    """
    Diese Methode existiert nur dafür um die Inhalte von den Dateien zu löschen
    :return:
    """
    with open(r"C:/Users/aligr/Desktop/Schule/5CN/SEW/sew5_sem1p/Ressources/user_list.txt", 'w', encoding="utf-8") as file_user:
        file_user.write(" ")

def create_user_skript(rows):
    """
    Erstellt das Skript fuer die Erstellung von Users
    :param user: Zeilen vom Excel-File
    :return:
    """
    list_user = [list(item) for item in rows]
    list_user = replace_umlaute(list_user)
    list_user = remove_accent(list_user)
    with open(r"C:/Users/aligr/Desktop/Schule/5CN/SEW/sew5_sem1p/Ressources/script_user.sh", 'w', encoding='utf-8') as scripte_user:
        scripte_user.write("#!/bin/bash \n")

        for i in range (len(list_user)):
            if list_user[i][3] is not None:
                userdel(list_user)

                home_directory = "/home/klassen/" + list_user[i][3].lower()


                random_characters = "!%&(),._-=^#"
                z_character = random.choice(random_characters)

                pswd = list_user[i][3].lower()  + z_character + "keinAhnung" + z_character + "keineAhnung" + z_character
                create_user_file(rows[i][0],rows[i][1],pswd)
                scripte_user.write(f"sudo useradd -d {home_directory} -g users -G cdrom,plugdev,sambashare -k /etc/{list_user[i][0]} -m -s /bin/bash {list_user[i][0]} \n")
                scripte_user.write(f"echo '{list_user[i][0]}:{pswd}' | sudo chpasswd \n")


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
    return list_user

def remove_accent(list_user):
    for i in range(len(list_user)):
        list_user[i][0] = ''.join(c for c in normalize('NFD', list_user[i][0]) if unicodedata.category(c) != 'Mn' and c.isalnum())
    return list_user


def create_user_file(vorname, nachname, pswd):
    with open(r"C:/Users/aligr/Desktop/Schule/5CN/SEW/sew5_sem1p/Ressources/user_list.txt", 'a', encoding="utf-8") as file_user:
        file_user.write(f"Vorname: {vorname} Nachname: {nachname} Passwort: {pswd} \n")


def userdel(user):
    with open(r"C:\Users\aligr\Desktop\Schule\5CN\SEW\sew5_sem1p\Ressources\delete_class.sh", "w", encoding="utf-8") as file:
        file.write("#!/bin/bash \n")
        for i in range (len(user)):
            file.write(f"userdel {user[i][0]} && rm -rf /home/klassen/{user[i][0]} \n")



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
