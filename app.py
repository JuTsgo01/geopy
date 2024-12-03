#%%
import geopy
import geopy.distance
from geopy.distance import geodesic
import pandas as pd
#%%
df_a = pd.read_excel('lojasMadeiro.xlsx')
df_b = pd.read_excel('lojasEchope.xlsx')

#%%

def extrair_coordenada (localizacao):
    lat, long = map(float, localizacao.split(', '))
    return lat, long

def calcular_distancias (df_a, df_b):
    
    resultado = []

    for _, row_a in df_a.iterrows():
        loja_a = row_a['Localidade']
        lojas_a_coord = extrair_coordenada(row_a['Coordenada'])
        menor_distancia = float('inf')
        loja_b_mais_proxima = None
        
        for _, row_b in df_b.iterrows():
            loja_b = row_b['NOME']
            loja_b_coord = extrair_coordenada(row_b['latLong'])
            
            distancia = geodesic(lojas_a_coord, loja_b_coord).kilometers
            
            if distancia < menor_distancia:
                menor_distancia = distancia
                loja_b_mais_proxima = loja_b
                
        resultado.append({'loja_madeiro':loja_a, 
                            'loja_echope':loja_b_mais_proxima,
                            'distancia_km':menor_distancia})
    df_distancia_calculada = pd.DataFrame(resultado)
    
    return df_distancia_calculada

distancias = calcular_distancias(df_a, df_b)

distancias.to_excel('distancias_lojas.xlsx', index=False)