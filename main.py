from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from routes.heuristicproblemsroutes import hproblems
from models.heuristicowner import HeuristicOwner

app = Flask(__name__)
app.register_blueprint(hproblems)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/usabilitydb'  # ajusta según tu configuración
db = SQLAlchemy(app)


class DesignOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    designtests = db.relationship('DesignQuestionnaires', backref='owner', lazy=True)

class DesignQuestionnaires(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('design_owner.id'), nullable=False)
    question = db.Column(db.String(250), nullable=False)
    answers = db.Column(db.String(250), nullable=False)

class HeuristicOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    checklists = db.relationship('HeuristicCheckList', backref='owner', lazy=True)

class HeuristicEvaluations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('heuristic_owner.id'), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    hi = db.Column(db.String(250), nullable=False)
    incidents = db.Column(db.Integer, nullable=False)
    severity = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    criticism = db.Column(db.Integer, nullable=False)


class HeuristicDescriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)


class HeuristicCheckList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('heuristic_owner.id'), nullable=False)
    H01P01 = db.Column(db.Boolean, nullable=False)
    H01P02 = db.Column(db.Boolean, nullable=False)
    H01P03 = db.Column(db.Boolean, nullable=False)
    H01P04 = db.Column(db.Boolean, nullable=False)
    H01P05 = db.Column(db.Boolean, nullable=False)
    H01P06 = db.Column(db.Boolean, nullable=False)
    H01P07 = db.Column(db.Boolean, nullable=False)

    H02P01 = db.Column(db.Boolean, nullable=False)
    H02P02 = db.Column(db.Boolean, nullable=False)
    H02P03 = db.Column(db.Boolean, nullable=False)
    H02P04 = db.Column(db.Boolean, nullable=False)
    H02P05 = db.Column(db.Boolean, nullable=False)
    H02P06 = db.Column(db.Boolean, nullable=False)
    H02P07 = db.Column(db.Boolean, nullable=False)
    H02P08 = db.Column(db.Boolean, nullable=False)

    H03P01 = db.Column(db.Boolean, nullable=False)
    H03P02 = db.Column(db.Boolean, nullable=False)
    H03P03 = db.Column(db.Boolean, nullable=False)
    H03P04 = db.Column(db.Boolean, nullable=False)
    H03P05 = db.Column(db.Boolean, nullable=False)
    H03P06 = db.Column(db.Boolean, nullable=False)
    H03P06 = db.Column(db.Boolean, nullable=False)
    H04P01 = db.Column(db.Boolean, nullable=False)
    H04P02 = db.Column(db.Boolean, nullable=False)
    H04P03 = db.Column(db.Boolean, nullable=False)
    H04P04 = db.Column(db.Boolean, nullable=False)
    H04P05 = db.Column(db.Boolean, nullable=False)
    H04P06 = db.Column(db.Boolean, nullable=False)
    H04P07 = db.Column(db.Boolean, nullable=False)
    H04P08 = db.Column(db.Boolean, nullable=False)
    H04P09 = db.Column(db.Boolean, nullable=False)
    H04P10 = db.Column(db.Boolean, nullable=False)
    H04P11 = db.Column(db.Boolean, nullable=False)
    H04P12 = db.Column(db.Boolean, nullable=False)
    H04P13 = db.Column(db.Boolean, nullable=False)
    H05P01 = db.Column(db.Boolean, nullable=False)
    H05P02 = db.Column(db.Boolean, nullable=False)
    H05P03 = db.Column(db.Boolean, nullable=False)
    H05P04 = db.Column(db.Boolean, nullable=False)
    H05P05 = db.Column(db.Boolean, nullable=False)
    H06P01 = db.Column(db.Boolean, nullable=False)
    H06P02 = db.Column(db.Boolean, nullable=False)
    H06P03 = db.Column(db.Boolean, nullable=False)
    H07P01 = db.Column(db.Boolean, nullable=False)
    H07P02 = db.Column(db.Boolean, nullable=False)
    H07P03 = db.Column(db.Boolean, nullable=False)
    H07P04 = db.Column(db.Boolean, nullable=False)
    H07P05 = db.Column(db.Boolean, nullable=False)
    H07P06 = db.Column(db.Boolean, nullable=False)
    H07P07 = db.Column(db.Boolean, nullable=False)
    H08P01 = db.Column(db.Boolean, nullable=False)
    H08P02 = db.Column(db.Boolean, nullable=False)
    H08P03 = db.Column(db.Boolean, nullable=False)
    H08P04 = db.Column(db.Boolean, nullable=False)
    H08P05 = db.Column(db.Boolean, nullable=False)
    H08P06 = db.Column(db.Boolean, nullable=False)
    H08P07 = db.Column(db.Boolean, nullable=False)
    H08P08 = db.Column(db.Boolean, nullable=False)
    H08P09 = db.Column(db.Boolean, nullable=False)
    H08P10 = db.Column(db.Boolean, nullable=False)
    H08P11 = db.Column(db.Boolean, nullable=False)
    H09P01 = db.Column(db.Boolean, nullable=False)
    H09P02 = db.Column(db.Boolean, nullable=False)
    H09P03 = db.Column(db.Boolean, nullable=False)
    H09P04 = db.Column(db.Boolean, nullable=False)
    H09P05 = db.Column(db.Boolean, nullable=False)
    H09P06 = db.Column(db.Boolean, nullable=False)
    H10P01 = db.Column(db.Boolean, nullable=False)
    H10P02 = db.Column(db.Boolean, nullable=False)
    H10P03 = db.Column(db.Boolean, nullable=False)
    H10P04 = db.Column(db.Boolean, nullable=False)
    H10P05 = db.Column(db.Boolean, nullable=False)
    H10P06 = db.Column(db.Boolean, nullable=False)
    H10P07 = db.Column(db.Boolean, nullable=False)
    H10P08 = db.Column(db.Boolean, nullable=False)
    H10P09 = db.Column(db.Boolean, nullable=False)
    OBSERVACIONH1 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH2 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH3 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH4 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH5 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH6 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH7 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH8 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH9 = db.Column(db.String(300), nullable=False)
    OBSERVACIONH10 = db.Column(db.String(300), nullable=False)

