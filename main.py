from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd

URL = "https://www.fundsexplorer.com.br/ranking"
OPTIONS = Options()
OPTIONS.add_argument("--headless")
BROWSER = webdriver.Firefox(options=OPTIONS)
BROWSER.get(URL)

table = dict()

for col_title in range(1, 27):
    title_raw = BROWSER.find_element(By.XPATH, f"/html/body/section[1]/div/section[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/table/thead/tr/th[{col_title}]")
    title = title_raw.text
    title.replace("\n", " ")

    row_list = list()
    
    for row_title in range(1, 294):
        row_raw = BROWSER.find_element(By.XPATH, f"/html/body/section[1]/div/section[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/table/tbody/tr[{row_title}]/td[{col_title}]")
        row = row_raw.text
        row_list.append(row)
    
    table[title] = row_list

df = pd.DataFrame(table)

print(df)

df.to_excel("Fundos Imobiliários.xlsx")

BROWSER.close()
