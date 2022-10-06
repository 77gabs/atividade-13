
def Gabriel(cm):
  ValorPolegadas = cm/2.54
  gdsa = open('arquivo.txt', 'a+', encoding = 'utf-8')
  gdsa.write(f'{cm} cintímetros é %.3f em polegadas.\n' %(ValorPolegadas))