#rutas para desing
@app.route('/desingtests', methods=['POST'])
def create_desingtest():
    data = request.get_json()
    new_owner = DesignOwner(name=data['name'], url=data['url'], description=data['description'])
    print(new_owner.__dict__)
    db.session.add(new_owner)
    db.session.commit()
    return jsonify({'message': 'Diseño creado correctamente'}), 201

@app.route('/desingtests', methods=['GET'])
def get_desingtest():
    owners = DesignOwner.query.all()
    owners_list = []
    for owner in owners:
        owners_list.append({
            'id': owner.id,
            'name': owner.name,
            'url': owner.url,
            'description': owner.description
        })
    return jsonify({'owners': owners_list}), 200

#ruta questionaries
@app.route('/questionaries', methods=['POST'])
def create_questionary():
    data = request.get_json()
    new_owner = DesignQuestionnaires(name=data['name'], url=data['url'], description=data['description'])
    print(new_owner.__dict__)
    db.session.add(new_owner)
    db.session.commit()
    return jsonify({'message': 'Diseño creado correctamente'}), 201

# Ruta para obtener todos los HeuristicOwners
@app.route('/owners', methods=['GET'])
def get_owners():
    owners = HeuristicOwner.query.all()
    owners_list = []
    for owner in owners:
        owners_list.append({
            'id': owner.id,
            'name': owner.name,
            'url': owner.url,
            'description': owner.description
        })
    return jsonify({'owners': owners_list}), 200


