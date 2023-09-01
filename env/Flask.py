from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\william\OneDrive\Documentos\env\TallerDB.accdb;")

 
print("Conectado a BD")

cursor = conn.cursor()

def get_estudiantes():

    cursor.execute("SELECT * FROM Estudiantes")

    estudiantes = cursor.fetchall()

    return estudiantes


def get_cursos():
    cursor.execute("SELECT * FROM Cursos")
    cursos = cursor.fetchall()
    return cursos

# Rutas

@app.route('/')
def index():
    return f"<h1>estudiantes</h1><p>{estudiantes}<h1>cursos</h1><p>{cursos}</p>"

@app.route('/estudiantes.html')
def estudiantes():
    estudiantes = get_estudiantes()
    return render_template('estudiantes.html', estudiantes=estudiantes)

@app.route('/cursos.html')  
def cursos():
    cursos = get_cursos()
    return render_template('cursos.html', cursos=cursos)


if __name__ == "__main__":

    app.run(debug=True)