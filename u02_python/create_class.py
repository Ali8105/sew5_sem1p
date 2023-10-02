"""
- ein Bash-Script2 mit allen notwendigen Schritten/Befehlen zum Erzeugen der Benutzer3
– ein Bash-Script zum Löschen der angelegten Benutzer
– eine Liste mit Usernamen und Passwörtern zum Verteilen an die unterrichtenden Lehrer
– ein Logfile mit sinnvollen Angaben
"""
from openpyxl import load_workbook

__author__ = "Ali Gurbuz"

def read_excel_file():
    workbook = load_workbook(r"../Ressources/Namen.xlsx", read_only=True)
    worksheet = workbook[workbook.sheetnames[0]]

    for row in worksheet.iter_rows(values_only=True):
        yield row


def remove_accent(user):
    print(user[0])
    
for i in read_excel_file():
    remove_accent(i)