# Ruta para crear un nuevo HeuristicOwner
@app.route('/owners', methods=['POST'])
def create_owner():
    data = request.get_json()
    new_owner = HeuristicOwner(name=data['name'], url=data['url'], description=data['description'])
    print(new_owner.__dict__)
    db.session.add(new_owner)
    db.session.commit()
    return jsonify({'message': 'HeuristicOwner creado correctamente'}), 201


# Ruta para eliminar un HeuristicOwner por ID
@app.route('/owners/<int:id>', methods=['DELETE'])
def delete_owner(id):
    owner = HeuristicOwner.query.get(id)
    if not owner:
        return jsonify({'message': 'HeuristicOwner no encontrado'}), 404

    db.session.delete(owner)
    db.session.commit()
    return jsonify({'message': 'HeuristicOwner eliminado correctamente'}), 200


# Ruta para crear un nuevo HeuristicCheckList asociado a un owner
@app.route('/heuristics', methods=['POST'])
def create_heuristic():
    data = request.get_json()
    owner_id = data.get('owner_id')

    owner = HeuristicOwner.query.get(owner_id)
    if not owner:
        return jsonify({"message": "Owner not found!"}), 404

    heuristic = HeuristicCheckList(owner=owner, **data)
    db.session.add(heuristic)
    db.session.commit()

    return jsonify({"message": "Created successfully!", "id": heuristic.id}), 201


