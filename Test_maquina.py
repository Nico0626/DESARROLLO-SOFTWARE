import pytest
from Maquina_coser import MaquinaDeCoser  # Asegúrate de que el nombre del archivo sea correcto

@pytest.fixture
def maquina():
    return MaquinaDeCoser(modelo='ModeloX', color_hilo='rojo', velocidad=1000, centimetros_hilo=50)

def test_encender(maquina):
    resultado = maquina.encender()
    assert resultado == "Máquina encendida"
    assert maquina.estado == 'encendida'

def test_encender_ya_encendida(maquina):
    maquina.encender()  # Encendemos la máquina
    with pytest.raises(ValueError, match="La máquina ya está encendida"):
        maquina.encender()

def test_apagar(maquina):
    maquina.encender()  # Encendemos la máquina primero
    resultado = maquina.apagar()
    assert resultado == "Máquina apagada"
    assert maquina.estado == 'apagada'

def test_apagar_ya_apagada(maquina):
    with pytest.raises(ValueError, match="La máquina ya está apagada"):
        maquina.apagar()

def test_empezar_cocer(maquina):
    maquina.encender()  # Encendemos la máquina primero
    resultado = maquina.empezar_cocer()
    assert resultado == "La máquina ModeloX está cociendo"
    assert maquina.estado == 'cociendo'

def test_empezar_cocer_apagada(maquina):
    with pytest.raises(ValueError, match="La máquina está apagada"):
        maquina.empezar_cocer()

def test_parar_cocer(maquina):
    maquina.encender()  # Encendemos la máquina
    maquina.empezar_cocer()  # Ponemos en modo cociendo
    resultado = maquina.parar_cocer()
    assert resultado == "La máquina ModeloX ha dejado de coser y está encendida"
    assert maquina.estado == 'encendida'

def test_parar_cocer_no_cociendo(maquina):
    maquina.encender()  # Encendemos la máquina
    with pytest.raises(ValueError, match="La máquina no está cociendo"):
        maquina.parar_cocer()

def test_cambiar_hilo(maquina):
    resultado = maquina.cambiar_hilo('verde')
    assert resultado == "El hilo se cambió al color verde"
    assert maquina.color_hilo == 'verde'

def test_puntadas_realizadas(maquina):
    maquina.encender()  # Encendemos la máquina
    maquina.empezar_cocer()  # Ponemos en modo cociendo
    maquina.cambiar_hilo('verde')  # Cambiamos el hilo a verde
    resultado = maquina.puntadas_realizadas(15)
    assert resultado == "Se hicieron 15 puntadas\nQuedan 45.0 cm de hilo (verde)"
    assert maquina.puntadas == 15
    assert maquina.centimetros_hilo == 45.0

def test_puntadas_realizadas_sin_hilo(maquina):
    maquina.encender()  # Encendemos la máquina
    maquina.empezar_cocer()  # Ponemos en modo cociendo
    maquina.centimetros_hilo = 1
    with pytest.raises(ValueError, match="No hay suficiente hilo"):
        maquina.puntadas_realizadas(10)

def test_puntadas_realizadas_maquina_apagada(maquina):
    with pytest.raises(ValueError, match="La máquina está apagada o no está en modo cociendo"):
        maquina.puntadas_realizadas(10)

def test_estado_maquina(maquina):
    maquina.encender()  # Encendemos la máquina
    maquina.empezar_cocer()  # Ponemos en modo cociendo
    expected_output = (
        "Modelo: ModeloX\n"
        "Estado: cociendo\n"
        "Color de hilo: rojo\n"
        "Velocidad: 1000\n"
        "Puntadas realizadas: 0\n"
        "Hilo restante: 50 cm"
    )
    assert str(maquina) == (expected_output)
    
def test_str_method(maquina):
    maquina.encender()  # Encendemos la máquina
    maquina.cambiar_hilo('verde')
    expected_output = (
        "Modelo: ModeloX\n"
        "Estado: encendida\n"
        "Color de hilo: verde\n"
        "Velocidad: 1000\n"
        "Puntadas realizadas: 0\n"
        "Hilo restante: 50 cm"
    )
    assert str(maquina) == expected_output

def test_aumento_velocidad(maquina):
    maquina.encender()
    assert maquina.velocidad == 1000
    resultado = maquina.aumentar_velocidad(100)
    assert maquina.velocidad == 1100
    assert resultado == "Velocidad ajustada a 1100 rpm"
    


def test_disminuir_velocidad(maquina):
    maquina.encender()
    assert maquina.velocidad == 1000
    resultado = maquina.disminuir_velocidad(100)
    assert maquina.velocidad == 900
    assert resultado == "Velocidad ajustada a 900 rpm"

   