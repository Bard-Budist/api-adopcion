
from models.animal import Animal
from models.genero import Genero
from models.vacunas import Vacunas
from models.aperado import Operado


from models.usuario import Usuario
from models.posting import Posting
from models.info import Info
from datetime import datetime

from models import storage
from routes import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/info/', methods=['GET'], strict_slashes=False)
def get_Info():
   
    animal = Animal()
    genero = Genero()
    vacunas = Vacunas()
    operado = Operado()
    
    animal = storage.all(Animal)
    genero = storage.all(Genero)
    vacunas = storage.all(Vacunas)
    operado = storage.all(Operado)

    listaGrande = {}

    listaGrande["Animal"]=listaObjetos(animal)
    listaGrande["Genero"]=listaObjetos(genero)
    listaGrande["Vacunas"]=listaObjetos(vacunas)
    listaGrande["Operado"]=listaObjetos(operado)

    return jsonify(listaGrande)
    
@app_views.route('/info/', methods=['POST'], strict_slashes=False)
def create_Info():
    data = request.get_json(force=True)
    if not data:
        abort(400)
    data['data']['imagen'] = bytes(data['data']['imagen'], 'utf8')    
    instance = Info(**data['data'])
    instance.save()
    create_Posting(data['data']['id_user'])
    return make_response({'status': 'ok'}, 201)

def create_Posting(id):
    info = storage.all(Info)
    for key, value in info.items():
        rs = value.to_dict()
        maxValue = rs['id']
    post = Posting()
    post.usuario = id
    post.info = maxValue
    post.fecha = datetime.now()
    post.estado = 4
    post.save()

def listaObjetos(result):
    lista = []
    for rs in result.values():
        lista.append(rs.to_dict())
        
    return lista


@app_views.route('/posting/', methods=['GET'], strict_slashes=False)
def getPosting():
    postings = storage.all(Posting)

    info_data = []
    for posting in postings.values():
        info = storage.get(Info, posting.info)
        user = storage.get(Usuario, posting.usuario)
        data_dict = info.to_dict()
        image = str(info.imagen).replace("b'", "")
        data_dict['imagen'] = image.replace("'", "")
        data_dict['usuario'] = user.to_dict();
        info_data.append(data_dict)
    return jsonify(info_data)