@app.route('/identifyproblems/<int:owner_id>', methods=['GET'])
def identify_problems(owner_id):
    print(owner_id)
    heuristics = HeuristicCheckList.query.filter_by(owner_id=owner_id).all()
    # print(heuristics)
    heuristics_list = []
    for heuristic in heuristics:
        heuristics_list.append({

            'H01P01': heuristic.H01P01,
            'H01P02': heuristic.H01P02,
            'H01P03': heuristic.H01P03,
            'H01P04': heuristic.H01P04,
            'H01P05': heuristic.H01P05,
            'H01P06': heuristic.H01P06,
            'H01P07': heuristic.H01P07,
            'H02P01': heuristic.H02P01,
            'H02P02': heuristic.H02P02,
            'H02P03': heuristic.H02P03,
            'H02P04': heuristic.H02P04,
            'H02P05': heuristic.H02P05,
            'H02P06': heuristic.H02P06,
            'H02P07': heuristic.H02P07,
            'H02P08': heuristic.H02P08,
            'H03P01': heuristic.H03P01,
            'H03P02': heuristic.H03P02,
            'H03P03': heuristic.H03P03,
            'H03P04': heuristic.H03P04,
            'H03P05': heuristic.H03P05,
            'H03P06': heuristic.H03P06,
            'H04P01': heuristic.H04P01,
            'H04P02': heuristic.H04P02,
            'H04P03': heuristic.H04P03,
            'H04P04': heuristic.H04P04,
            'H04P05': heuristic.H04P05,
            'H04P06': heuristic.H04P06,
            'H04P07': heuristic.H04P07,
            'H04P08': heuristic.H04P08,
            'H04P09': heuristic.H04P09,
            'H04P10': heuristic.H04P10,
            'H04P11': heuristic.H04P11,
            'H04P12': heuristic.H04P12,
            'H04P13': heuristic.H04P13,
            'H05P01': heuristic.H05P01,
            'H05P02': heuristic.H05P02,
            'H05P03': heuristic.H05P03,
            'H05P04': heuristic.H05P04,
            'H05P05': heuristic.H05P05,
            'H06P01': heuristic.H06P01,
            'H06P02': heuristic.H06P02,
            'H06P03': heuristic.H06P03,
            'H07P01': heuristic.H07P01,
            'H07P02': heuristic.H07P02,
            'H07P03': heuristic.H07P03,
            'H07P04': heuristic.H07P04,
            'H07P05': heuristic.H07P05,
            'H07P06': heuristic.H07P06,
            'H07P07': heuristic.H07P07,
            'H08P01': heuristic.H08P01,
            'H08P02': heuristic.H08P02,
            'H08P03': heuristic.H08P03,
            'H08P04': heuristic.H08P04,
            'H08P05': heuristic.H08P05,
            'H08P06': heuristic.H08P06,
            'H08P07': heuristic.H08P07,
            'H08P08': heuristic.H08P08,
            'H08P09': heuristic.H08P09,
            'H08P10': heuristic.H08P10,
            'H08P11': heuristic.H08P11,
            'H09P01': heuristic.H09P01,
            'H09P02': heuristic.H09P02,
            'H09P03': heuristic.H09P03,
            'H09P04': heuristic.H09P04,
            'H09P05': heuristic.H09P05,
            'H09P06': heuristic.H09P06,
            'H10P01': heuristic.H10P01,
            'H10P02': heuristic.H10P02,
            'H10P03': heuristic.H10P03,
            'H10P04': heuristic.H10P04,
            'H10P05': heuristic.H10P05,
            'H10P06': heuristic.H10P06,
            'H10P07': heuristic.H10P07,
            'H10P08': heuristic.H10P08,
            'H10P09': heuristic.H10P09,

        })
    # print(heuristics_list)

    false_heuristics_count = {}  # Diccionario para almacenar el recuento de heurísticas falsas

    # Iterar sobre la lista de heurísticas y contar las que son falsas
    for heuristics_dict in heuristics_list:
        for heuristic, value in heuristics_dict.items():
            if not value:  # Si el valor es False
                # Incrementar el recuento en el diccionario o inicializarlo en 1 si es la primera vez que se encuentra
                false_heuristics_count[heuristic] = false_heuristics_count.get(heuristic, 0) + 1

    # Imprimir el recuento de heurísticas falsas
    respuesta = []
    hi = [

        "telacreiste",
        "Visibilidad del estado del sistema",
        "Relación entre el sistema y el mundo real",
        "Control y libertad de usuario",
        "Consistencia y Estándares",
        "Prevención de Errores",
        "Minimizar la carga de memoria del usuario",
        "Flexibilidad y eficiencia de uso ",
        "Diseño estético y minimalista",
        "Ayuda al usuario para reconocer, diagnosticar y recuperarse de errores",
        "Ayuda y Documentación",
    ]
    for heuristic, count in false_heuristics_count.items():
        import re

        descripcion = HeuristicDescriptions.query.filter_by(name=heuristic).first().description
        print(descripcion)
        resultado = re.search(r'h(\d+)', heuristic, re.IGNORECASE)
        hfail = ""
        if resultado:
            numero_despues_de_h = resultado.group(1)
            print(int(numero_despues_de_h))
            hfail = hi[int(numero_despues_de_h)]
            print("Número después de 'h':", numero_despues_de_h)
        else:
            print("No se encontró ningún número después de 'h' en la cadena.")

        respuesta.append({"name": heuristic, "description": descripcion, "hi": hfail, "incidents": count})

    print(respuesta)
    return jsonify(respuesta)

@app.route('/evaluations/<int:owner_id>', methods=['POST'])
def saveEvaluations(owner_id):
    data = request.get_json()
    print(owner_id)
    print(data)

    for evaluation in data:
        ev = HeuristicEvaluations(owner_id=owner_id, **evaluation)
        db.session.add(ev)
        db.session.commit()


    return jsonify({"message":"Guardado Correctamente"})

@app.route('/evaluations/<int:owner_id>', methods=['GET'])
def getEvaluations(owner_id):
    evaluations = HeuristicEvaluations.query.filter_by(owner_id=owner_id).all()
    print(evaluations)
    response=[]
    for evaluation in evaluations:
        response.append({
            'name': evaluation.name,
            'description': evaluation.description,
            'hi': evaluation.hi,
            'incidents': evaluation.incidents,
            'severity': evaluation.severity,
            'frequency': evaluation.frequency,
            'criticism': evaluation.criticism,
        })
    print(response)
    return jsonify(response)

