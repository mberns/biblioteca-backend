from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request
import traceback


from app import app, db,ma
from modelos.libro_modelo import *


class LibroSchema(ma.Schema):
    class Meta:
        fields=('id','titulo','autor','genero','anio_publicacion','cantidad','imagen')

libro_schema=LibroSchema()  # El objeto producto_schema es para traer un producto
libros_schema=LibroSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto


# crea los endpoint o rutas (json)
'''
@app.route('/libros',methods=['GET'])
def get_Libros():
    all_libros=Libro.query.all() # el metodo query.all() lo hereda de db.Model
    result=libro_schema.dump(all_libros)  #el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)     # retorna un JSON de todos los registros de la tabla
'''

@app.route('/libros/<id>',methods=['GET'])
def get_libro(id):
    libro=Libro.query.get(id)
    return libro_schema.jsonify(libro)   # retorna el JSON de un producto recibido como parametro
'''
@app.route('/libros/<id>',methods=['DELETE'])
def delete_libro(id):
    libro=Libro.query.get(id)
    db.session.delete(libro)
    db.session.commit()                     # confirma el delete
    return libro_schema.jsonify(libro) # me devuelve un json con el registro eliminado
'''
    

# Método POST para crear un nuevo libro
@app.route('/libros', methods=['POST'])
def create_libro():
    if not request.json:
        return jsonify({"error": "No input data provided"}), 400

    data = request.json
    required_fields = ['titulo', 'autor', 'genero', 'anio_publicacion', 'cantidad', 'imagen']
    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        titulo = data['titulo']
        autor = data['autor']
        genero = data['genero']
        anio_publicacion = data['anio_publicacion']
        cantidad = data['cantidad']
        imagen = data['imagen']
    
        new_libro = Libro(titulo, autor, genero, anio_publicacion, cantidad, imagen)
        db.session.add(new_libro)
        db.session.commit()
    
        result = libro_schema.dump(new_libro)
        return jsonify(result), 201
    except Exception as e:
        print(traceback.format_exc())  # Imprime el traceback completo en los registros del servidor
        return jsonify({"error": str(e)}), 500

# Método GET para obtener todos los libros
@app.route('/libros', methods=['GET'])
def get_libros():
    try:
        all_libros = Libro.query.all()
        result = libros_schema.dump(all_libros)
        return jsonify(result), 200
    except Exception as e:
        print(traceback.format_exc())  # Imprime el traceback completo en los registros del servidor
        return jsonify({"error": str(e)}), 500

# Método DELETE para eliminar un libro por ID
@app.route('/libros/<id>', methods=['DELETE'])
def delete_libro(id):
    try:
        libro = Libro.query.get(id)
        if libro is None:
            return jsonify({"error": "Libro not found"}), 404
        
        db.session.delete(libro)
        db.session.commit()
        
        return jsonify({"message": "Libro deleted successfully"}), 200
    except Exception as e:
        print(traceback.format_exc())  # Imprime el traceback completo en los registros del servidor
        return jsonify({"error": str(e)}), 500



'''
@app.route('/libros', methods=['POST']) # crea ruta o endpoint
def create_libro():
    #print(request.json)  # request.json contiene el json que envio el cliente
    titulo=request.json['titulo']
    autor=request.json['autor']
    genero=request.json['genero']
    anio_publicacion=request.json['anio_publicacion']
    cantidad=request.json['cantidad']
    imagen=request.json['imagen']
    new_libro=Libro(titulo,autor,genero,anio_publicacion,cantidad,imagen)
    db.session.add(new_libro)
    db.session.commit() # confirma el alta
    return libro_schema.jsonify(new_libro)
'''
    

#self,titulo,autor,genero,anio_publicacion,cantidad,imagen
@app.route('/libros/<id>' ,methods=['PUT'])
def update_libro(id):
    libro=Libro.query.get(id)
 
    libro.titulo=request.json['titulo']
    libro.autor=request.json['autor']
    libro.genero=request.json['genero']
    libro.anio_publicacion=request.json['anio_publicacion']
    libro.cantidad=request.json['cantidad']
    libro.imagen=request.json['imagen']


    db.session.commit()    # confirma el cambio
    return libro_schema.jsonify(libro)    # y retorna un json con el producto


@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON de un usuario recibido como parametro