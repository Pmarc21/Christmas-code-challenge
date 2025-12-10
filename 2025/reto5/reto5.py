'''
Los elfos tienen un timestamp secreto: es la fecha y hora exacta en la que 
Papá Noel despega con el trineo 🛷 para repartir regalos por el mundo. 
Pero en el Polo Norte usan un formato rarísimo para guardar la hora: YYYY*MM*DD@HH|mm|ss NP (ejemplo: 2025*12*25@00|00|00 NP).

Tu misión es escribir una función que reciba:

fromTime → fecha de referencia en formato elfo (YYYY*MM*DD@HH|mm|ss NP).
takeOffTime → la misma fecha de despegue, también en formato elfo.
La función debe devolver:

Los segundos completos que faltan para el despegue.
Si ya estamos en el despegue exacto → 0.
Si el despegue ya ocurrió → un número negativo indicando cuántos segundos han pasado desde entonces.
🎯 Reglas
Convierte el formato elfo a un timestamp primero. El sufijo NP indica la hora oficial del Polo Norte (sin husos horarios ni DST), así que puedes tratarlo como si fuera UTC.
Usa diferencias en segundos, no en milisegundos.
Redondea siempre hacia abajo (floor): solo segundos completos.
'''
from datetime import datetime
from math import floor
def time_until_take_off(from_time: str, take_off_time: str) -> int:
  from_time_norm = from_time.replace("*","-").replace("@", " ").replace("|", ":").replace(" NP", "")
  from_time_aux = datetime.strptime(from_time_norm, "%Y-%m-%d %H:%M:%S")
  from_time_aux_2 = from_time_aux.timestamp()

  take_off_time_norm = take_off_time.replace("*","-").replace("@", " ").replace("|", ":").replace(" NP", "")
  take_off_time_aux = datetime.strptime(take_off_time_norm, "%Y-%m-%d %H:%M:%S")
  take_off_time_aux_2 = take_off_time_aux.timestamp()
  return floor(take_off_time_aux_2 - from_time_aux_2)

from_time = "2025*12*25@00|00|00 NP"
take_off_time = "2025*12*24@12|00|00 NP"
time_until_take_off(from_time, take_off_time)