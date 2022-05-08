import datetime, os, pathlib


def save_in_file(licenses, directory):
    if directory:
        filename = "licenses_" + str(datetime.datetime.now()) + ".txt"
        endpath = directory + filename
        with open(endpath, "w+") as f:
            for current in licenses:
                f.write(current)
