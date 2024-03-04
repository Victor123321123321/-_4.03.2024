import csv
import random


class Student():
    def __init__(self, inf):
        self.id = inf[0]
        self.Name = inf[1].split()
        self.title = inf[2]
        self.clas = inf[3]
        if inf[4] == "None\n":
            inf[4] = "1"
        self.score = int(inf[4])
        self.login = generate_login(self.Name)
        self.password = generate_password()


def generate_login(name):
    return name[0] + "_" + name[1][0] + name[2][0]


def generate_password():
    st = ''
    for i in range(8):
        st += "1234567890QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"[random.randint(0, 61)]
    return st


f = open(input(), encoding="utf-8")
f.readline()
spisok = []
for i in f:
    inf = i.split(',')
    s = Student(inf)
    spisok.append(s)

with open("students_password.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    for i in spisok:
        file_writer.writerow([i.id, i.Name, i.title, i.clas, i.score, i.login, i.password])
