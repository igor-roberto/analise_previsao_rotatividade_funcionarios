import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'WA_Fn-UseC_-HR-Employee-Attrition.csv' não foi encontrado.")
    exit()


