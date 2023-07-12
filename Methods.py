import csv
import random
import datetime
import pandas as pd

with open("csvNotAnonym.csv") as f:
    lines = list(csv.reader(f))
    del lines[0]


def nichtangabe():
    data = pd.read_csv("csvNotAnonym.csv")
    headers = ["id_assessment", "id_student", "date_submitted", "is_banked", "score"]
    nichtangabe = data[headers]
    pd.DataFrame(nichtangabe).to_csv('nichtangabe.csv', header=headers, index=False)


def ersetzung():
    ersetzung = lines
    for i in range(206):
        ersetzung[i][0] = "Mustervorname"
        ersetzung[i][1] = "Musternachname"
        ersetzung[i][2] = "Musteradresse"
        ersetzung[i][3] = '01.01' + str(ersetzung[i][3][5:])
    pd.DataFrame(ersetzung).to_csv('ersetzung.csv', header=["Vorname",
                                                            "Nachname",
                                                            "Adresse",
                                                            "Geburtsdatum",
                                                            "id_assessment",
                                                            "id_student",
                                                            "date_submitted",
                                                            "is_banked",
                                                            "score"], index=False)


def mischung():
    rd_vname = []
    rd_nname = []
    rd_gdate = []

    id_assess = []
    id_student = []
    date_submit = []
    is_banked = []
    score = []

    for i in range(206):
        rd_vname.append(lines[i][0])
        rd_nname.append(lines[i][1])
        rd_gdate.append(lines[i][3])
        id_assess.append(lines[i][4])
        id_student.append(lines[i][5])
        date_submit.append(lines[i][6])
        is_banked.append(lines[i][7])
        score.append(lines[i][8])

    new_vname = random.sample(rd_vname, len(rd_vname))
    new_nname = random.sample(rd_nname, len(rd_nname))
    new_gdate = random.sample(rd_gdate, len(rd_gdate))

    shuffle = [] * 206

    for i in range(206):
        shuffle.append(
            [new_vname[i],
             new_nname[i],
             new_gdate[i],
             id_assess[i],
             id_student[i],
             date_submit[i],
             is_banked[i],
             score[i]])

    pd.DataFrame(shuffle).to_csv('mischung.csv', header=["Vorname",
                                                        "Nachname",
                                                        "Geburtsdatum",
                                                        "id_assessment",
                                                        "id_student",
                                                        "date_submitted",
                                                        "is_banked",
                                                        "score"], index=False)


def varianzmethode():
    current_date = "12.6.2020"
    current_date_temp = datetime.datetime.strptime(current_date, "%d.%m.%Y")
    newdate = current_date_temp + datetime.timedelta(days=random.randint(1, 29))

    # print(newdate.strftime("%d.%m.%Y"))

    rd_gdate = []
    id_assess = []
    id_student = []
    date_submit = []
    is_banked = []
    score = []

    for i in range(206):
        rd_gdate.append((datetime.datetime.strptime(lines[i][3], "%d.%m.%Y") + datetime.timedelta(
            days=random.randint(1, 30))).strftime("%d.%m.%Y"))
        id_assess.append(lines[i][4])
        id_student.append(lines[i][5])
        date_submit.append(lines[i][6])
        is_banked.append(lines[i][7])
        score.append(lines[i][8])

    varianz = [] * 206

    for i in range(206):
        varianz.append(
            [rd_gdate[i],
             id_assess[i],
             id_student[i],
             date_submit[i],
             is_banked[i],
             score[i]])

    pd.DataFrame(varianz).to_csv('varianzmethode.csv', header=["Geburtsdatum",
                                                               "id_assessment",
                                                               "id_student",
                                                               "date_submitted",
                                                               "is_banked",
                                                               "score"], index=False)

if __name__ == '__main__':
    #nichtangabe()
    #ersetzung()
    #mischung()
    varianzmethode()
