#/home/dani-ideas/IdeaProjects/Cronogam_process/
from datetime import datetime as dt
class EmployeeModel:
    def __init__(self, id, employee_name,workStartHour, workStartMinute, workEndHour, workEndMinute, lineMonitor, lineNoMonitor):
        self.id = id  # Dato simple
        self.name = employee_name
        self.workStartTime = dt(dt.now().year, dt.now().month, dt.now().day, workStartHour, workStartMinute)
        self.workEndTime = dt(dt.now().year, dt.now().month, dt.now().day, workEndHour, workEndMinute)
        self.lineMonitor = lineMonitor  # Lista bidimensional
        self.lineNoMonitor = lineNoMonitor  # Lista bidimensional

    def get_name(self):
        return self.name

    def set_nombre_usuario(self, new_employee_name):
        self.name = new_employee_name

    def get_workStartTime(self):
        return self.workStartTime
    
    def get_workEndTime(self):
        return self.workEndTime
    
    def get_lineMonitor(self):
        return self.lineMonitor
    
    def mostrar_procesos(self):
        for fila in self.lineMonitor:
            fecha = fila[0].strftime('%Y-%m-%d %H:%M')
            detalles = fila[1]
            print(f"Fecha: {fecha}, Detalles: {detalles}")