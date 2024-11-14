import pandas as pd
from typing import Optional
from datetime import date

from src.views import excel_read

def data(date:str) -> str:
    date = str(date)
    if date == date.today():
        date_1 = str(date.today())[8:10] + '.' + str(date.today())[5:7] + '.' + str(date.today())[0:4]

    s = int(date[3:5])
    r = int(date[6:10])

    if s <= 3:
        e = date[0:3] + str(12-(3-s)) + '.' + str(r-1)
    elif 4 <= s <= 12:
        e = date[0:3] + '0' + str((s - 3)) + date[5:10]
    else:
        e = date[0:3] + str((s - 3)) + date[5:10]
    return e

def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date_1: Optional[str] = date.today()) -> pd.DataFrame:
    pass
    s = 0

    for i in transactions:
        if i['Категория'] == category:
            if i['Дата платежа'] < data(date_1):
                print(i['Дата платежа'])
                s += -i['Сумма операции']

    return s


print(spending_by_category(excel_read('../data/operations.xlsx'), 'Наличные'))
# if date(25.10.2021) > date(27.12.2021):
#     print('dfff')
# print(str(date.today())[8:10] + '.' + str(date.today())[5:7] + '.' + str(date.today())[0:4])


