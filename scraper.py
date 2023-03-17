from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
#START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

# Controlador web
browser = webdriver.Chrome("D:\documentos\TravisV4.1\Snacks\Python\PRO-C127_EXTRACCIÓN_DE_DATOS_WEB\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Definir el método de extracción de datos para wikitable
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## AGREGAR EL CÓDIGO AQUÍ ##
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("table", attrs = {"class", "wikitable"}):
            li_tags = ul_tag.find_all("tb")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if (index == 0):
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try: 
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planets_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()




        
# Llamada del método
scrape()

# Definir los encabezados
headers = ["Start_name", "Distance", "mass", "radius", "Luminosity"]

# Definir el dataframe de Pandas
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Convertir a CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")