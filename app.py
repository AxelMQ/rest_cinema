from flask import Flask, jsonify, request

app = Flask(__name__)

#importar datos desde cartelera
from cartelera import cartelera

@app.route('/')
def welcome():
    return jsonify({
        "message": "welcome.json"
    })

@app.route('/cartelera')
def getCartelera():
    return jsonify({
        "message": "Cartelera's list",
        "cartelera": cartelera
    })

@app.route('/cartelera/<string:pelicula_name>')
def getPelicula(pelicula_name):
    peliculaFound = [pelicula for pelicula in cartelera if pelicula['pelicula'] == pelicula_name]
    if (len(peliculaFound) > 0):
        return jsonify({
            "message": "Pelicula Found",
            "pelicula": peliculaFound[0]
        })
    return jsonify({"message": "Pelicula Not Found"})

@app.route('/cartelera/duration/<int:duration_pelicula>')
def durationPelicula(duration_pelicula):
    peliculaFound = [pelicula for pelicula in cartelera if pelicula['duration'] >= duration_pelicula]
    if (len(peliculaFound) > 0):
        return jsonify ({
            "message": "Pelicula's duration",
            "pelicula": peliculaFound
        })
    return jsonify ({
        "message": "Pelicula Not Found"
    })

@app.route('/cartelera/genero/<string:genero_pelicula>')    
def generoPelicula(genero_pelicula):
    peliculaFound = [pelicula for pelicula in cartelera if pelicula['genero'] == genero_pelicula]
    if peliculaFound:
        return jsonify({
            "message": "Pelicula Found (Genero)",
            "pelicula": peliculaFound
        })
    return jsonify({
        "message": "Pelicula Not found..."
    })

@app.route('/cartelera', methods=['POST'])
def addPelicula():
    new_pelicula = {
        "pelicula": request.json['pelicula'],
        "genero": request.json['genero'],
        "duration": request.json['duration']
    }
    cartelera.append(new_pelicula)
    return jsonify({
        "message": "Pelicula added Succesfully",
        "pelicula": cartelera
    })

@app.route('/cartelera/<string:pelicula_name>', methods=['PUT'])
def updatePelicula(pelicula_name):
    peliculaFound = [pelicula for pelicula in cartelera if pelicula['pelicula'] == pelicula_name]
    if (len(peliculaFound) > 0):
        peliculaFound[0]['pelicula'] = request.json['pelicula'],
        peliculaFound[0]['genero'] = request.json['genero'],
        peliculaFound[0]['duration'] =  request.json['duration'],
        return jsonify({
            "message": "Pelicula Update",
            "cartelera": peliculaFound[0]
        })
    return jsonify({
        "message": "Pelicula Not Found"
    })

@app.route('/cartelera/<string:pelicula_name>', methods=['DELETE'])
def deletePelicula(pelicula_name):
    peliculaFound = [pelicula for pelicula in cartelera if pelicula['pelicula'] == pelicula_name]
    if (len(peliculaFound) > 0):
        cartelera.remove(peliculaFound[0])
        return jsonify({
            "message": "Pelicula Deleted",
            "cartelera": cartelera
        })
    return jsonify({
        "message": "Pelicula Not Found"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)