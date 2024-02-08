from bs4 import BeautifulSoup
import requests
import urllib.request
from openpyxl import *
def check_internet_connection(url):
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.URLError:
        return False

def get_updated_data():


    result = requests.get(url).text
    doc= BeautifulSoup(result, "html.parser")

    tbody=doc.tbody
    trs=tbody.contents

    # dic_conversion={}
    # for tr in trs :
    #     liste=(str(tr.text).split('\n'))
    #
    #     if len(liste)>2:
    #
    #         monnaie, dollar_vers_monnaie, monnaie_vers_dollar=liste[1], liste[2], liste[3]
    #         #print(monnaie, dollar_vers_monnaie, monnaie_vers_dollar)
    #         dic_conversion[monnaie]={}
    #         dic_conversion[monnaie]['en dollar']=float(monnaie_vers_dollar)
    #         dic_conversion[monnaie][f'dollar en {monnaie}'] = float(dollar_vers_monnaie)

    liste_monnaie = ['Euro', 'Japanese Yen', 'British Pound', 'Swiss Franc', 'Canadian Dollar', 'Australian Dollar',
                     'South African Rand']

    def udpate_excel():

        wb = load_workbook('convertisseur_table_updated.xlsx')
        wa = wb.active
        for monnaie, conversion in dic_total.items():
            if monnaie in liste_monnaie:
                index=3
                for i in range(len(liste_monnaie)):
                    if monnaie==liste_monnaie[i]:
                        index+=i
                        break
                wa['B' + str(index)].value=conversion
                wb.save('convertisseur_table_updated.xlsx')




    dic_total={}
    for tr in doc.findAll('table')[1]:
        liste=(str(tr.text).split('\n'))
        if len(liste)>10:
            liste_a_traiter=[]
            for j in range(len(liste)):
                if liste[j]!='':
                    liste_a_traiter.append(liste[j])

            index=0
            while len(dic_total)<len(liste_monnaie):
                if index%3==0 and liste_a_traiter[index] in liste_monnaie:
                    dic_total[liste_a_traiter[index]] = float(liste_a_traiter[index+2])
                    index+=3
                else :
                    index+=3

    udpate_excel()





url='https://www.x-rates.com/table/?from=USD&amount=1'

if check_internet_connection(url):
    get_updated_data()
