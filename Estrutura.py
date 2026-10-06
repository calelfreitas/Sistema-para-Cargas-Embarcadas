cargas_embarcadas = int(input("Quantidade de cargas embarcadas: "))

cargas = []
pesos_cargas = []
cargas_maiores_500 = []
cargas_maiores_800 = []

# Leitura e classificação dos dados
for i in range(cargas_embarcadas):
    carga = float(input(f"Peso da {i+1}ª carga: "))
    cargas.append([i + 1, carga])
    pesos_cargas.append(carga)
    
    # As verificações devem ficar DENTRO do loop
    if carga > 500:
        cargas_maiores_500.append(carga)
    if carga > 800:
        cargas_maiores_800.append(carga)

# Garantindo que existem cargas para calcular estatísticas
if cargas_embarcadas > 0:
    peso_total = sum(pesos_cargas)
    peso_medio = peso_total / len(pesos_cargas)

    # Inicialização para busca do maior e menor
    maior_peso = cargas[0][1]
    alta_carga = cargas[0][0]
    
    menor_peso = cargas[0][1]
    baixa_carga = cargas[0][0]

    # Busca da maior e menor carga
    for linha in cargas:
        num_carga = linha[0]
        peso_atual = linha[1]
        
        if peso_atual > maior_peso:
            maior_peso = peso_atual
            alta_carga = num_carga
            
        if peso_atual < menor_peso:
            menor_peso = peso_atual
            baixa_carga = num_carga

    print("\n" + "-" * 60)
    print("                  Registro de Cargas LogTrans                  ")
    print(f"Peso total das cargas: {peso_total:.2f} Kg")
    print(f"Peso médio das cargas: {peso_medio:.2f} Kg")
    print(f"Quantidade de cargas superiores a 500 Kg: {len(cargas_maiores_500)}")
    print(f"Quantidade de cargas superiores a 800 Kg: {len(cargas_maiores_800)}")
    print(f"Maior carga encontrada: N° {alta_carga} ({maior_peso:.2f} Kg)")
    print(f"Menor carga encontrada: N° {baixa_carga} ({menor_peso:.2f} Kg)")
    print("-" * 60)
else:
    print("\nNenhuma carga foi registrada.")