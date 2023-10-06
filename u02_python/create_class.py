"""
- ein Bash-Script2 mit allen notwendigen Schritten/Befehlen zum Erzeugen der Benutzer3
– ein Bash-Script zum Löschen der angelegten Benutzer
– eine Liste mit Usernamen und Passwörtern zum Verteilen an die unterrichtenden Lehrer
– ein Logfile mit sinnvollen Angaben
"""
from openpyxl import load_workbook
from unicodedata import normalize
import sys
import argparse

__author__ = "Ali Gurbuz"

def read_excel_file(file):
    workbook = load_workbook(file, read_only=True)
    worksheet = workbook[workbook.sheetnames[0]]

    for row in worksheet.iter_rows(values_only=True):
        print(row[0], row[1], row[2])


def create_user_skript(user):
    """
    Erstellt das Skript fuer die Erstellung von Users
    :param user: Zeilen vom Excel-File
    :return:
    """
    


def remove_accent(user):
    list_user = list(user)
    list_user[0] = normalize('NFC', list_user[0])
    replace_umlaute(list_user)

def replace_umlaute(user):

    user[0] = user[0].replace('ä','ae')
    user[0] = user[0].replace('ö', 'oe')
    user[0] = user[0].replace('ü', 'ue')
    user[0] = user[0].replace('ß','ss')

    user[0] = user[0].replace('Ä','AE')
    user[0] = user[0].replace('Ö', 'OE')
    user[0] = user[0].replace('Ü', 'UE')
    user[0] = user[0].replace(' ','_')
    print(user)

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
