
print("=" * 40)
print("       Cálculo de Área de Terrenos")
print("=" * 40)

quantidade = int(input("Quantos terrenos?: "))

if quantidade <= 0:
    print("A quantidade deve ser maior que zero!")

else:
    area_total = 0
    maior_area = 0
    menor_area = 0

    maior_terreno = 0
    menor_terreno = 0

    areas = []

    for i in range(quantidade):

        print("-" * 40)
        print(f"Terreno {i + 1}")
        print("-" * 40)

        largura = float(input("Largura (metros): "))
        comprimento = float(input("Comprimento (metros): "))

        if largura <= 0 or comprimento <= 0:
            print("As medidas devem ser positivas!")
            break

        area = largura * comprimento

        print(f"Área do terreno {i + 1}: {area:.2f} m²")

        areas.append(area)

        area_total += area

        if i == 0:
            maior_area = area
            menor_area = area
            maior_terreno = i + 1
            menor_terreno = i + 1

        else:
            if area > maior_area:
                maior_area = area
                maior_terreno = i + 1

            if area < menor_area:
                menor_area = area
                menor_terreno = i + 1

    else:
        diferenca = maior_area - menor_area

        print("=" * 40)
        print("            RESULTADO FINAL")
        print("=" * 40)

        for i in range(quantidade):
            print(f"Área do terreno {i + 1}: {areas[i]:.2f} m²")

        print("-" * 40)
        print(f"Área total: {area_total:.2f} m²")

        if maior_area == menor_area:
            print("Todos os terrenos possuem a mesma área!")
        else:
            print(f"Maior terreno: Terreno {maior_terreno}")
            print(f"Maior área: {maior_area:.2f} m²")

            print(f"Menor terreno: Terreno {menor_terreno}")
            print(f"Menor área: {menor_area:.2f} m²")

        print(f"Diferença entre as áreas: {diferenca:.2f} m²")
        print("=" * 40)
