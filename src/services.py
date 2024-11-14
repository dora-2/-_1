from src.views import excel_read
import re
import json



def dgvljdb():
    s = excel_read('../data/operations.xlsx')
    w = []
    for i in s:
        if i['Категория'] == 'Переводы' and re.findall('[A-ЯЁ][а-яё]+\s+[А-ЯЁ]\.', i['Описание']):
            w.append(i)
    return w

print(dgvljdb())

# json_data = json.dumps(dgvljdb(), indent=4)
#
# # Запишем данные в файл
# with open("services.json", "w") as file:
#     file.write(json_data)
#
# print("JSON файл успешно создан!")