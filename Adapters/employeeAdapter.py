import json
from datetime import datetime as dt
from MVP.GUI.Models.Employee import Employee

class EmployeeAdapter:
    @staticmethod
    def from_json(json_data):
        # Cargar el JSON
        data = json.loads(json_data)

        # Procesar workStart y workEnd
        workStartHour = data['workStartHour']
        workStartMinute = data['workStartMinute']
        workEndHour = data['workEndHour']
        workEndMinute = data['workEndMinute']

        # Procesar lineMonitor y lineNoMonitor
        lineMonitor = EmployeeAdapter._process_line_data(data['lineMonitor'])
        lineNoMonitor = EmployeeAdapter._process_line_data(data['lineNoMonitor'])

        # Retornar el objeto Employee
        return Employee(
            id=data['id'],
            name=data['name'],
            workStartHour=workStartHour,
            workStartMinute=workStartMinute,
            workEndHour=workEndHour,
            workEndMinute=workEndMinute,
            lineMonitor=lineMonitor,
            lineNoMonitor=lineNoMonitor
        )

    @staticmethod
    def _process_line_data(line_data):
        array_bidimensional = []
        for timestamp, details in line_data.items():
            # Convertir el timestamp a objeto datetime
            fecha = dt.fromisoformat(timestamp)
            # Agregar la fecha y los detalles al array bidimensional
            array_bidimensional.append([fecha, details])
        return array_bidimensional

    @staticmethod
    def to_json(employee):
        # Convertir el objeto Employee a JSON
        return json.dumps(employee.__dict__)

