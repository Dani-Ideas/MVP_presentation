#/home/dani-ideas/IdeaProjects/Cronogam_process/
from datetime import datetime as dt

class Employee:
    def __init__(self, id, name, workStartHour, workStartMinute, workEndHour, workEndMinute, lineMonitor, lineNoMonitor):
        self.id = id  # Dato simple
        self.name = name  # Dato simple
        self.workStartTime = dt(dt.now().year, dt.now().month, dt.now().day, workStartHour, workStartMinute)
        self.workEndTime = dt(dt.now().year, dt.now().month, dt.now().day, workEndHour, workEndMinute)
        self.lineMonitor = lineMonitor  # Lista bidimensional
        self.lineNoMonitor = lineNoMonitor  # Lista bidimensional
    
    def mostrar_procesos(self):
        for fila in self.lineMonitor:
            fecha = fila[0].strftime('%Y-%m-%d %H:%M')
            detalles = fila[1]
            print(f"Fecha: {fecha}, Detalles: {detalles}")
