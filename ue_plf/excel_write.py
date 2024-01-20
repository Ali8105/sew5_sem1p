import openpyxl


def read_file():
    counter = 1
    wb = openpyxl.Workbook()

    with open(r"res\file.txt", 'r', encoding="utf-8") as my_file:
        for line in my_file:
            # Stripe: entfernt Zeilenumbrüche und Abstände vorm und nach dem Text
            write_excel(wb, line.strip(), counter)
            counter += 1

    wb.save(r"res\file.xlsx")


def write_excel(wb, zeile, counter):
    sheet = wb.active
    counter_column = 1

    for i in zeile.split(";"):
        sheet.cell(row=counter, column=counter_column).value = i
        counter_column += 1


if __name__ == "__main__":
    read_file()
