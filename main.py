# ==========================================================
# CALCULADORA DE AREAS Y CENTROIDES
# Aplicación para Ingeniería Civil
# ==========================================================


from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import math



# ==========================================================
# CALCULOS GEOMETRICOS
# ==========================================================


def calcular_poligono(puntos):

    figura = Polygon(puntos)

    area = figura.area

    centroide = figura.centroid

    cx = centroide.x
    cy = centroide.y

    return area, cx, cy



def calcular_circulo(radio):

    area = math.pi * radio**2

    cx = 0
    cy = 0

    return area, cx, cy



# ==========================================================
# GRAFICAS
# ==========================================================


def graficar_poligono(puntos, cx, cy, area):


    x = []
    y = []


    for punto in puntos:

        x.append(punto[0])
        y.append(punto[1])


    # cerrar figura

    x.append(x[0])
    y.append(y[0])


    plt.figure(figsize=(8,8))


    plt.plot(
        x,
        y,
        linewidth=2
    )


    plt.fill(
        x,
        y,
        alpha=0.3
    )


    # Centroide

    plt.scatter(
        cx,
        cy,
        s=120,
        label="Centroide"
    )


    plt.text(
        cx,
        cy,
        f"\nC({cx:.3f},{cy:.3f})"
    )


    # Area en la grafica

    plt.text(
        min(x),
        max(y),
        f"Área = {area:.4f} m²",
        fontsize=12
    )


    plt.title(
        "Área y Centroide de Sección"
    )


    plt.xlabel(
        "Eje X (m)"
    )


    plt.ylabel(
        "Eje Y (m)"
    )


    plt.grid()


    plt.axis(
        "equal"
    )


    plt.legend()


    plt.show()





def graficar_circulo(radio,cx,cy,area):


    figura = plt.Circle(
        (0,0),
        radio,
        alpha=0.3
    )


    plt.figure(figsize=(8,8))


    ax = plt.gca()


    ax.add_patch(
        figura
    )


    plt.scatter(
        cx,
        cy,
        s=120,
        label="Centroide"
    )


    plt.text(
        cx,
        cy,
        " Centroide"
    )


    plt.text(
        -radio,
        radio,
        f"Área = {area:.4f} m²"
    )


    plt.title(
        "Área y Centroide del Círculo"
    )


    plt.xlabel(
        "Eje X (m)"
    )


    plt.ylabel(
        "Eje Y (m)"
    )


    plt.grid()


    plt.axis(
        "equal"
    )


    plt.legend()


    plt.show()




# ==========================================================
# MENU PRINCIPAL
# ==========================================================



while True:


    print("\n")
    print("======================================")
    print(" CALCULADORA DE CENTROIDES CIVIL ")
    print("======================================")


    print("""
Seleccione la figura:

1. Rectángulo
2. Triángulo
3. Círculo
4. Figura mediante coordenadas

""")


    opcion = int(
        input("Ingrese opción: ")
    )



    # ------------------------------------------------------
    # RECTANGULO
    # ------------------------------------------------------


    if opcion == 1:


        base = float(
            input("Base (m): ")
        )


        altura = float(
            input("Altura (m): ")
        )


        puntos=[

            (0,0),
            (base,0),
            (base,altura),
            (0,altura)

        ]


        area,cx,cy = calcular_poligono(
            puntos
        )


        graficar_poligono(
            puntos,
            cx,
            cy,
            area
        )



    # ------------------------------------------------------
    # TRIANGULO
    # ------------------------------------------------------


    elif opcion == 2:


        base=float(
            input("Base (m): ")
        )


        altura=float(
            input("Altura (m): ")
        )


        puntos=[

            (0,0),
            (base,0),
            (base/2,altura)

        ]


        area,cx,cy = calcular_poligono(
            puntos
        )


        graficar_poligono(
            puntos,
            cx,
            cy,
            area
        )



    # ------------------------------------------------------
    # CIRCULO
    # ------------------------------------------------------


    elif opcion == 3:


        radio=float(
            input("Radio (m): ")
        )


        area,cx,cy = calcular_circulo(
            radio
        )


        graficar_circulo(
            radio,
            cx,
            cy,
            area
        )



    # ------------------------------------------------------
    # FIGURA LIBRE
    # ------------------------------------------------------


    elif opcion == 4:


        cantidad=int(
            input(
            "Número de vértices: "
            )
        )


        puntos=[]


        for i in range(cantidad):


            print(
                "\nVertice",
                i+1
            )


            x=float(
                input("X: ")
            )


            y=float(
                input("Y: ")
            )


            puntos.append(
                (x,y)
            )



        area,cx,cy = calcular_poligono(
            puntos
        )


        graficar_poligono(
            puntos,
            cx,
            cy,
            area
        )



    else:

        print(
            "Opción incorrecta"
        )

        continue



    # RESULTADOS


    print("\n==============================")
    print(" RESULTADOS")
    print("==============================")


    print(
        f"Área = {area:.4f} m²"
    )


    print(
        f"Centroide X = {cx:.4f} m"
    )


    print(
        f"Centroide Y = {cy:.4f} m"
    )



    print("==============================")


    continuar=input(
        "\n¿Desea calcular otra figura? (s/n): "
    )


    if continuar.lower() != "s":

        print(
            "\nPrograma terminado."
        )

        break
    