@app.route('/getobservations/<int:owner_id>')
def get_observations(owner_id):
    heuristics = HeuristicCheckList.query.filter_by(owner_id=owner_id).all()
    print(heuristics)
    heuristics_observations_list = []
    for heuristic in heuristics:
        heuristics_observations_list.append({
            "H1": heuristic.OBSERVACIONH1,
            "H2": heuristic.OBSERVACIONH2,
            "H3": heuristic.OBSERVACIONH3,
            "H4": heuristic.OBSERVACIONH4,
            "H5": heuristic.OBSERVACIONH5,
            "H6": heuristic.OBSERVACIONH6,
            "H7": heuristic.OBSERVACIONH7,
            "H8": heuristic.OBSERVACIONH8,
            "H9": heuristic.OBSERVACIONH9,
            "H10": heuristic.OBSERVACIONH10,
        })
    for h in heuristics_observations_list:
        print(h)
    return jsonify(heuristics_observations_list)


# Ruta para obtener todos los HeuristicCheckLists asociados a un owner
@app.route('/owners/<int:owner_id>/heuristics', methods=['GET'])
def get_owner_heuristics(owner_id):
    owner = HeuristicOwner.query.get(owner_id)
    if not owner:
        return jsonify({"message": "Owner not found!"}), 404

    heuristics = HeuristicCheckList.query.filter_by(owner_id=owner_id).all()
    heuristics_list = []
    for heuristic in heuristics:
        heuristics_list.append({
            'id': heuristic.id,
            'H01P01': heuristic.H01P01,
            'H01P02': heuristic.H01P02,
            'H01P03': heuristic.H01P03,
            'H01P04': heuristic.H01P04,
            'H01P05': heuristic.H01P05,
            'H01P06': heuristic.H01P06,
            'H01P07': heuristic.H01P07,
            'H02P01': heuristic.H02P01,
            'H02P02': heuristic.H02P02,
            'H02P03': heuristic.H02P03,
            'H02P04': heuristic.H02P04,
            'H02P05': heuristic.H02P05,
            'H02P06': heuristic.H02P06,
            'H02P07': heuristic.H02P07,
            'H02P08': heuristic.H02P08,
            'H03P01': heuristic.H03P01,
            'H03P02': heuristic.H03P02,
            'H03P03': heuristic.H03P03,
            'H03P04': heuristic.H03P04,
            'H03P05': heuristic.H03P05,
            'H03P06': heuristic.H03P06,
            'H04P01': heuristic.H04P01,
            'H04P02': heuristic.H04P02,
            'H04P03': heuristic.H04P03,
            'H04P04': heuristic.H04P04,
            'H04P05': heuristic.H04P05,
            'H04P06': heuristic.H04P06,
            'H04P07': heuristic.H04P07,
            'H04P08': heuristic.H04P08,
            'H04P09': heuristic.H04P09,
            'H04P10': heuristic.H04P10,
            'H04P11': heuristic.H04P11,
            'H04P12': heuristic.H04P12,
            'H04P13': heuristic.H04P13,
            'H05P01': heuristic.H05P01,
            'H05P02': heuristic.H05P02,
            'H05P03': heuristic.H05P03,
            'H05P04': heuristic.H05P04,
            'H05P05': heuristic.H05P05,
            'H06P01': heuristic.H06P01,
            'H06P02': heuristic.H06P02,
            'H06P03': heuristic.H06P03,
            'H07P01': heuristic.H07P01,
            'H07P02': heuristic.H07P02,
            'H07P03': heuristic.H07P03,
            'H07P04': heuristic.H07P04,
            'H07P05': heuristic.H07P05,
            'H07P06': heuristic.H07P06,
            'H07P07': heuristic.H07P07,
            'H08P01': heuristic.H08P01,
            'H08P02': heuristic.H08P02,
            'H08P03': heuristic.H08P03,
            'H08P04': heuristic.H08P04,
            'H08P05': heuristic.H08P05,
            'H08P06': heuristic.H08P06,
            'H08P07': heuristic.H08P07,
            'H08P08': heuristic.H08P08,
            'H08P09': heuristic.H08P09,
            'H08P10': heuristic.H08P10,
            'H08P11': heuristic.H08P11,
            'H09P01': heuristic.H09P01,
            'H09P02': heuristic.H09P02,
            'H09P03': heuristic.H09P03,
            'H09P04': heuristic.H09P04,
            'H09P05': heuristic.H09P05,
            'H09P06': heuristic.H09P06,
            'H10P01': heuristic.H10P01,
            'H10P02': heuristic.H10P02,
            'H10P03': heuristic.H10P03,
            'H10P04': heuristic.H10P04,
            'H10P05': heuristic.H10P05,
            'H10P06': heuristic.H10P06,
            'H10P07': heuristic.H10P07,
            'H10P08': heuristic.H10P08,
            'H10P09': heuristic.H10P09,
            'OBSERVACIONH1': heuristic.OBSERVACIONH1,
            'OBSERVACIONH2': heuristic.OBSERVACIONH2,
            'OBSERVACIONH3': heuristic.OBSERVACIONH3,
            'OBSERVACIONH4': heuristic.OBSERVACIONH4,
            'OBSERVACIONH5': heuristic.OBSERVACIONH5,
            'OBSERVACIONH6': heuristic.OBSERVACIONH6,
            'OBSERVACIONH7': heuristic.OBSERVACIONH7,
            'OBSERVACIONH8': heuristic.OBSERVACIONH8,
            'OBSERVACIONH9': heuristic.OBSERVACIONH9,
            'OBSERVACIONH10': heuristic.OBSERVACIONH10,
        })

    return jsonify({'heuristics': heuristics_list}), 200


