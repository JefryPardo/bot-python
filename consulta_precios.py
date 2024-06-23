
import utils.tareas as tareas
import time
import BD.consultas as consultas
from datetime import datetime


def consultar_precio(id,nombre_item):
    
    tareas.limpiar_input_store()
    print(nombre_item)
    tareas.escribir_texto(nombre_item)
    tareas.buscar_item()

    unidades = tareas.get_unidades_en_venta_slot1()
    time.sleep(1)
    precio = tareas.get_precio_slot1()

    print('unidades: ',unidades)
    print('precio: ',precio)
    print('/////////')
    print()

    consultas.insert_into_flipping(
        unidades,
        datetime.now(),
        precio,
        id
    )
