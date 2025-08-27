import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import math

print("\nCon este programa se ofrecen 6 simulaciones de principios y modelos físicos entre los que elegir.")

def tiempo_caida_libre():
    """
    MODELO DE CAÍDA LIBRE DE UNA PELOTA QUE REBOTA
    _____________________________________________________
    
    En esta simulación se estudia un modelo de movimiento muy conocido, la caída libre.
    Se elige la altura desde la que se deja caer una pelota la cual rebota hasta otra altura.
    Se tiene en cuenta que el coeficiente de restitución de la pelota, el cual indica el grado de conservación de la energía cinética, es 2^(1/2)/2.
    Cabe recordar que este coeficiente obtiene valores entre 0 y 1. 

    Parámetros: 
    - Altura inicial desde la que se deja caer la pelota (en metros) (float positivo).
    - Gravedad (en m/s^2) (float positivo). 
    - Tiempo de caída (en segundos) (float positivo). 
    - Altura final que alcanza la pelota tras rebotar (en metros) (float positivo). 
    - Coeficiente de restitución (float positivo). 
    
    A partir de este programa es posible insertar una altura inicial de su preferencia y obtener tanto el tiempo que tarda en alcanzar el suelo como la altura que alcanzaría nuevamente tras rebotar. 
    """
    
    altura = float(input("Ingresa la altura en metros: "))
    
    # Control de errores:
    if altura < 0:
        raise ValueError("La altura no puede ser negativa.")
    
    # Fórmulas
    tiempo = np.sqrt((2 * altura) / 9.8)
    h_rebote = altura * (np.sqrt(2)/2)**2 
    
    # Impresión por pantalla
    print(f"\nLa pelota tardaría {tiempo:.2f} segundos en caer en caída libre desde una altura de {altura:.2f} metros.")
    print("Si la pelota rebota ¿que altura alcanzaría?")
    print(f"La pelota alcanzaría una altura de {h_rebote:.2f} metros tras rebotar.")
    print("\nFIN DE LA SIMULACIÓN")

def fuerza_centrifuga_y_centripeta():
    """
    MODELO DE FUERZA CENTRÍFUGA Y CENTRÍPETA DE UN COCHE EN UNA ROTONDA
    _______________________________________________________________________
    
    En esta simulación se estudian las principales fuerzas que actúan en un coche que realiza el recorrido de una rotonda a una velocidad constante.
    
    Parámetros:
    - Radio (en metros) (float positivo)
    - Masa (en Kilogramos) (float positivo)
    - Velocidad (en m/s) (float positivo)
    """
    
    velocidad = float(input("Ingresa la velocidad del coche en m/s: "))
    radio = 15
    masa = 1500
    
    if velocidad < 0:
        raise ValueError("La velocidad no puede ser negativa.")
    
    # Cálculo de fuerzas
    fuerza_centrifuga = (masa * velocidad**2) / radio
    fuerza_centripeta = fuerza_centrifuga  # Son iguales en magnitud
    
    print(f"La fuerza centrifuga del coche es {fuerza_centrifuga:.2f} Newtons")
    print(f"La fuerza centrípeta es {fuerza_centripeta:.2f} Newtons")
    print("La fuerza centrífuga y la centrípeta tienen el mismo valor ya que se trata de un movimiento circular uniforme.")
    
    # Mostrar imagen
    response = requests.get('https://i.pinimg.com/564x/cd/71/22/cd712279ea0dd776a826af18afdf8dca.jpg')
    img = Image.open(BytesIO(response.content))
    img.show()
    
    print("\nFIN DE LA SIMULACIÓN")

def ley_de_snell():
    """
    LEY DE SNELL
    _____________________________________
    
    Un rayo de luz incide desde el aire con un determinado ángulo de incidencia y atraviesa el agua con otro grado de refracción.
    """
    
    angulo_incidencia = float(input("Ingresa el ángulo de incidencia en grados: "))
    indice_aire = 1
    indice_agua = 1.333

    # Control de errores
    if angulo_incidencia <= 0:
        raise ValueError("El ángulo de incidencia ha de ser positivo.")
    if angulo_incidencia >= 90:
        raise ValueError("El ángulo de incidencia ha de ser mayor que 0 y menor que 90.")
    
    # Cálculo del ángulo de refracción
    angulo_refraccion = math.degrees(math.asin(math.sin(math.radians(angulo_incidencia)) * indice_aire / indice_agua))
    print(f"\nSi el rayo incide con un ángulo de {angulo_incidencia}º entonces el ángulo de refracción será {angulo_refraccion:.3f}º.")

    # Tabla de valores
    print("\nTabla de valores:")
    print("| Ángulo de incidencia | Ángulo de refracción |")
    print("|----------------------|----------------------|")
    for ang in [10, 20, 30, 40, 50]:
        ang_ref = math.degrees(math.asin(math.sin(math.radians(ang)) * indice_aire / indice_agua))
        print(f"| {ang}°                  | {ang_ref:.2f}°                |")
    
    print("\nFIN DE LA SIMULACIÓN")

