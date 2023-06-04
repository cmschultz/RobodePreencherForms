from selenium import webdriver
import pandas as pd
import time

navegador = webdriver.Firefox()
navegador.get("https://forms.gle/qanvgX32PCzfP8997")

tabela = pd.read_excel("Planilha sem título.xlsx")




# ##Teste
# # matematica
# navegador.find_element("xpath",
#     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(6.9)
# # portugues
# navegador.find_element("xpath",
#     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(7)
# # historia
# navegador.find_element("xpath",
#     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(7)
# # geografia
# navegador.find_element("xpath",
#     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(8.6)
# # fisica
# navegador.find_element("xpath",
#     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(9.6)
# # quimica
# navegador.find_element("xpath",
#     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(5.2)
# # biologia
# navegador.find_element("xpath",
#     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(9.3)
# #clicar no botao
# navegador.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()



for i, matematica in enumerate(tabela["Matemática"]):
    portugues = tabela.loc[i, "Português"]
    historia = tabela.loc[i, "História"]
    geografia = tabela.loc[i, "Geografia"]
    fisica = tabela.loc[i, "Física"]
    quimica = tabela.loc[i, "Química"]
    biologia = tabela.loc[i, "Biologia"]

    # matematica
    navegador.find_element("xpath",
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(matematica)
    # portugues
    navegador.find_element("xpath",
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(portugues)
    # historia
    navegador.find_element("xpath",
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(historia)
    # geografia
    navegador.find_element("xpath",
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(geografia)
    # fisica
    navegador.find_element("xpath",
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(fisica)
    # quimica
    navegador.find_element("xpath",
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(quimica)
    # biologia
    navegador.find_element("xpath",
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(biologia)
    # clicar no botao
    navegador.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    
    #outra resposta
    navegador.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    


