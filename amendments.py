import csv
import random
import re
import string
import shutil
from tempfile import NamedTemporaryFile

filename = 'LaTeXOnly.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)
relevant_col = 1

matrix_choices = ["A", "B", "C", "D", "X", "Y"]
set_choices = ["A", "B", "C", "D", "X", "Y"]
prime_choices = ["a'", "b'", "c'", "x'", "y'", "z'"]
variable_pattern = r"g\\_prime}\((?:a'|b'|c'|x'|y'|z')\)"

def replace_matrix(match):
    return random.choice(matrix_choices)

def replace_set(match):
    return random.choice(set_choices)

def replace_base(match):
    return "{:.2f}".format(random.uniform(1, 500))

def replace_number(match):
    return str(random.randint(1, 500))

def replace_letter(match):
    return random.choice(string.ascii_lowercase)

def replace_field(match):
    return "F"

def replace_force(match):
    return "F"

def replace_mass(match):
    return "m"

def replace_expected(match):
    return "\\hat{y}"

def replace_observed(match):
    return "y"

def replace_acceleration(match):
    return "\\alpha"

def replace_std(match):
    return "\\sigma"


with open(filename, 'r', newline='') as csvfile, tempfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(tempfile)

    
    for row in reader:
        if len(row) > relevant_col:
            row[relevant_col] = re.sub(r"\{matrix\}", replace_matrix, row[relevant_col])
            row[relevant_col] = re.sub(r"\{set\}", replace_set, row[relevant_col])
            row[relevant_col] = re.sub(r"\{variable\}", replace_letter, row[relevant_col])
            row[relevant_col] = re.sub(r"\{base\}", replace_base, row[relevant_col])
            row[relevant_col] = re.sub(r"\{number\}", replace_number, row[relevant_col])
            row[relevant_col] = re.sub(r"\{field\}", replace_field, row[relevant_col])
            row[relevant_col] = re.sub(r"\{Force\}", replace_force, row[relevant_col])
            row[relevant_col] = re.sub(r"\{mass\}", replace_mass, row[relevant_col])
            row[relevant_col] = re.sub(r"\{Expected\}", replace_expected, row[relevant_col])
            row[relevant_col] = re.sub(r"\{Observed\}", replace_observed, row[relevant_col])
            row[relevant_col] = re.sub(r"\{acceleration\}", replace_acceleration, row[relevant_col])
            row[relevant_col] = re.sub(r"\{event1\}", "E1", row[relevant_col])
            row[relevant_col] = re.sub(r"\{event2\}", "E2", row[relevant_col])
            row[relevant_col] = re.sub(r"\\{_prime}", "'", row[relevant_col])
            row[relevant_col] = re.sub(r"\{std\\_dev\}", replace_std, row[relevant_col])
        writer.writerow(row)

shutil.move(tempfile.name, filename)
