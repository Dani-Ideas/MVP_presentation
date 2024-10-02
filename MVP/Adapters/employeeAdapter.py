import json
from datetime import datetime as dt
from GUI.Models.EmplyeeModel import EmployeeModel
from GUI.Models.ProcessModel import ProcessModel

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
        return EmployeeModel(
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
            # Crear una instancia de ProcessModel con los detalles
            process = ProcessModel(
                id_process=details["id_process"],
                name=details["name"],
                id_block_Process=details["id_block_Process"],
                need_monitoring=details["need_monitoring"],
                standardtime_minutes=details["standardtime_minutes"],
                simulan=details["simulan"]
            )
            # Agregar la fecha y el objeto ProcessModel al array bidimensional
            array_bidimensional.append([fecha, process])
        return array_bidimensional

    @staticmethod
    def to_json(employee):
        # Convertir el objeto Employee a JSON
        return json.dumps(employee.__dict__)