def longitud_muelle_estirado():
    """
    MODELO DE ESTIRAMIENTO DE UN MUELLE POR UNA FUERZA (Ley de Hooke)
    ___________________________________________________
    """
    
    Li = float(input("Introduce una longitud inicial de un muelle en metros: "))
    F = float(input("Introduce también una fuerza aplicable al muelle en N: "))
    constante_elasticidad = 21.68

    if F < 0:
        raise ValueError("La fuerza no puede ser negativa.")
    
    # Cálculo de la elongación (corrección de la fórmula)
    elongacion = F / constante_elasticidad
    Lf = Li + elongacion
    
    print(f"El muelle se alarga {elongacion:.3f} m tras aplicar la fuerza de {F} Newtons")
    print(f"La longitud final del muelle es {Lf:.3f} m")
    print("\nFIN DE LA SIMULACIÓN")

def tercera_ley_de_kepler():
    """
    MODELO DE UN PLANETA ORBITANTE (Tercera Ley de Kepler)
    _________________________________
    """
    
    radio = float(input("Introduce el radio en metros de la órbita: "))
    masa_estrella = float(input("Introduce la masa en kg de tu estrella: "))
    G = 6.67e-11

    if radio <= 0:
        raise ValueError("El radio debe ser mayor que 0")
    if masa_estrella <= 0:
        raise ValueError("La masa debe ser mayor a 0")
    
    # Cálculo corregido del período orbital
    T = np.sqrt((4 * np.pi**2 * radio**3) / (G * masa_estrella))
    T_dias = T / (24 * 3600)  # Convertir a días
    
    print(f"El planeta tarda {T_dias:.2f} días en completar una órbita alrededor de la estrella")
    
    answer = input("¿Desea ver un gráfico de la órbita? (s/n): ")
    if answer.lower() == 's':
        # Gráfico de la órbita
        theta = np.linspace(0, 2 * np.pi, 100)
        x = radio * np.cos(theta)
        y = radio * np.sin(theta)
        
        plt.figure(figsize=(8, 8))
        plt.plot(x, y, label='Órbita')
        plt.plot(0, 0, 'yo', markersize=20, label='Estrella')
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
        plt.title('Órbita Planetaria')
        plt.axis('equal')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    print("\nFIN DE LA SIMULACIÓN")

def efecto_Doppler():
    """
    VARIACIÓN DE LA FRECUENCIA DE ONDA (Efecto Doppler)
    ___________________________________________________
    """
    
    frecuencia_foco = float(input("Introduce el valor de la frecuencia emitida por el foco (Hz): "))
    velocidad_foco = float(input("Introduce la velocidad de la fuente (m/s). Positiva si se acerca, negativa si se aleja: "))
    V = 340  # Velocidad del sonido en m/s (más realista que 300,000,000 m/s)

    if frecuencia_foco <= 0:
        raise ValueError("La frecuencia debe ser mayor que 0")
    
    # Cálculo corregido del efecto Doppler
    if velocidad_foco > 0:  # Fuente se acerca
        frecuencia_percibida = frecuencia_foco * (V / (V - velocidad_foco))
    else:  # Fuente se aleja
        frecuencia_percibida = frecuencia_foco * (V / (V + abs(velocidad_foco)))
    
    print(f"La frecuencia percibida por el observador es {frecuencia_percibida:.2f} Hz")
    
    answer = input("¿Desea ver una imagen explicativa del efecto Doppler? (s/n): ")
    if answer.lower() == 's':
        try:
            response = requests.get('https://significado.com/img/cien/efecto-doppler-onda-sonido.jpg')
            img = Image.open(BytesIO(response.content))
            img.show()
        except:
            print("No se pudo cargar la imagen")
    
    print("\nFIN DE LA SIMULACIÓN")

# Menú principal
while True:
    print("\n" + "="*50)
    print("SIMULADOR DE PRINCIPIOS FÍSICOS")
    print("="*50)
    print("\nSeleccione el principio físico sobre el que desea aprender:")
    print("1. Caída libre de una pelota que rebota")
    print("2. Fuerza centrífuga y centrípeta")
    print("3. Ley de Snell (refracción)")
    print("4. Ley de Hooke (estiramiento de muelle)")
    print("5. Tercera Ley de Kepler (órbitas)")
    print("6. Efecto Doppler")
    print("0. Salir")

    try:
        opcion = int(input("\nSelecciona una opción: "))
        
        if opcion == 0:
            print("¡Gracias por usar el simulador!")
            break
        elif opcion == 1:
            tiempo_caida_libre()
        elif opcion == 2:
            fuerza_centrifuga_y_centripeta()
        elif opcion == 3:
            ley_de_snell()
        elif opcion == 4:
            longitud_muelle_estirado()
        elif opcion == 5:
            tercera_ley_de_kepler()
        elif opcion == 6:
            efecto_Doppler()
        else:
            print("Opción inválida. Por favor, elige una opción del 0 al 6.")
    
    except ValueError:
        print("Por favor, introduce un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    print("\n" + "-"*50)