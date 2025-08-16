from analises import (opt_1, opt_2,opt_3,opt_4, opt_5, opt_6)
import time


def menu(df):
    while True:
        print("\nMenu de Análises de Rotatividade de Funcionários")
        print("[1] Quantos funcionários saíram da empresa?")
        print("[2] Qual a taxa de rotatividade?")
        print("[3] Distribuição de idade por rotatividade")
        print("[4] Correlação entre variáveis numéricas")
        print("[5] Rotatividade por Departamento")
        print("[6] Rotatividade por Horas Extras")
        print("[0] Sair")

        opt = int(input("Escolha uma opção de 1 a 7 ---> "))


        if opt == 1:
            opt_1(df)
        
        elif opt == 2:
            opt_2(df)
        
        elif opt == 3:
            opt_3(df)

        elif opt == 4:
            opt_4(df)
        
        elif opt==5:
            opt_5(df)
        
        elif opt==6:
            opt_6(df)

        elif opt == 0:
            print('Saindo...')
            time.sleep(2)
            break
        else: 
            print('Opção não implementada!')



    