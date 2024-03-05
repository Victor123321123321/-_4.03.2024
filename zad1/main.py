import csv


class Student():
    def __init__(self, inf):
        self.id = inf[0]
        self.Name = inf[1].split()
        self.title = inf[2]
        self.clas = inf[3]
        if inf[4] == "None\n":
            inf[4] = "-1"
        self.score = int(inf[4])


f = open("students.csv", encoding='utf-8')
f.readline()
dict = {}
spisok = []
for i in f:
    inf = i.split(',')
    s = Student(inf)
    if inf[-2] not in dict.keys():
        dict[inf[-2]] = [1, float(inf[-1])]
    else:
        dict[inf[-2]] = [int(dict[inf[-2]][0]) + 1,
                         int(dict[inf[-2]][1]
                             + int(inf[-1]))]
    spisok.append(s)

for i in range(len(spisok)):
    if spisok[i].score == -1:
        spisok[i].score = round(dict[spisok[i].clas][1] / dict[spisok[i].clas][0], 3)
        spisok[i].score = '{:.3f}'.format(spisok[i].score)
    if " ".join(spisok[i].Name)[:len("Хадаров Владимир")] == "Хадаров Владимир":
        print("Ты получил: " + str(spisok[i].score) + ", за проект - " + str(spisok[i].title))

with open("student_new.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(['id', "Name", "titleProject_id", "class", "score"])
    for i in spisok:
        file_writer.writerow([i.id, ' '.join(i.Name), i.title, i.clas, i.score])
