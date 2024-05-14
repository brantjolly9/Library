import sqlite3
import pandas as pd
book_path = 'Book1.xlsx'

xls = pd.ExcelFile(book_path)
sheet_names = xls.sheet_names
conn = sqlite3.connect('books.db')


def load_excel():
    for sheet_name in sheet_names:
        df = pd.read_excel(book_path, sheet_name=sheet_name)
        # Create a table name based on the sheet name, or use a custom naming scheme
        table_name = sheet_name.replace(' ', '_') # Example: replace spaces with underscores
        df.to_sql(table_name, conn, if_exists='replace', index=False)
