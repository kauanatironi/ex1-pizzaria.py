def percorrer(caminhos, caminho, visitar):
    
    if visitar == []:
        caminhos.append(caminho)
    
    else:
        for x in visitar:
            copia_caminho = list(caminho)
            copia_visitar = list(visitar)
            copia_caminho.append(x)
            copia_visitar.remove(x)
            percorrer(caminhos, copia_caminho, copia_visitar)

    return caminhos

def somar_distancias(caminho, distancias):
    distancia = 0
    
    for i in range(len(caminho)):
    
        if i == len(caminho)-1: # se for o ultimo elemento da lista calcula com o primeiro
            posicao = caminho[i]+caminho[0]

        else:
            posicao = caminho[i]+caminho[i+1]
    
        distancia += distancias[posicao]

    return distancia

distancias = {"AB": 1,
            "AC": 2.64,
            "AD": 4,
            "BA": 1,
            "BC": 2,
            "BD": 4.13,
            "CA": 2.64,
            "CB": 2,
            "CD": 3,
            "DA": 4,
            "DB": 4.13,
            "DC": 3}

caminhos = percorrer([], ["A"], ["B", "C", "D"])

for caminho in caminhos:
    print(caminho)
    distancia = somar_distancias(caminho, distancias)
    print("Distância: " + str(distancia))
