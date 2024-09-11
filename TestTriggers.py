import time
from pylsl import StreamInfo, StreamOutlet

# Crear el stream LSL con el nombre "test_triggers"
info = StreamInfo(name='test_triggers', type='Markers', channel_count=1, channel_format='string', source_id='test_triggers_id')
outlet = StreamOutlet(info)

def fishing_trial_routine():
    outlet.push_sample(["start_trial"])
    print("sending: start_trial")
    time.sleep(5)

    outlet.push_sample(["open_scene"])
    print("sending: open_scene")
    time.sleep(15)

    outlet.push_sample(["3"])  # Extensión RA
    print("sending: lower_right_arm")
    time.sleep(15)

    outlet.push_sample(["2"])  # Flexión RA
    print("sending: rise_right_arm")
    time.sleep(15)    

    outlet.push_sample(["1"])  # Extensión LA
    print("sending: lower_left_arm")
    time.sleep(15)

    outlet.push_sample(["0"])  # Flexión LA
    print("sending: rise_left_arm")
    time.sleep(15)

    outlet.push_sample(["close_scene"])
    print("sending: close_scene")
    time.sleep(1)

    outlet.push_sample(["end_trial"])
    print("sending: end_trial")
    time.sleep(5)

def run_trials(repetitions):
    for i in range(repetitions):
        print(f"\nRunning trial {i + 1}/{repetitions}")
        fishing_trial_routine()
        time.sleep(5)  # Espera opcional entre repeticiones de las pruebas

def display_menu():
    print("###########################################")
    print("#         Test Fishing Triggers           #")
    print("###########################################")
    
    # Preguntar cuántas veces se requiere repetir el experimento
    while True:
        try:
            repetitions = int(input("\n¿Cuántas veces deseas repetir el experimento? "))
            if repetitions > 0:
                break
            else:
                print("Por favor, introduce un número mayor que 0.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    # Esperar a que el usuario presione Enter para comenzar la prueba
    input("\nPresiona Enter para comenzar el experimento...")

    return repetitions

if __name__ == "__main__":
    # Mostrar el menú
    repetitions = display_menu()

    # Ejecutar las pruebas
    run_trials(repetitions)
