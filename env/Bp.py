import pyodbc

 

# Conexión a la BD de Access

cnxn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\william\OneDrive\Documentos\env\TallerDB.accdb;")

cursor = cnxn.cursor()

# Creación de tablas

cursor.execute("""CREATE TABLE Estudiantes (id COUNTER PRIMARY KEY, nombre VARCHAR(50), apellido VARCHAR(50), edad INT )""")
cursor.execute(""" CREATE TABLE Cursos ( id COUNTER PRIMARY KEY,nombre_curso VARCHAR(100),id_estudiante INT,FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id))""")


# Insertar datos de ejemplo
cursor.execute("INSERT INTO Estudiantes (nombre, apellido, edad) VALUES ('Juan', 'Perez', 18)")
cursor.execute("INSERT INTO Cursos (nombre_curso, id_estudiante) VALUES ('Python', 1)")
cursor.execute("INSERT INTO Cursos (nombre_curso, id_estudiante) VALUES ('Java', 1)")
cnxn.commit()