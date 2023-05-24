from funciones_parcial1 import *
import json
import os


lista_elementos_con_marca_nueva = []
lista_insumos_act=[]

while True:
    os.system("cls")  # limpia el terminal de ejecuc
    opcion = mostrar_menu()  # importo el menu desde el archivo menu.py

    if opcion == "1":
        # abro el archivo insumos.csv, lo recorro y convierto en lista de # diccionarios
        with open("primer_parcial_labo\insumos.csv", "r", encoding="utf-8") as file:
            lista = []
            lista_elementos0 = []
            lista_elementos = []
            diccionario = {}
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            for elemento in lista_elementos0:
                lista_elementos.append({"ID": elemento[0], "NOMBRE": elemento[1],
                                        "MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})

    elif opcion == "2":
        motrar = mostrar_cantidad_por_marca(lista_elementos, "MARCA")
    elif opcion == "3":
        motrar = mostrar_marca_y_precios(lista_elementos, "MARCA")
    elif opcion == "4":
        motrar = mostrar_por_caracteristica(lista_elementos, "CARACTERISTICAS")
    elif opcion == "5":
        motrar = ordenar_listas_dict(lista_elementos, "MARCA", True)
    elif opcion == "6":  # hacer compras
        total = 0
        with open("primer_parcial_labo\compras.txt", "w") as file:
            file.write("                           FACTURA DE COMPRA\n")
            file.write(
                "\nCANTIDAD                   PRODUCTO/MARCA                     SUBTOTAL                    \n")
            file.write("\n")
            while True:
                # dato = input("Ingrese un dato (o escriba 'salir' para terminar): ")
                coincidencia = 0
                marca_ingresada = input("ingrese marca: (o salir)").lower()
                for elemento in lista_elementos:
                    if (marca_ingresada == str(elemento["MARCA"]).lower()):
                        coincidencia += 1
                while (coincidencia == 0 and marca_ingresada != "salir"):
                    marca_ingresada = input(
                        "ERROR: ingrese marca de la lista: (o salir)")
                    for elemento in lista_elementos:
                        if ((marca_ingresada == str(elemento["MARCA"]).lower()) or marca_ingresada == "salir"):
                            coincidencia += 1
                if marca_ingresada == 'salir':
                    file.write(
                        "\n" + "TOTAL A PAGAR                                                $"+str(total))
                    file.close
                    break
            # declaro la lista donde voy a appendear los id que coincidan con la caracteristica ingresada
                lista_id_caracteristica = []
                for elemento in lista_elementos:
                    # appendeo los id que coincidan con la caracteristica
                    if str(marca_ingresada) in str(elemento["MARCA"]).lower():
                        lista_id_caracteristica.append(elemento["ID"])
                        print(elemento)
                producto_id = input("ingrese numero del producto: ")
            # valido que numero de producto este en la lista id y que no sea alfabetico
                while ((producto_id not in lista_id_caracteristica) or producto_id.isalpha()):
                    producto_id = input("Error, ingrese numero del producto: ")

                for elemento in lista_elementos:
                    if elemento["ID"] == producto_id:
                        precio_producto = elemento["PRECIO"]
                        producto = elemento["NOMBRE"]
                        precio_producto = precio_producto.replace("$", "")
                        precio_producto = float(precio_producto)
                        print("El precio del producto es: $",
                              str(precio_producto))
                cantidad = input("ingrese cantidad: ")
            # valido que la cantidad de productos este entre (0 y 100) y que no sea alfabetico

                # while ((cantidad.isalpha() or cantidad.isalnum()) or (int(cantidad) < 0 or int(cantidad)>100 )):
                while ((cantidad.isalpha()) or (int(cantidad) < 0 or int(cantidad) > 100)):
                    cantidad = input(
                        "Error, ingrese una cantidad correcta (1-100): ")

                cantidad = int(cantidad)
                subtotal = precio_producto*cantidad
                total += subtotal
                file.write(str(cantidad) + "                   " + producto +
                           ", " + marca_ingresada + "          " + str(subtotal) + "\n")
        with open("primer_parcial_labo\compras.txt", "r") as file:
            for linea in file.readlines():
                print(linea)

    # Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra "Alimento".
    elif opcion == "7":
        # abro "productos.js" modo escritura
        with open("primer_parcial_labo\productos.json", "w", encoding="utf-8") as file:
            # copie el insumos.csv a un .json
            # abro "insumos.csv" modo lectura para obtener los insumos
            with open("primer_parcial_labo\insumos.csv", "r", encoding="utf-8") as file:
                lista = []
                lista_elementos0 = []
                lista_elementos_js = []
                diccionario = {}

                for linea in file:
                    linea = linea.lower()
                    # filtrando los que tienen la palabra "alimento"
                    if "alimento" in str(linea).lower():
                        # abro "productos.js" modo "a" para appendearles las lineas
                        with open("primer_parcial_labo\productos.json", "a", encoding="utf-8") as file:
                            file.write(linea)

    elif opcion == "8":  # abro el archivo productos.js, lo recorro y convierto en lista de diccionarios
        with open("primer_parcial_labo\productos.json", "r", encoding="utf-8") as file:
            lista = []
            lista_elementos0 = []
            lista_elementos_js = []
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            for elemento in lista_elementos0:
                print(elemento)
                lista_elementos_js.append({"ID": elemento[0], "NOMBRE": elemento[1],
                                           "MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})

    elif opcion == "9":  # actualizar precios
        # abro el archivo insumos.csv, lo recorro y convierto en lista de
        with open("primer_parcial_labo\insumos.csv", "r", encoding="utf-8") as file:
            # diccionarios
            lista = []
            lista_elementos0 = []
            lista_elementos = []
            diccionario = {}
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            # hago una funcion nueva con MAP recorriendo "lista_elementos0" y le doy el formato dict con las claves por cada indice de la lista y ademas,
            # directamente paso a float el PRECIO que es con el que vouy a hacer cuentas.
            lista_elementos = list(map(lambda elemento: {"ID": elemento[0], "NOMBRE": elemento[1], "MARCA": elemento[2], "PRECIO": float(
                elemento[3].replace("$", "")), "CARACTERISTICAS": elemento[4]}, lista_elementos0))

        with open("primer_parcial_labo\insumos2.csv", "w", encoding="utf-8") as file:
            for elemento in lista_elementos:
                porcentaje = 8.4

                elemento["PRECIO"] = elemento["PRECIO"] + \
                    (elemento["PRECIO"]*porcentaje/100)

                file.write(
                    f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]:.2f}{","}{elemento["CARACTERISTICAS"]}\n')
            print(
                "se realizo incremento del 8.4'%' a los precios. y se guardo en archivo insumos2.csv")

    elif opcion == "10":
        
        with open("primer_parcial_labo\marcas.txt", "r", encoding="utf-8") as file:
            # diccionarios
            
            lista_marcas_nuevas=[]
            diccionario = {}
            for linea in file:
                lista_marcas_nuevas.append((linea.replace("\n","")).lower())
            print("Las marcas disponibles son:\n")
            for marca in lista_marcas_nuevas:
                print(marca)
            print("\n")
        marca_ingresada=input("ingrese una marca de las listadas: ").lower()
        while True:
            if (marca_ingresada.isdigit() or (marca_ingresada not in lista_marcas_nuevas)):
                print("Las marcas disponibles son:\n")
                for marca in lista_marcas_nuevas:
                    print(marca)
                print("\n")
                marca_ingresada=input("ingrese una marca de las listadas: ").lower()
            else:
                break
        print("Marca Correcta\n")
        lista_id=[]
        for elementos in lista_elementos:
            lista_id.append(elementos["ID"])
        id=input("Ingrese ID del producto: ")
        while (id.isalpha() or id in lista_id):
            id=input("ID existente, Ingrese ID valido: ")

        nombre=input("Ingrese nombre del producto: ")
        precio=input("Ingrese precio del producto: $")
        cont_carac=2
        caracteristicas=input("Ingrese caracteristicas del producto (1 a 3): ")
        while cont_carac < 4:
            cargar_otra=input("desea ingresar otra caracteristica?: (si/no)").lower()
            if cargar_otra == "no":
                break
            else:
                caracteristicas_=input("Ingrese caracteristicas del producto (1 a 3): ")
                caracteristicas+="~"+caracteristicas_
                cont_carac+=1
        
        lista_elementos_con_marca_nueva.append({"ID": id, "NOMBRE": nombre,
                                        "MARCA": marca_ingresada, "PRECIO": "$"+str(precio), "CARACTERISTICAS": caracteristicas})
        print(lista_elementos_con_marca_nueva)
        lista_elementos.append({"ID": id, "NOMBRE": nombre,
                                        "MARCA": marca_ingresada, "PRECIO": "$"+str(precio), "CARACTERISTICAS": caracteristicas})

    elif opcion == "11":

        tipo_de_archivo=input("Ingrese 2 para guardarlo como .csv 1 para guardarlo como .json: ")
        #nombre_archivo = input("Ingrese el nombre del archivo a crear: ")
        if tipo_de_archivo == "1":
            with open("primer_parcial_labo\datos_act.csv", "w", encoding="utf-8") as file:
                for elemento in lista_elementos:
                    file.write(
                        f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')
                if len(lista_elementos_con_marca_nueva) > 1:
                        for elemento in lista_marcas_nuevas:
                            file.write(
                                f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')    
        elif tipo_de_archivo == "2":
            with open("primer_parcial_labo\datosactualizados.json", "w", encoding="utf-8") as file:
                
                for elemento in lista_elementos:
                    file.write(
                        f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')
                if len(lista_elementos_con_marca_nueva) > 1:
                        for elemento in lista_marcas_nuevas:
                            file.write(
                                f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')    


    elif opcion == "12":  # salir
        salida = input("Confirma salida?: s/n: ")
        if salida == "s" or "S":
            break
    os.system("pause")  # pausa el sistema para ver los resultados
