from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from app import app, db   #,ma

#—---
# defino las tablas
class Libro(db.Model):   # la clase Libro hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    titulo=db.Column(db.String(100))
    autor=db.Column(db.String(100))
    genero=db.Column(db.String(100))
    anio_publicacion=db.Column(db.Integer)
    cantidad=db.Column(db.Integer)
    imagen=db.Column(db.String(1000))
    def __init__(self,titulo,autor,genero,anio_publicacion,cantidad,imagen): #crea el  constructor de la clase
        self.titulo=titulo # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.autor=autor
        self.genero=genero
        self.anio_publicacion=anio_publicacion
        self.cantidad=cantidad
        self.imagen=imagen


    #  si hay que crear mas tablas , se hace aqui


with app.app_context():
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas
#  ************************************************************