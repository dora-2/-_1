import pandas as pd
from typing import Optional
from src.views import excel_read

def data(date:str) -> str:
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
                         date: Optional[str] = None) -> pd.DataFrame:
    pass
    s = 0
    for i in transactions:
        if i['Категория'] == category:
            if i['Дата операции'][:-9] < data(date):
                print(i['Дата операции'][:-9])
                s += -i['Сумма операции']

    return s


print(spending_by_category(excel_read('../data/operations.xlsx'), 'Наличные', '27.12.2021'))



