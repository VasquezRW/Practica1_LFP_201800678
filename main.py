from tkinter import *
from tkinter.filedialog import askopenfilename

comando = []


def escoger_archivo():
    ruta = Tk()
    a = askopenfilename()
    ruta.withdraw()
    return a


def leer_archivo(archivo):
    with open(archivo) as fichero:
        for linea in fichero.readlines():
            comando.append(linea)
        pass


def separar_comas(lista):
    palabra = []
    for p in lista.split(","):
        palabra.append(p)
    return palabra


def imprimir(vector):
    for elemento in vector:
        print(elemento)


def separar_lineas(vector):
    a = []
    for fil in vector:
        a.append(fil.strip("\n").split("="))
    for fila in a:
        elem = fila[1]
        ord = fila[1].find("ORDENAR")
        bus = fila[1].find("BUSCAR")
        if bus != -1 & ord == -1:
            fin = fila[1].find("BUSCAR")
            fila.append("BUSCAR")
            numeros = ''.join(elem[:fin - 1].strip().split())
            numerosBuscar = ''.join(elem[fin + 6:].strip().split())
            fila[1] = numeros
            fila.append(numerosBuscar)
        elif ord != -1 & bus == -1:
            fin = fila[1].find("ORDENAR")
            fila.append("ORDENAR")
            numeros = ''.join(elem[:fin - 1].strip().split())
            fila[1] = numeros
        elif ord != -1 & bus != -1:
            fin = fila[1].find("ORDENAR")
            fila.append("ORDENAR")
            numeros = ''.join(elem[:fin - 1].strip().split())
            instrucciones = elem[fin:].strip()
            fila[1] = numeros
            indice = instrucciones.find("BUSCAR")
            fila.append("BUSCAR")
            fila.append(''.join(instrucciones[indice + 6:].strip().split()))
        else:
            print("algo pazo :v")
    return a


def imprimirOrdenadas():
    print("Desplegar Listas Ordenadas")
    for linea in comando:
        for elemento in linea:
            if elemento == "ORDENAR":
                numeros = separar_comas(linea[1])
                nombreLista = linea[0]
                num = ','.join(sorted(numeros))
                print(nombreLista + ": ORDENADOS = " + num, end="\n")


def imprimirBusquedas():
    print("Desplegar Busquedas")
    for linea in comando:
        for elemento in linea:
            if elemento == "BUSCAR":
                numeros = separar_comas(linea[1])
                numeroBuscar = linea[len(linea) - 1]
                nombreLista = linea[0]
                num = ','.join(numeros)
                posiciones = buscarNum(numeros, numeroBuscar)
                if not is_empty(posiciones):
                    pos = ','.join(map(str, posiciones))
                    print(nombreLista + " = " + num + " BUSQUEDA POSICIONES = " + pos, end="\n")
                else:
                    print(nombreLista + " = " + num + " BUSQUEDA POSICIONES = NO ENCONTRADO", end="\n")


def is_empty(data_structure):
    if data_structure:
        return False
    else:
        return True


def buscarNum(vector, num):
    posiciones = []
    for i in range(0, (len(vector) - 1)):
        if vector[i] == num:
            posiciones.append(i)
    return posiciones


def is_ordenar(vector):
    for elemento in vector:
        if elemento == "ORDENAR":
            return True
    return False


def is_buscar(vector):
    for elemento in vector:
        if elemento == "BUSCAR":
            return True
    return False


def imptimir_todo():
    for linea in comando:
        ord = is_ordenar(linea)
        bus = is_buscar(linea)
        numeros = separar_comas(linea[1])
        nombreLista = linea[0]

        if ord is True and bus is False:
            print("Ordenar y no buscar")
            num = ','.join(ordenarAscendente(numeros))
            print(nombreLista + ": ORDENADO = " + num, end="\n")
        elif ord is False and bus is True:
            print("No Ordenar y buscar")
            numeroBuscar = linea[len(linea) - 1]
            num = ','.join(numeros)
            posiciones = buscarNum(numeros, numeroBuscar)
            if not is_empty(posiciones):
                pos = ','.join(map(str, posiciones))
                print(nombreLista + " = " + num + " | BUSQUEDA: POSICIONES = " + pos, end="\n")
            else:
                print(nombreLista + " = " + num + " | BUSQUEDA: POSICIONES = NO ENCONTRADO", end="\n")
        elif ord is True and bus is True:
            print("Ordenar y buscar")
            numeroBuscar = linea[len(linea) - 1]
            num = ','.join(ordenarAscendente(numeros))
            posiciones = buscarNum(numeros, numeroBuscar)
            if not is_empty(posiciones):
                pos = ','.join(map(str, posiciones))
                print(nombreLista + " ORDENADO =" + num + " | BUSQUEDA: POSICIONES = " + pos, end="\n")
            else:
                print(nombreLista + " ORDENADO =" + num + " | BUSQUEDA: POSICIONES = NO ENCONTRADO", end="\n")
        else:
            print("No Ordenar y no buscar")
            num = ','.join(numeros)
            print(nombreLista + ": " + num, end="\n")


