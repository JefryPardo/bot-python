from firebasedatabase import FirebaseDB

fb_bd = FirebaseDB()

usuario = {
    'nombre': 'jeff',
    'edad': '29'
}

fb_bd.write_record('/usuario',  usuario)