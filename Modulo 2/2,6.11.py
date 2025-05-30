hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
minn = mins + dura
hora = hour + mins // 60
minn = mins % 60
hora = hour % 24
print(hora, ":", minn, sep='')
