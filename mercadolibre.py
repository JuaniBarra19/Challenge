import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://listado.mercadolibre.com.ar/dodge-gtx-de-colecci%C3%B3n#D[A:Dodge%20Gtx%20-%20De%20Colecci%C3%B3n]') 
driver.maximize_window()


PAGINACION_MAX = 10
PAGINACION_ACTUAL = 1 
NOMBRE = [] 
PRECIO = []




try: 
  disclaimer = driver.find_element_by_xpath('//button[@data-testid="action:understood-button"]')
  disclaimer.click() 
except Exception as e:
  print (e) 
  None


while PAGINACION_MAX > PAGINACION_ACTUAL:

  links_productos = driver.find_elements_by_xpath('//a[@class="ui-search-result__content ui-search-link"]')
  links_de_la_pagina = []
  for a_link in links_productos:
    links_de_la_pagina.append(a_link.get_attribute("href"))
 



  for link in links_de_la_pagina:

    try:
      
      driver.get(link)

      titulo = driver.find_element_by_xpath('//h1').text
      precio = driver.find_element_by_xpath('//div[@class="ui-pdp-price__second-line"]//span[@class="andes-visually-hidden"]').text
      NOMBRE.append(titulo) 
      PRECIO.append(precio)
      print (titulo)
      print (precio)

      
      driver.back()
    except Exception as e:
      print (e)
      
      driver.back()

  
  try:
    puedo_seguir_horizontal = driver.find_element_by_xpath('//span[text()="Siguiente"]')
    puedo_seguir_horizontal.click()
  except: 
    break

  PAGINACION_ACTUAL += 1  

data = {
        "Nombre": NOMBRE,
        "Precio": PRECIO
                
        }   

df = pd.DataFrame(data) 
print(df)  
df.to_csv('Articulos.csv', index = None, header=True)  