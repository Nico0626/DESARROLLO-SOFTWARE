class MaquinaDeCoser:
    def __init__(self, modelo, color_hilo, velocidad):
        self.estado = 'apagada'
        self.modelo = modelo
        self.color_hilo = color_hilo
        self.velocidad = velocidad
        self.puntadas = 3
        self.centimetros_hilo = 1000
        self.velocidad_maxima=2000
        self.velocidad_minima=100


    def encender(self):
        if self.estado == 'apagada':
            self.estado = 'encendida'
            return "Máquina encendida"
        else:
            raise ValueError("La máquina ya está encendida")

    def apagar(self):
        if self.estado == 'encendida':
            self.estado = 'apagada'
            return "Máquina apagada"
        else:
            raise ValueError("La máquina ya está apagada")
        
    def empezar_cocer(self):
        if self.estado == 'encendida':
            self.estado = 'cociendo'
            return f"La máquina {self.modelo} está cociendo"
        elif self.estado == 'apagada':
            raise ValueError("La máquina está apagada")
        elif self.estado == 'cociendo':
            raise ValueError("La máquina ya está cociendo")
        
    def parar_cocer(self):
        if self.estado == 'cociendo':
            self.estado = 'encendida'
            return f"La máquina {self.modelo} ha dejado de coser y está encendida"
        elif self.estado == 'encendida':
            raise ValueError("La máquina no está cociendo")
        elif self.estado == 'apagada':
            raise ValueError("La máquina está apagada")
        
    def cambiar_hilo(self, nuevo_color):
        self.color_hilo = nuevo_color
        return f"El hilo se cambió al color {nuevo_color}"
    
    def puntadas_realizadas(self, cantidad):
        if self.estado == 'cociendo':
            cm_usados = cantidad / 3
            if self.centimetros_hilo >= cm_usados:
                self.puntadas += cantidad
                self.centimetros_hilo -= cm_usados
                return f"Se hicieron {cantidad} puntadas\nQuedan {self.centimetros_hilo} cm de hilo ({self.color_hilo})"
            else:
                raise ValueError("No hay suficiente hilo")
        else:
            raise ValueError("La máquina está apagada o no está en modo cociendo")
        
    def __str__(self):
        return (f"Modelo: {self.modelo}\n"
                f"Estado: {self.estado}\n"
                f"Color de hilo: {self.color_hilo}\n"
                f"Velocidad: {self.velocidad}\n"
                f"Puntadas realizadas: {self.puntadas}\n"
                f"Hilo restante: {self.centimetros_hilo} cm")
    
    def estado_maquina(self): 
        return self.__str__()
    
    def aumentar_velocidad(self, aumento):
        nuevaVelocidad=self.velocidad + aumento
        if self.estado== "encendida":
            if nuevaVelocidad >= self.velocidad_minima and nuevaVelocidad <= self.velocidad_maxima:
                self.velocidad=nuevaVelocidad
                return f"Velocidad ajustada a {self.velocidad} rpm"
            else:
                raise ValueError ("La maquina no soporta esa velocidad")
        else:
            raise ValueError ("Encienda la maquina primero")
        
    def disminuir_velocidad(self, decremento):
        nuevaVelocidad=self.velocidad - decremento
        if self.estado== "encendida":
            if nuevaVelocidad >= self.velocidad_minima and nuevaVelocidad <= self.velocidad_maxima:
                self.velocidad=nuevaVelocidad
                return f"Velocidad ajustada a {self.velocidad} rpm"
            else:
                raise ValueError ("La maquina no soporta esa velocidad")
        else:
            raise ValueError ("Encienda la maquina primero")
        

        
