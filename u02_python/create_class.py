"""
- ein Bash-Script2 mit allen notwendigen Schritten/Befehlen zum Erzeugen der Benutzer3
– ein Bash-Script zum Löschen der angelegten Benutzer
– eine Liste mit Usernamen und Passwörtern zum Verteilen an die unterrichtenden Lehrer
– ein Logfile mit sinnvollen Angaben
"""
from openpyxl import load_workbook

__author__ = "Ali Gurbuz"

workbook = load_workbook(r"Ressources/Namen.xlsx")
worksheet = workbook[workbook.sheetnames[0]]
for cell in worksheet["A"]:
    print(cell.value)