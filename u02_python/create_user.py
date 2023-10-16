import argparse
import logging
import unicodedata
from collections import namedtuple
from logging.handlers import RotatingFileHandler

from openpyxl import load_workbook

def generate_scripts():
    with open("res/create_user.sh", "w") as file:
        logger.debug("opened file " + file.name)
        print("set -e", file=file)
    with open("res/delete_user.sh", "w") as file:
        logger.debug("opened file " + file.name)
        print("set -x", file=file)
    open("res/passwords_user", "w").close()
    users = dict()


def remove_accent(txt):
    norm_txt = unicodedata.normalize('NFD',txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    erg = unicodedata.normalize('NFC', shaved)
    return erg


def get_user():
    User = namedtuple("User", "vmnam nname group u_class login_name")
    for row in ws.iter_rows(min_row=2):
        print("sd")


def useradd(user, pwd):
    return 0

def userdel(user):
    return 0

def addpasswd(user, pwd):
    return 0



if '__main__' == __name__:
    parser = argparse.ArgumentParser()
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    output_group.add_argument("-q", "--quiet", help="decrease output verbosity", action="store_true")
    parser.add_argument("file", help="file with the userdata")
    args = parser.parse_args()

    logger = logging.Logger()

    formatter = logging.Formatter("%(asctime)s; %(levelname)s; %(message)s",
                                  "%Y-%m-%d %H:%M:%S")

    rotating_file_handler = RotatingFileHandler("res/logs/create_user.log", maxBytes=10000, backupCount=5)
    rotating_file_handler.setFormatter(formatter)
    logger.addHandler(rotating_file_handler)


    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


    logger.setLevel(logging.DEBUG)

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