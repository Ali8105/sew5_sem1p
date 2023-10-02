"""
- ein Bash-Script2 mit allen notwendigen Schritten/Befehlen zum Erzeugen der Benutzer3
– ein Bash-Script zum Löschen der angelegten Benutzer
– eine Liste mit Usernamen und Passwörtern zum Verteilen an die unterrichtenden Lehrer
– ein Logfile mit sinnvollen Angaben
"""
from openpyxl import load_workbook

__author__ = "Ali Gurbuz"

wb = load_workbook(r"Ressources/Namen.xlsx", read_only=True)
ws = wb[wb.sheetnames[0]]
print(f"Worksheet names: {wb.sheetnames}")