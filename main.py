import pandas as pd
from menu import menu


try:
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'WA_Fn-UseC_-HR-Employee-Attrition.csv' não foi encontrado.")
    exit()

menu(df)