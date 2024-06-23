import time
import consulta_precios
import BD.consultas as consultas

def main():
    time.sleep(5)
    items = consultas.select_all_items()
    
    posicion_nombre_item = 2 
    posicion_id = 0

    

    for item in items:

        print(item[0])
        print(item[1])
        print(item[2])
        print(item[3])

        consulta_precios.consultar_precio(
            item[posicion_id],
            item[posicion_nombre_item]
        )



if __name__ == "__main__":
    main()