import numpy as np
import pandas as pd
import csv
from faker import Faker
from faker.providers import address
from faker.providers import date_time
from faker.providers import person
#Faker URL: https://faker.readthedocs.io/en/master/ (Zuletzt besucht: 02.06.2023)
#Pandas URL: https://pandas.pydata.org (Zuletzt besucht: 02.06.2023)
#CSV-Datei einlesen URL: https://www.python-lernen.de/csv-datei-einlesen.htm (Zuletzt besucht: 02.06.2023)


fake = Faker('en_UK')
fake.unique.add_provider(person)
fake.add_provider(address)
fake.add_provider(date_time)

with open("studentAssesment.csv") as f:
    lines = list(csv.reader(f))
    del lines[0]
    print(lines[0])

lst = []
for i in range(206):
    lst.append([str(fake.first_name()),
                str(fake.last_name()),
                str(fake.address()).replace("\n", " "),
                str(fake.date_of_birth(minimum_age=18, maximum_age=28).strftime("%d.%m.%Y"))])

csvNotAnonym = [[]] * 206
for i in range(206):
    csvNotAnonym[i] = lst[i] + lines[i]
print(csvNotAnonym)
pd.DataFrame(csvNotAnonym).to_csv('csvNotAnonym.csv',header=["Vorname",
                                                          "Nachname",
                                                          "Adresse",
                                                          "Geburtsdatum",
                                                          "id_assessment",
                                                          "id_student",
                                                          "date_submitted",
                                                          "is_banked",
                                                          "score"], index=False)