@app.route('/heuristic/<int:id>')
def getheuristicbyid(id):
    heuristic = HeuristicCheckList.query.get(id)
    if not heuristic:
        return jsonify({"message": "heuristic not found!"}), 404
    return jsonify({
        'id': heuristic.id,
        'H01P01': heuristic.H01P01,
        'H01P02': heuristic.H01P02,
        'H01P03': heuristic.H01P03,
        'H01P04': heuristic.H01P04,
        'H01P05': heuristic.H01P05,
        'H01P06': heuristic.H01P06,
        'H01P07': heuristic.H01P07,
        'H02P01': heuristic.H02P01,
        'H02P02': heuristic.H02P02,
        'H02P03': heuristic.H02P03,
        'H02P04': heuristic.H02P04,
        'H02P05': heuristic.H02P05,
        'H02P06': heuristic.H02P06,
        'H02P07': heuristic.H02P07,
        'H02P08': heuristic.H02P08,
        'H03P01': heuristic.H03P01,
        'H03P02': heuristic.H03P02,
        'H03P03': heuristic.H03P03,
        'H03P04': heuristic.H03P04,
        'H03P05': heuristic.H03P05,
        'H03P06': heuristic.H03P06,
        'H04P01': heuristic.H04P01,
        'H04P02': heuristic.H04P02,
        'H04P03': heuristic.H04P03,
        'H04P04': heuristic.H04P04,
        'H04P05': heuristic.H04P05,
        'H04P06': heuristic.H04P06,
        'H04P07': heuristic.H04P07,
        'H04P08': heuristic.H04P08,
        'H04P09': heuristic.H04P09,
        'H04P10': heuristic.H04P10,
        'H04P11': heuristic.H04P11,
        'H04P12': heuristic.H04P12,
        'H04P13': heuristic.H04P13,
        'H05P01': heuristic.H05P01,
        'H05P02': heuristic.H05P02,
        'H05P03': heuristic.H05P03,
        'H05P04': heuristic.H05P04,
        'H05P05': heuristic.H05P05,
        'H06P01': heuristic.H06P01,
        'H06P02': heuristic.H06P02,
        'H06P03': heuristic.H06P03,
        'H07P01': heuristic.H07P01,
        'H07P02': heuristic.H07P02,
        'H07P03': heuristic.H07P03,
        'H07P04': heuristic.H07P04,
        'H07P05': heuristic.H07P05,
        'H07P06': heuristic.H07P06,
        'H07P07': heuristic.H07P07,
        'H08P01': heuristic.H08P01,
        'H08P02': heuristic.H08P02,
        'H08P03': heuristic.H08P03,
        'H08P04': heuristic.H08P04,
        'H08P05': heuristic.H08P05,
        'H08P06': heuristic.H08P06,
        'H08P07': heuristic.H08P07,
        'H08P08': heuristic.H08P08,
        'H08P09': heuristic.H08P09,
        'H08P10': heuristic.H08P10,
        'H08P11': heuristic.H08P11,
        'H09P01': heuristic.H09P01,
        'H09P02': heuristic.H09P02,
        'H09P03': heuristic.H09P03,
        'H09P04': heuristic.H09P04,
        'H09P05': heuristic.H09P05,
        'H09P06': heuristic.H09P06,
        'H10P01': heuristic.H10P01,
        'H10P02': heuristic.H10P02,
        'H10P03': heuristic.H10P03,
        'H10P04': heuristic.H10P04,
        'H10P05': heuristic.H10P05,
        'H10P06': heuristic.H10P06,
        'H10P07': heuristic.H10P07,
        'H10P08': heuristic.H10P08,
        'H10P09': heuristic.H10P09,
        'OBSERVACIONH1': heuristic.OBSERVACIONH1,
        'OBSERVACIONH2': heuristic.OBSERVACIONH2,
        'OBSERVACIONH3': heuristic.OBSERVACIONH3,
        'OBSERVACIONH4': heuristic.OBSERVACIONH4,
        'OBSERVACIONH5': heuristic.OBSERVACIONH5,
        'OBSERVACIONH6': heuristic.OBSERVACIONH6,
        'OBSERVACIONH7': heuristic.OBSERVACIONH7,
        'OBSERVACIONH8': heuristic.OBSERVACIONH8,
        'OBSERVACIONH9': heuristic.OBSERVACIONH9,
        'OBSERVACIONH10': heuristic.OBSERVACIONH10,
    })


