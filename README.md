# geopy


### Usando Geopy para encontrar a distância em km entre lojas

- Possuindo as coordenadas das lojas, o objetivo era saber a distâncias em que cada loja do "df_a" estavam das lojas do "df_b" e para isso, tive que iterar para cada loja do "df_a" em todas do "df_b"

- Sabendo a distância em que uma loja do "df_a" estava das do "df_b", retornaria apenas a que possuisse menor distância

- Com isso, teria a resposta de qual loja do "df_b" poderia atender a loja do "df_a", já que estaria mais próxima