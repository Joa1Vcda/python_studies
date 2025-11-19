import os
import json

"""Creating archives in Python"""

# pathing = 'c:\\Users\\Samsung\\Desktop\\Repositories\\Python_studies\\Python-cap2\\'
# pathing += 'testing(page 02).txt'

# with open(pathing, 'w+', encoding='utf-8') as archive:
#     archive.write('Atenção\n''Linha 1\n''Linha 2',)
#     archive.seek(0,0)
#     print(archive.read())

# os.remove(pathing)

randomdict = {
    "name": "João Vitor",
    "last name": "Cirqueira de Araújo",
    "Years old": "19",
    "Adresses": [
        {"Street": "R1", "number": 513},
        {"Street": "R2", "number": 612},
    ],
    "Dev": True,
}

Directorypath = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(Directorypath, "dict.json")

with open(path, "w+", encoding="utf-8") as archive_2:
    json.dump(randomdict, archive_2, ensure_ascii=False)
