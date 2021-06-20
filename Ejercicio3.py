from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_integrantes = [{'item_id': 1, 'Matrícula': 91810166, 'Nombre':'Fabián', 'APaterno':'Cruz', 
                    'AMaterno':'Gómez', 'Edad':21, 'Correo':'Levy.zg14@gmail.com', 'Teléfono': 9191685016, 'Carrera':'RIyC'},

                     {'item_id': 2, 'Matrícula': 91810190, 'Nombre':'Claudia Arely', 'APaterno':'Pérez', 
                     'AMaterno':'Mayo', 'Edad':20, 'Correo':'claudiaarely00@gmail.com', 'Teléfono': 9191563826, 'Carrera':'RIyC'}, 

                     {'item_id': 3, 'Matrícula': 91810225, 'Nombre':'Giobanni de Jesús', 'APaterno':'Sánchez', 
                     'AMaterno':'de la Cruz', 'Edad':21, 'Correo':'llomami@hotmail.com', 'Teléfono': 9191545943, 'Carrera':'RIyC'}, 

                     {'item_id': 4, 'Matrícula': 91810897, 'Nombre':'Juan Daniel', 'APaterno':'Vázquez', 
                     'AMaterno':'Vera', 'Edad':24, 'Correo':'aljim400ro@gmail.com', 'Teléfono': 5619333011, 'Carrera':'RIyC'},

                     {'item_id': 5, 'Matrícula': 91814025, 'Nombre':'Alison', 'APaterno':'Hernández', 
                     'AMaterno':'Gómez', 'Edad':21, 'Correo':'alisonHG@gmail.com', 'Teléfono': 9615792016, 'Carrera':'Contaduría'},

                     {'item_id': 6, 'Matrícula': 91814026, 'Nombre':'Eduardo', 'APaterno':'Gutiérrez', 
                     'AMaterno':'Sánchez', 'Edad':22, 'Correo':'eduardo98@gmail.com', 'Teléfono': 9194620818, 'Carrera':'Contaduría'},

                     {'item_id': 7, 'Matrícula': 91814028, 'Nombre':'Pablo', 'APaterno':'Ramírez', 
                     'AMaterno':'Morales', 'Edad':22, 'Correo':'pabloRM@gmail.com', 'Teléfono': 9192904839, 'Carrera':'Gastronomía'},

                     {'item_id': 8, 'Matrícula': 91814030, 'Nombre':'Jennifer', 'APaterno':'Sánchez', 
                     'AMaterno':'Rodríguez', 'Edad':22, 'Correo':'Jenni98@gmail.com', 'Teléfono': 9197931028, 'Carrera':'Gastronomía'},

                     {'item_id': 9, 'Matrícula': 91814032, 'Nombre':'Rubén', 'APaterno':'Moreno', 
                     'AMaterno':'López', 'Edad':21, 'Correo':'morenoruben@gmail.com', 'Teléfono': 9196285046, 'Carrera':'Procesos Bioalimentarios'},

                     {'item_id': 10, 'Matrícula': 91814034, 'Nombre':'Melissa', 'APaterno':'Roblero', 
                     'AMaterno':'Pérez', 'Edad':22, 'Correo':'meliRP@gmail.com', 'Teléfono': 9197164294, 'Carrera':'Procesos Bioalimentarios'}]

@app.get("/integrantes")
async def leer_integrante(item_id: int):
    for diccionario in lista_integrantes:
        if diccionario.get('item_id') == item_id:
            respuesta = f"""
                <html>
                <head>
                    <title>{diccionario.get('Nombre')}</title>
                </head>
                <body>
                    <h3>SITIO PERSONAL</h3>
                    <ul>
                        <li>Matrícula: {diccionario.get('Matrícula')}</li>
                        <li>Nombre: {diccionario.get('Nombre')}</li>
                        <li>APaterno: {diccionario.get('APaterno')}</li>
                        <li>AMaterno: {diccionario.get('AMaterno')}</li>
                        <li>Edad: {diccionario.get('Edad')}</li>
                        <li>Correo: {diccionario.get('Correo')}</li>
                        <li>Teléfono: {diccionario.get('Teléfono')}</li>
                        <li>Carrera: {diccionario.get('Carrera')}</li>
                    </ul>
                </body>
                </html>
            """
            return HTMLResponse(content=respuesta, status_code=200)
    return "No se encontró el registro"



#async def buscar_integrante(lista_integrantes: Iterable [dict], clave: Hashable, valor: Any) -> Optional[dict]:
#     for diccionario in lista_integrantes:
#        #if diccionario.get(clave) == valor:
#        #  print(diccionario)
#        #return json.dumps(diccionario)
#     #return None

#@app.get("/data")
#async def get_data(start_indx: int = 1, step: int = 8):
#	return lista_integrantes[start_indx : start_indx+step]

async def get_data(indice: int = 0):
	return lista_integrantes[indice]
	
	
	