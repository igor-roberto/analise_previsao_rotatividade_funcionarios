import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def opt_1(df):
    print("\n📊 Contagem de Funcionários que Saíram ou Permaneceram:\n")

    contagem = df['Attrition'].value_counts()

    new_names = {
        "No": "Funcionários que permaneceram",
        "Yes": "Funcionários que saíram"
    }

    for chave, valor in contagem.items():
        print(f'{new_names[chave]}: {valor}')


def opt_2(df):
    print("\n Taxa de rotatividade:\n")

    cont_porc= df['Attrition'].value_counts(normalize=True)*100

    new_names = {
        "No": "Funcionários que permaneceram",
        "Yes": "Funcionários que saíram"
    }

    for chave, valor in cont_porc.items():
        print(f'{new_names[chave]}: {valor:.2f}%')
        

def opt_3(df):
    sns.kdeplot(df[df['Attrition'] == 'Yes']['Age'],label='Saiu', linewidth=2, color='red')
    sns.kdeplot(df[df['Attrition'] == 'No']['Age'], label='Permaneceu', linewidth=2, color='green')

    plt.legend()
    plt.title('Distribuição da Idade - Rotatividade')
    plt.xlabel('Idade')
    plt.ylabel('Densidade')
    plt.grid()
    plt.show()


def opt_4(df):
    print("\n📊 Correlação entre Variáveis Numéricas e Rotatividade (Variáveis Chave):\n")

    #Selecionando apenas as colunas que contém números
    number_df = df.select_dtypes(include=['number'])

    #Precisamos transformar o Yes(1) e No(0) para numero

    df_corr = df.copy()
    df_corr['Attrition_Numeric'] = df_corr['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0) #criamos uma nova coluna, o lambda cria uma função anonima chamada X, caso for Yes substitui o X por 1, caso contrario substitua por 0


    #correlacionado as colunas numericas com a que eu acabei de criar, a df_corr

    correlacao = df_corr[number_df.columns].corrwith(df_corr['Attrition_Numeric']).sort_values(ascending=False)

    format_correlacao = correlacao.dropna().round(4)
    print('Correlação com a Rotatividade:\n',format_correlacao.to_string())


    plt.figure(figsize=(12,10))

    top_correlacoes = correlacao.abs().dropna().nlargest(10).index

    if not top_correlacoes.empty:
        sns.heatmap(df_corr[top_correlacoes].corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title('Mapa de calor de correlação das 10 variáveis mais correlacionadas com Attrition')
        plt.tight_layout()
        plt.show()
    else:
        print("\nNão há variáveis suficientes para gerar o heatmap de correlação.")


def opt_5(df):
    print('\n📊 Rotatividade por Departamento:\n')

    dp_att = df.groupby(['Department','Attrition']).size().unstack(fill_value=0)
    dp_att['Total'] = dp_att['No'] + dp_att['Yes']
    dp_att['Attrition_Rate_%'] = (dp_att['Yes'] / dp_att['Total']) *100

    print(dp_att.sort_values(by='Attrition_Rate_%', ascending=False))

    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x='Department', hue='Attrition', palette='viridis')
    plt.title('Rotatividade por Departamento')
    plt.xlabel('Departamento')
    plt.ylabel('Número de Funcionários')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Rotatividade', labels=['Permaneceu', 'Saiu'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def opt_6(df):
    print("\n📊 Rotatividade por Horas Extra:\n")

    overtime_reduction = df.groupby(['OverTime', 'Attrition']).size().unstack(fill_value=0)
    overtime_reduction['Total'] = overtime_reduction['No'] + overtime_reduction['Yes']
    overtime_reduction['Attrition %'] = ((overtime_reduction['Yes']/ overtime_reduction['Total'])*100).round(2)



    print(overtime_reduction.sort_values(by= 'Attrition %', ascending=False))



    plt.figure(figsize=(8,6))
    sns.countplot(data=df, x='OverTime', hue='Attrition', palette='magma')
    plt.title('Rotatividade por Horas Extras')
    plt.xlabel('Horas Extra')
    plt.ylabel('N° Funcionários')
    plt.legend(title='Rotatividade', labels=['Permaneceu', 'Saiu'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