def ordenarAscendente(vector):
    for i in range (len(vector)):
        for j in range(0, len(vector) - 1):
            if vector[j] > vector[j + 1]:
                temp = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = temp
    return vector


def desplegarHTML():
    f = open('tabla.html', 'w')

    inicio = """<html>
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <nav class="navbar navbar-dark bg-dark">
      <a class="navbar-brand">
        <img src="usacIcono.png" width="100" height="100">
        
      </a>
      <a class="navbar-brand">
      <h2><b> Wilmer Estuardo Vasquez Raxon - 2018000678 </b></h2>
      </a>
    </nav>
    </head>
    <body>"""
    f.write(inicio)
    datos = """
    
    
    <br>
    <br>
    \n"""
    f.write(datos)
    f.write("""
    <div class="container" style="text-align: center;"><h4 > <b> DATOS OPERADOS DEL ARCHIVO SELECCIONADO </b> <h4></div>
    <br>
    <div class="container" style="text-align: center;" > <ul class="list-group">""")

    for linea in comando:
        f.write("<br>")
        ord = is_ordenar(linea)
        bus = is_buscar(linea)
        numeros = separar_comas(linea[1])
        nombreLista = linea[0]

        if ord is True and bus is False:
            print("Ordenar y no buscar")
            num = ','.join(ordenarAscendente(numeros))
            f.write("""<li class="list-group-item">""")
            f.write(nombreLista + ": | ORDENADO = " + num + "\n")
            f.write("</li>")
        elif ord is False and bus is True:
            print("No Ordenar y buscar")
            numeroBuscar = linea[len(linea) - 1]
            num = ','.join(numeros)
            posiciones = buscarNum(numeros, numeroBuscar)
            if not is_empty(posiciones):
                pos = ','.join(map(str, posiciones))
                f.write("""<li class="list-group-item">""")
                f.write(nombreLista + " = " + num + " | BUSQUEDA: POSICIONES = " + pos + "\n")
                f.write("</li>")
            else:
                f.write("""<li class="list-group-item">""")
                f.write(nombreLista + " = " + num + " | BUSQUEDA: POSICIONES = NO ENCONTRADO\n")
                f.write("</li>")
        elif ord is True and bus is True:
            print("Ordenar y buscar")
            numeroBuscar = linea[len(linea) - 1]
            num = ','.join(ordenarAscendente(numeros))
            posiciones = buscarNum(numeros, numeroBuscar)
            if not is_empty(posiciones):
                pos = ','.join(map(str, posiciones))
                f.write("""<li class="list-group-item">""")
                f.write(nombreLista + " | ORDENADO =" + num + " | BUSQUEDA: POSICIONES = " + pos + "\n")
                f.write("</li>")
            else:
                f.write("""<li class="list-group-item">""")
                f.write(nombreLista + " | ORDENADO =" + num + " | BUSQUEDA: POSICIONES = NO ENCONTRADO\n")
                f.write("</li>")
        else:
            print("No Ordenar y no buscar")
            num = ','.join(numeros)
            f.write("""<li class="list-group-item">""")
            f.write(nombreLista + ": " + num + "\n")
            f.write("</li>")
    f.write('\n</ul> </div> \n')
    fin = """</body>
        </html>"""
    f.write(fin)
    f.close()


if __name__ == '__main__':
    op = None
    while op != 6:
        print("----------------------------------")
        print("Bienvenido a Practica 1")
        print("1. Cargar Archivo")
        print("2. Desplegar Listas Ordenadas")
        print("3. Deplegar Busquedas")
        print("4. Deplegar Todas")
        print("5. Deplegar Todas a Archivo")
        print("6. Salir")
        print("----------------------------------")
        op = int(input())
        if op == 1:
            print("----------------------------------")
            print("Cargar Archivo")
            ruta = escoger_archivo()
            leer_archivo(ruta)
            print()
            print(ruta)
            print()
            imprimir(comando)
            print("----------------------------------")
            comando = separar_lineas(comando)
            imprimir(comando)
            print("----------------------------------")
        elif op == 2:
            print("----------------------------------")
            imprimirOrdenadas()
            print("----------------------------------")
        elif op == 3:
            print("----------------------------------")
            imprimirBusquedas()
            print("----------------------------------")
        elif op == 4:
            print("----------------------------------")
            imptimir_todo()
            print("----------------------------------")
        elif op == 5:
            print("----------------------------------")
            desplegarHTML()
            print("----------------------------------")
        elif op == 6:
            print("----------------------------------")
        else:
            print("nose :v")