# Ruta para obtener un HeuristicCheckList por ID asociado a un owner
@app.route('/owners/<int:owner_id>/heuristics/<int:id>', methods=['GET'])
def get_owner_heuristic(owner_id, id):
    owner = HeuristicOwner.query.get(owner_id)
    if not owner:
        return jsonify({"message": "Owner not found!"}), 404

    heuristic = HeuristicCheckList.query.filter_by(owner_id=owner_id, id=id).first()
    if not heuristic:
        return jsonify({"message": "HeuristicCheckList not found!"}), 404

    return jsonify({
        'id': heuristic.id,
        'OBSERVACIONES': heuristic.OBSERVACIONES,

    }), 200


# Ruta para obtener un HeuristicOwner por ID
@app.route('/owners/<int:id>', methods=['GET'])
def get_owner(id):
    owner = HeuristicOwner.query.get(id)
    if not owner:
        return jsonify({'message': 'HeuristicOwner no encontrado'}), 404
    owner_data = {
        'id': owner.id,
        'name': owner.name,
        'url': owner.url,
        'description': owner.description,
    }
    return jsonify(owner_data), 200


# Ruta para actualizar un HeuristicOwner por ID
@app.route('/owners/<int:id>', methods=['PUT'])
def update_owner(id):
    owner = HeuristicOwner.query.get(id)
    if not owner:
        return jsonify({'message': 'HeuristicOwner no encontrado'}), 404

    data = request.get_json()
    owner.Name = data['name']
    owner.Url = data['url']
    db.session.commit()
    return jsonify({'message': 'HeuristicOwner actualizado correctamente'}), 200


if __name__ == '__main__':
    with app.app_context():
        print("recreando base de datos")
        db.create_all()
    app.run(debug=True)
