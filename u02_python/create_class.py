"""
- ein Bash-Script2 mit allen notwendigen Schritten/Befehlen zum Erzeugen der Benutzer3
– ein Bash-Script zum Löschen der angelegten Benutzer
– eine Liste mit Usernamen und Passwörtern zum Verteilen an die unterrichtenden Lehrer
– ein Logfile mit sinnvollen Angaben
"""
import os
import random
import unicodedata
import logging
from logging.handlers import RotatingFileHandler

from openpyxl import load_workbook
from unicodedata import normalize
import sys
import argparse
import numpy

__author__ = "Ali Gurbuz"

def generate_scripts():
    with open(r"C:\Users\aligr\Desktop\Schule\5CN\SEW\sew5_sem1p\Ressources\create_class.sh", "w") as file:
        logger.debug("opened file " + file.name)
        print("set -e", file=file)
    with open("res/delete_class.sh", "w") as file:
        logger.debug("opened file " + file.name)
        print("set -x", file=file)
    open("res/passwords_class", "w").close()
    create_user_entry(("lehrer",), ''.join(random.choice(string.ascii_letters) for _ in range(10)))
    create_user_entry(("seminar",), ''.join(random.choice(string.ascii_letters) for _ in range(10)))
    for user in get_user():
        pw = generate_password(user)
        create_user_entry(user, pw)


def create_user_entry(user, pwd)
    useradd(user, pwd)
    userdel(user)
    addpasswd(user, pwd)


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

    parser = argparse.ArgumentParser()
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    output_group.add_argument("-q", "--quiet", help="decrease output verbosity", action="store_true")
    parser.add_argument("file", help="file with the userdata")
    args = parser.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter("%(asctime)s; %(levelname)s; %(message)s",
                                  "%Y-%m-%d %H:%M:%S")

    rotating_file_handler = RotatingFileHandler("res/create_class.log", maxBytes=10000, backupCount=5)
    rotating_file_handler.setFormatter(formatter)
    logger.addHandler(rotating_file_handler)

    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if args.verbose:
        stream_handler.setLevel(logging.DEBUG)
    elif args.quiet:
        stream_handler.setLevel(logging.CRITICAL)
    else:
        stream_handler.setLevel(logging.INFO)

    try:
        wb = load_workbook(args.file, read_only=True)
        ws = wb[wb.sheetnames[0]]
        generate_scripts()
    except FileNotFoundError:
        logger.critical("couldnt find file")



