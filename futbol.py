class JugadorFutbol:

  def __init__(self, nombre, edad, posicion, equipo, pais, numero_camiseta):
    self.nombre = nombre
    self.edad = edad
    self.posicion = posicion
    self.equipo = equipo
    self.pais = pais
    self.numero_camiseta = numero_camiseta
    self.estadisticas = {
        "goles": 0,
        "asistencias": 0,
        "amarillas": 0,
        "rojas": 0
    }
    self.premios = []

  def actualizar_informacion(self, **kwargs):
    for key, value in kwargs.items():
      if hasattr(self, key):
        if key == 'estadisticas':
          self.estadisticas.update(value)
        else:
          setattr(self, key, value)

  def calcular_promedio_goles(self):
    return self.estadisticas["goles"] / 10

  def es_goleador(self):
    return self.estadisticas["goles"] > 20

  def agregar_premio(self, premio):
    self.premios.append(premio)

  def eliminar_premio(self, premio):
    if premio in self.premios:
      self.premios.remove(premio)

  def marcar_gol(self, cantidad_goles=1):
    self.estadisticas["goles"] += cantidad_goles


jugadores = []

while True:
  print("\n--- Menú ---")
  print("1. Crear nuevo jugador")
  print("2. Mostrar información de un jugador existente")
  print("3. Actualizar información de un jugador existente")
  print("4. Registrar goles de un jugador")
  print("5. Verificar si un jugador es un goleador")
  print("6. Agregar un premio o reconocimiento a un jugador")
  print("7. Eliminar un premio o reconocimiento de un jugador")
  print("8. Salir")

  opcion = input("Ingrese una opción: ")

  if opcion == "1":
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador: "))
    posicion = input("Ingrese la posición del jugador: ")
    equipo = input("Ingrese el equipo del jugador: ")
    pais = input("Ingrese el país de origen del jugador: ")
    numero_camiseta = int(input("Ingrese el número de camiseta del jugador: "))
    jugador_nuevo = JugadorFutbol(nombre, edad, posicion, equipo, pais,
                                  numero_camiseta)
    jugadores.append(jugador_nuevo)
    print("Jugador creado correctamente.")

  elif opcion == "2":
    if jugadores:
      nombre_jugador = input("Ingrese el nombre del jugador: ")
      jugador_encontrado = next(
          (jugador
           for jugador in jugadores if jugador.nombre == nombre_jugador), None)
      if jugador_encontrado:
        print("\nInformación del jugador:")
        print(f"Nombre: {jugador_encontrado.nombre}")
        print(f"Edad: {jugador_encontrado.edad}")
        print(f"Posición: {jugador_encontrado.posicion}")
        print(f"Equipo: {jugador_encontrado.equipo}")
        print(f"País: {jugador_encontrado.pais}")
        print(f"Número de camiseta: {jugador_encontrado.numero_camiseta}")
        print(f"Estadísticas: {jugador_encontrado.estadisticas}")
        print(f"Premios: {jugador_encontrado.premios}")
      else:
        print("Jugador no encontrado.")
    else:
      print("No hay jugadores registrados.")

  elif opcion == "3":
    if jugadores:
      nombre_jugador = input("Ingrese el nombre del jugador: ")
      jugador_encontrado = next(
          (jugador
           for jugador in jugadores if jugador.nombre == nombre_jugador), None)
      if jugador_encontrado:
        opcion_actualizar = input(
            "¿Qué información desea actualizar? (nombre/edad/posicion/equipo/pais/numero_camiseta): "
        )
        if hasattr(jugador_encontrado, opcion_actualizar):
          valor_actualizado = input(
              f"Ingrese el nuevo valor para {opcion_actualizar}: ")
          setattr(jugador_encontrado, opcion_actualizar, valor_actualizado)
          print("Información actualizada correctamente.")
        else:
          print("Opción inválida.")
      else:
        print("Jugador no encontrado.")
    else:
      print("No hay jugadores registrados.")

  elif opcion == "4":
    if jugadores:
      nombre_jugador = input("Ingrese el nombre del jugador: ")
      jugador_encontrado = next(
          (jugador
           for jugador in jugadores if jugador.nombre == nombre_jugador), None)
      if jugador_encontrado:
        cantidad_goles = int(
            input("Ingrese la cantidad de goles que marcó el jugador: "))
        jugador_encontrado.marcar_gol(cantidad_goles)
        print("Goles registrados correctamente.")
      else:
        print("Jugador no encontrado.")
    else:
      print("No hay jugadores registrados.")

  elif opcion == "5":
    if jugadores:
      nombre_jugador = input("Ingrese el nombre del jugador: ")
      jugador_encontrado = next(
          (jugador
           for jugador in jugadores if jugador.nombre == nombre_jugador), None)
      if jugador_encontrado:
        if jugador_encontrado.es_goleador():
          print(f"{jugador_encontrado.nombre} es un goleador.")
        else:
          print(f"{jugador_encontrado.nombre} no es un goleador.")
      else:
        print("Jugador no encontrado.")
    else:
      print("No hay jugadores registrados.")

  elif opcion == "6":
    if jugadores:
      nombre_jugador = input("Ingrese el nombre del jugador: ")
      jugador_encontrado = next(
          (jugador
           for jugador in jugadores if jugador.nombre == nombre_jugador), None)
      if jugador_encontrado:
        premio = input("Ingrese el premio o reconocimiento a agregar: ")
        jugador_encontrado.agregar_premio(premio)
        print("Premio agregado correctamente.")
      else:
        print("Jugador no encontrado.")
    else:
      print("No hay jugadores registrados.")

  elif opcion == "7":
    if jugadores:
      nombre_jugador = input("Ingrese el nombre del jugador: ")
      jugador_encontrado = next(
          (jugador
           for jugador in jugadores if jugador.nombre == nombre_jugador), None)
      if jugador_encontrado:
        premio = input("Ingrese el premio o reconocimiento a eliminar: ")
        jugador_encontrado.eliminar_premio(premio)
        print("Premio eliminado correctamente.")
      else:
        print("Jugador no encontrado.")
    else:
      print("No hay jugadores registrados.")

  elif opcion == "8":
    break

  else:
    print("Opción no válida. Por favor, elija una opción del menú.")

 