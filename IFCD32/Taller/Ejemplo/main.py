import MySQLdb

# Datos de conexión a la base de datos
host = 'localhost'
port = 32768
usuario = 'root'
contraseña = '12345'
base_datos = 'Prueba1'

try:
    # Establecer conexión a la base de datos
    conexion = MySQLdb.connect(host=host, port=port, user=usuario, passwd=contraseña, db=base_datos)
    
    # Crear un objeto cursor para ejecutar consultas
    cursor = conexion.cursor()
    
    # Borrar la tabla si ya existe
    cursor.execute("DROP TABLE IF EXISTS tabla_creada")
    
    print("Tabla borrada correctamente.")
    
    # Sentencia SQL para crear la tabla
    sentencia = '''
    CREATE TABLE tabla_creada (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(255),
        edad INT,
        estatura FLOAT
    )
    '''
    
    # Ejecutar la sentencia SQL
    cursor.execute(sentencia)
    
    print("Tabla creada correctamente.")
    
     # Agregar registros a la tabla
    registros = [
        ("Juan", 25, 1.75),
        ("María", 30, 1.68),
        ("Carlos", 40, 1.80)
    ]
    
    # Sentencia SQL para insertar registros
    sentencia = "INSERT INTO tabla_creada (nombre, edad, estatura) VALUES (%s, %s, %s)"
    
    # Ejecutar la sentencia SQL para cada registro
    cursor.executemany(sentencia, registros)
        
    print("Registros agregados correctamente.")
    
    # Sentencia SQL para borrar el segundo registro
    sentencia = "DELETE FROM tabla_creada WHERE id = 2"
    
    # Ejecutar la sentencia SQL
    cursor.execute(sentencia)
    
    print("Segundo registro borrado correctamente.")
    
    # Datos para actualizar el primer registro
    nuevo_nombre = 'Rosa'
    nueva_edad = 33
    nueva_estatura = 1.80
    
    # Sentencia SQL para actualizar el primer registro
    sentencia = "UPDATE tabla_creada SET nombre = %s, edad = %s, estatura = %s WHERE id = 1"
    
    # Ejecutar la sentencia SQL
    cursor.execute(sentencia, (nuevo_nombre, nueva_edad, nueva_estatura))
    
    
    print("Primer registro actualizado correctamente.")
    
     # Sentencia SQL para consultar la tabla ordenada por nombre
    sentencia = "SELECT * FROM tabla_creada ORDER BY nombre"
    
    # Ejecutar la sentencia SQL
    cursor.execute(sentencia)
    
    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()
    
    # Recorrer los resultados e imprimirlos
    for fila in resultados:
        print(fila)
    
    # Confirmar los cambios en la base de datos
    conexion.commit()
    
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    
except MySQLdb.Error as error:
    print("Error de la base de datos:", error)