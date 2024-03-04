class Student():
    def __init__(self, inf):
        self.id = inf[0]
        self.Name = inf[1].split()
        self.title = inf[2]
        self.clas = inf[3]
        if inf[4] == "None\n":
            inf[4] = "5"
        self.score = int(inf[4])


f = open("students.csv", encoding="utf8")
f.readline()
spisok = []
for i in f:
    inf = i.split(',')
    s = Student(inf)
    spisok.append(s)

n = int(input())
for i in spisok:
    if i.id == str(n):
        print('Проект №', i.id, "Оценка:", i.score)
        exit()
print("Ничего не найдено")
