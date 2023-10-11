"""
- ein Bash-Script2 mit allen notwendigen Schritten/Befehlen zum Erzeugen der Benutzer3
– ein Bash-Script zum Löschen der angelegten Benutzer
– eine Liste mit Usernamen und Passwörtern zum Verteilen an die unterrichtenden Lehrer
– ein Logfile mit sinnvollen Angaben
"""
import os
import unicodedata

from openpyxl import load_workbook
from unicodedata import normalize
import sys
import argparse

__author__ = "Ali Gurbuz"

def read_excel_file(file):
    """

    :param file: Path zum File
    :return:
    """
    workbook = load_workbook(file, read_only=True)
    worksheet = workbook[workbook.sheetnames[0]]
    for row in worksheet.iter_rows(values_only=True):
        replace_umlaute(row)


def create_user_skript(list_user):
    """
    Erstellt das Skript fuer die Erstellung von Users
    :param user: Zeilen vom Excel-File
    :return:
    """

    with open(r"C:/Users/aligr/Desktop/Schule/5CN/SEW/sew5_sem1p/Ressources/script_user.sh", 'a') as scripte_user:
       # print(list_user)
        scripte_user.flush()
       
        scripte_user.write(list_user)
        scripte_user.write('\n')

    


def remove_accent(user):
    list_user = list(user)
    # list_user[0] = normalize('NFKD', list_user[0]).encode('ASCII','ignore').decode('utf-8')
    # list_user[0] = normalize('NFD', list_user[0]).encode('ASCII','ignore').decode('utf-8')
    list_user[0] = ''.join(c for c in normalize('NFD', list_user[0]) if unicodedata.category(c) != 'Mn' and c.isalnum())
    # normalized_text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    print(list_user[0])

def replace_umlaute(list_user):
    list_user = list(list_user)
    list_user[0] = list_user[0].replace('ä', 'ae')
    list_user[0] = list_user[0].replace('ö', 'oe')
    list_user[0] = list_user[0].replace('ü', 'ue')
    list_user[0] = list_user[0].replace('ß', 'ss')

    list_user[0] = list_user[0].replace('Ä', 'AE')
    list_user[0] = list_user[0].replace('Ö', 'OE')
    list_user[0] = list_user[0].replace('Ü', 'UE')
    list_user[0] = list_user[0].replace(' ', '_')
    list_user[0] = list_user[0].replace('\'', ('_'))
    remove_accent(list_user)



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
