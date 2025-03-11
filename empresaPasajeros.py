def ingresarEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El número no puede ser negativo. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def ingresarFlotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El número no puede ser negativo. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

def ingresarViaje():
    origen = input("Ingrese la ciudad de origen: ")
    destino = input("Ingrese la ciudad de destino: ")
    precio = ingresarFlotante("Ingrese el precio del viaje: ")
    pasajeros = []
    while True:
        nombre = input("Nombre del pasajero (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        genero = input("Género del pasajero (M/F): ").upper()
        estudiante = input("¿Es estudiante? (S/N): ").upper()
        descuento = 0.3 if estudiante == 'S' else 0
        pasajeros.append((nombre, genero, descuento))
    return {"origen": origen, "destino": destino, "precio": precio, "pasajeros": pasajeros}

def calcularEstadisticas(viajes):
    totalPasajeros = 0
    totalRecaudado = 0
    totalHombres = 0
    totalMujeres = 0
    totalDescuentos = 0
    maxRecaudo = 0
    mejorViaje = None
    edades = []
    for viaje in viajes:
        recaudoViaje = 0
        for pasajero in viaje["pasajeros"]:
            totalPasajeros += 1
            precioFinal = viaje["precio"] * (1 - pasajero[2])
            totalRecaudado += precioFinal
            recaudoViaje += precioFinal
            totalDescuentos += viaje["precio"] * pasajero[2]
            if pasajero[1] == 'M':
                totalHombres += precioFinal
            else:
                totalMujeres += precioFinal
        if recaudoViaje > maxRecaudo:
            maxRecaudo = recaudoViaje
            mejorViaje = viaje
    return totalPasajeros, totalRecaudado, totalHombres, totalMujeres, totalDescuentos, mejorViaje, maxRecaudo

def main():
    viajes = []
    while True:
        opcion = input("¿Desea ingresar un nuevo viaje? (S/N): ").upper()
        if opcion == 'N':
            break
        viajes.append(ingresarViaje())
    totalPasajeros, totalRecaudado, totalHombres, totalMujeres, totalDescuentos, mejorViaje, maxRecaudo = calcularEstadisticas(viajes)
    print("Total de pasajeros que viajaron:", totalPasajeros)
    print("Total de dinero recaudado:", totalRecaudado)
    print("Total de dinero recaudado por hombres:", totalHombres)
    print("Total de dinero recaudado por mujeres:", totalMujeres)
    print("Total de descuentos aplicados:", totalDescuentos)
    if mejorViaje:
        print(f"El viaje con mayor recaudo fue de {mejorViaje['origen']} a {mejorViaje['destino']} con {maxRecaudo} recaudado.")
if __name__ == "__main__":
    main()