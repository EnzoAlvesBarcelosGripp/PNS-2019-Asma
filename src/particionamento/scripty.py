import pandas as pd
df = pd.read_csv(r"C:\Users\Enzo Gripp\Desktop\Faculdade\Mineração de Dados - PNS\data\Csv\pns2019.csv")
variaveis = {
    'C006' : 'Sexo',
    'C008':'Idade',
    'D00901':'Escolaridade',
    'E01601':'Exato Renda Trabalho0',
    'E01603':'Exato Renda Trabalho1',
    'E01801':'Exato Renda Trabalho2',
    'E01803':'Exato Renda Trabalho3',
    'F001021':'Exato Renda Trabalho4',
    'F007021':'Exato Renda Trabalho5',
    'F008021':'Exato Renda Trabalho6',
    'VDF00102':'Exato Renda Trabalho7',
    'M01001':'Fumo passivo no trabalho',
    'P00103':'Peso (automedido)',
    'P00403':'Altura (automedida)',
    'P00901':'Consumo em dias vegetal/legume',
    'P01001':'Consumo por dia vegetal/legume',
    'P015':'Consumo em dias peixe',
    'P018':'Consumo em dias frutas',
    'P019':'Consumo por dia frutas',
    'P02002':'Consumo em dias refrigerante',
    'P02102':'Tipo de refrigerante consumido',
    'P02501':'Consumo em dias alimentos doces',
    'P02602':'Consumo em dias alimentos ultraprocessados',
    'P034':'Pratica de exercicio',
    'P035':'Quantidade de exercicios na semana',
    'P036':'Tipo de exercicio',
    'P050':'Fumante ativo',
    'P052':'Ex-Fumante',
    'P068':'Fumante passivo',
    'Q074':'Asmatico',
    'W00201':'Altura - Primeira medida',
    'W00202':'Altura - Segunda medida',
    'W00101':'Peso - Primeira medida',
    'W00102':'Peso - Segunda medida',
    'VDF003':'Rendimento domiciliar per capita',
    #doenças
    'Q00201': 'Doenca 1',
    'Q03001': 'Doenca 2',
    'Q060': 'Doenca 3',
    'Q06306': 'Doenca 4',
    'Q068' : 'Doenca 5',
    'Q079': 'Doenca 6',
    'Q088': 'Doenca 7',
    'Q092': 'Doenca 8',
    'Q11006': 'Doenca 9',
    'Q11604': 'Doenca 10',
    'Q120': 'Doenca 11',
    'Q128': 'Doenca 12'
}

colunas_doencas = [
    'Doenca 1', 'Doenca 2', 'Doenca 3', 'Doenca 4', 'Asmatico','Doenca 5', 
    'Doenca 6', 'Doenca 7', 'Doenca 8', 'Doenca 9', 'Doenca 10', 
    'Doenca 11', 'Doenca 12', 
]

df_filtrado = df[list(variaveis.keys())].rename(columns=variaveis).copy()
df_bem = df_filtrado[
    (df_filtrado['Idade'] >= 30) & 
    (df_filtrado['Idade'] < 60) & 
    (df_filtrado[colunas_doencas] == 2).all(axis=1)
].copy()

df_Asmaticos= df_filtrado.query("Asmatico == 1 and Idade >= 30 and Idade < 60").copy()

print(len(df_Asmaticos))
print(len(df_bem))

doencas_para_apagar = [d for d in colunas_doencas if d != 'Asmatico']
df_bem = df_bem.drop(columns=doencas_para_apagar)
df_Asmaticos = df_Asmaticos.drop(columns=doencas_para_apagar)

df_final = pd.concat([df_bem,df_Asmaticos],ignore_index=True)

path = r"C:\Users\Enzo Gripp\Desktop\Faculdade\Mineração de Dados - PNS\data\Csv\pns2019_filtrado.csv"
df_final.to_csv(path, index=False, encoding='utf-8-sig')

print(df_final['Asmatico'].value_counts())