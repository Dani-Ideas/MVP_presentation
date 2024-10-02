class ProcessModel:
    def __init__(self, id_process, name, id_block_Process, need_monitoring, standardtime_minutes, simulan):
        self.idProcess = id_process
        self.nameProcess = name
        self.idBlockProcess = id_block_Process
        self.needMonitoring = need_monitoring
        self.standardTimeMinutes = standardtime_minutes
        self.simulanProcess = simulan

    def __repr__(self):
        return f"ProcessModel({self.idProcess}, {self.nameProcess}, {self.idBlockProcess}, {self.needMonitoring}, {self.standardTimeMinutes}, {self.simulanProcess})"
