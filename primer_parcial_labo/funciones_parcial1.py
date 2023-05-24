import json
import csv

lista=[]
lista_marca=[]

def mostrar_menu(): #Menu del programa
    opcion=""
    print("****************** MENU *****************")
    print("1 - Cargar datos desde archivo") #Esta opción permite cargar el contenido del archivo "Insumos.csv" en una colección
    print("2 - Listar cantidad por marca")
    print("3 - Listar insumos por marca")
    print("4 - Buscar insumo por característica")
    print("5 - Listar insumos ordenados")# ASCENDENTE ante marcas iguales, por precio descendente.
    print("6 - Realizar compras")
    print("7 - Guardar en formato JSON") #Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra Alimento"
    print("8 - Leer desde formato JSON")# y listar insumos"
    print("9 - Actualizar precios")
    print("10 - Agregar un nuevo producto a la lista")
    print("11 - Guardar todos los datos actualizados incluye las altas (.csv o .json)")
    print("12 - Salir del programa")
    print("****************** MENU *****************")
    while True:
        opcion = input("Ingrese una opción para continuar: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 11:
            break
        else:
            print("Error: Ingrese nuevamente una opción válida (1 al 11).")
    return opcion


#Muestra todas las marcas y la cantidad .de insumos correspondientes a cada una
def mostrar_cantidad_por_marca(lista:list, key):
    for elemento in lista:
        lista_marca.append(elemento[key].lower())
    lista_marca_sin_repetir=set(lista_marca)

    for marca in lista_marca_sin_repetir:
        retepiciones=lista_marca.count(marca)
        if retepiciones>1:
            print(marca, "tiene", retepiciones, "insumos")
        else:
            print(marca, "tiene", retepiciones, "insumo")

#---------------- 3 ----------------------
#PARA CADA MARCA: EL NOMBRE Y PRECIO DE LOS INSUMOS

def mostrar_marca_y_precios(lista:list, key):
    for elemento in lista:
        lista_marca.append(elemento[key].lower())
    lista_marca_sin_repetir=set(lista_marca)
    for marca in lista_marca_sin_repetir:
        print("\n--------------",marca,"------------------\n")
        for elemento in lista:
            if marca == elemento[key].lower():
                print(elemento["NOMBRE"], elemento["PRECIO"])

#El usuario ingresa una característica (por ejemplo, "Sin Granos") 
#y se listarán todos los insumos que poseen dicha característica

def mostrar_por_caracteristica(lista:list, key):
    caracteristica_ingresada=input("ingrese caracteristica: ")
    #validar ingreso de caracteristica
    validacion=0
    while validacion==0:
        for elemento in lista:
            if str(caracteristica_ingresada).lower() in str(elemento[key]).lower():
                validacion+=1
        if validacion==0:
            caracteristica_ingresada=input("Error! ingrese caracteristica: ")
        else:
            break

    print(caracteristica_ingresada)
    for elemento in lista:
        if str(caracteristica_ingresada).lower() in str(elemento[key]).lower():
            print(elemento)

#ordenados por marca de forma ascendente (A-Z) y, ante marcas iguales, por precio descendente.
def ordenar_listas_dict(lista: list, key: str, ascendente=True)->list:
    tamaño_lista = len(lista)
    for i in range(tamaño_lista-1):
        for j in range(i+1, tamaño_lista):
            if (lista[i][key]).isdigit():
                if (ascendente and float(lista[i][key]) > float(lista[j][key])) or (not ascendente and float(lista[i][key]) < float(lista[j][key])):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
            else:
                if (ascendente and lista[i][key] > lista[j][key]) or (not ascendente and lista[i][key] < lista[j][key]):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
    for i in range(tamaño_lista-1):
        for j in range(i+1, tamaño_lista):
            if (lista[i][key]==lista[j][key] and lista[i]["PRECIO"]<lista[j]["PRECIO"]):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
    for elemento in lista:
        caracteristica=elemento["CARACTERISTICAS"]
        caracteristica = caracteristica.split("~", 1)
        if len(caracteristica) > 1:
            resultado = caracteristica[0]
        else:
            resultado = caracteristica
        print(elemento["ID"], elemento["MARCA"], elemento["PRECIO"], resultado)

#Leer desde formato JSON: Permite mostrar un listado de los insumos guardados en el archivo JSON generado en la opción anterior.
def mostrar_elementos_js(lista:list)->list:
    with open("primer_parcial_labo\productos.json", "r") as file: #abro el archivo productos.js, lo recorro y convierto en lista de diccionarios 
        lista = []
        lista_elementos0 = []
        lista_elementos_js = []
        for linea in file: 
            lista.append(linea.replace("\n", ""))
        for linea in lista:
            lista_elementos0.append(linea.split(","))
        for elemento in lista_elementos0:
            lista_elementos_js.append({"ID": elemento[0], "NOMBRE": elemento[1],
                                "MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})
    print(lista_elementos_js)

#Actualizar precios: Aplica un aumento del 8.4% a todos los productos Los productos actualizados se guardan en el archivo "Insumos.csv".
def actualizar_precios(lista:list, key:str, porcentaje:float)->list:

    for elemento in lista:
        print(f"{'Precio anterior: '}             {elemento[key]}")
        elemento[key]=str(elemento[key]).replace("$","")
        elemento[key]=float(elemento[key])+(float(elemento[key])*porcentaje/100)
        #print(f"{'Precio con aumento del: '} {porcentaje}{'%'} {'$'}{elemento[key]:2f}")

