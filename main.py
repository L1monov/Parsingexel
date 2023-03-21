import db
import pathlib
from pathlib import Path
import defs
import pandas as pd   # pip install pandas

dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'лист.xlsx')

df = pd.read_excel(r'C:\Users\Limonov\PycharmProjects\test\лист.xlsx', sheet_name='Лист1')

print(defs.trabslit_list(df))


