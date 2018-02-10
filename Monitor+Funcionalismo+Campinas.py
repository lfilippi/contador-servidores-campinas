
# coding: utf-8

# In[ ]:


# 1. Monitor do número de servidores por secretaria na Prefeitura de Campinas

import csv

busca_secretaria = ["Saúde"]
busca_print = busca_secretaria[0].title()

planilha = open('SalariosCampinas_janeiro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em janeiro de 2017")

planilha = open('SalariosCampinas_fevereiro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em fevereiro de 2017")

planilha = open('SalariosCampinas_marco2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em março de 2017")

planilha = open('SalariosCampinas_abril2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em abril de 2017")

planilha = open('SalariosCampinas_maio2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em maio de 2017")

planilha = open('SalariosCampinas_junho2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em junho de 2017")

planilha = open('SalariosCampinas_julho2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em julho de 2017")

planilha = open('SalariosCampinas_agosto2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em agosto de 2017")

planilha = open('SalariosCampinas_setembro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em setembro de 2017")

planilha = open('SalariosCampinas_outubro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em outubro de 2017")

planilha = open('SalariosCampinas_novembro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em novembro de 2017")

planilha = open('SalariosCampinas_dezembro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_secretaria:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais na folha salarial da Secretaria de {busca_print} em dezembro de 2017")


# In[ ]:


# 2. Monitor do número de servidores por cargo na Prefeitura de Campinas

import csv


busca_cargo = ["MEDICO"]
cargo_print = busca_cargo[0].title()

planilha = open('SalariosCampinas_janeiro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de janeiro de 2017")

planilha = open('SalariosCampinas_fevereiro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de fevereiro de 2017")

planilha = open('SalariosCampinas_marco2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de março de 2017")

planilha = open('SalariosCampinas_abril2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de abril de 2017")

planilha = open('SalariosCampinas_maio2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de maio de 2017")

planilha = open('SalariosCampinas_junho2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de junho de 2017")

planilha = open('SalariosCampinas_julho2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de julho de 2017")

planilha = open('SalariosCampinas_agosto2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de agosto de 2017")

planilha = open('SalariosCampinas_setembro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de setembro de 2017")

planilha = open('SalariosCampinas_outubro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de outubro de 2017")

planilha = open('SalariosCampinas_novembro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de novembro de 2017")

planilha = open('SalariosCampinas_dezembro2017.csv', encoding='utf-8')
cargo_encontrado = {}
contador_cargo = 0
for linha in planilha:
    for palavra in busca_cargo:
        if palavra in linha:
            contador_cargo = contador_cargo + 1
    cargo_encontrado[palavra] = contador_cargo
print(f"A Prefeitura de Campinas tem {contador_cargo} profissionais com o cargo de {cargo_print} na folha salarial de dezembro de 2017")

