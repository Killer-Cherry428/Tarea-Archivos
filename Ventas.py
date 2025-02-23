def ContadorCompras():
    comprasPais = {} # Diccionario para almacenar la dupla, {Pais: Cantidad compras}

    try: #Bloque que captura errores
        with open('SalesJan2009.csv', 'r', encoding='utf-8') as archivo: #leemos el archivo  con codificacion UTF-8
            lineas = archivo.read().split('\n') #el arcgivo se vuelve un unico String con el .split(\n), se divide en los renglones del csv, ese metodo divide la cadena en otras subcadenas
            
            print('\nPaís                 | Número de Compras')
            print("-" * 40)

            for linea in lineas[1:]: #se itera desde la linea 1, ignoramos la 0
                if (not linea.strip()): #elimina los espacios en blanco al inicio y al final de la linea 
                    continue # si la linea esta vacia se la salta
                
                campos = [campo.strip() for campo in linea.split(',')] #primero eliminamos los espacios, luego con el .split() convertimos la linea en una lista dividida por comas
                
                if (len(campos) < 8):  # Verificar que exista el campo País (índice 7), si no cumple ignora la linea para evitar errores
                    continue
                
                pais = campos[7] #traemos el nombre de pais, que se ubica en el indice 7
                
                # Incrementar contador para el país
                if (pais in comprasPais):
                    comprasPais[pais] += 1 #se actualiza el contador, si en el diccionario ya esta el "pais", entonces se suma 1
                else:
                    comprasPais[pais] = 1 #si el pais no esta dentro del diccionario, lo agrega con valor 1

            # Ordenar e imprimir resultados
            for pais, conteo in sorted(comprasPais.items(), key=lambda x: x[1], reverse=True): #el sorted organiza los paises en funcion del que tenga mas compras de forma decendente
                #key=lambda x: x[1] especifica el orden por medio del segundo elemento de la tupla y se ordena de mayor a menor, por el reverse true
                print("{:<20} | {:>10}".format(pais, conteo)) #pais=clave y conteo=valor de transacciones realizadas
                #el print lo que hace es ubicar el valor de pais alineado a la izquierda, para que ocupe 20 caracteres de igual forma con conteo, pero este ocupa 15 a la derecha 

            print("\nTotal de países distintos que realizaron compras:", len(comprasPais)) #longitud del diccionario para conocer cuantos paises estan dentro del CSV
            print("Total de transacciones realizadas:", sum(comprasPais.values())) #Se suman todos los valores de los diccionarios, para tener el dato de cuantas transacciones se realizaron
            print("\n")

    except FileNotFoundError:
        print("Error: Archivo no encontrado")

ContadorCompras()