from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title = "FastAPI con Jinja2")

app.mount("/rutaestáticos", StaticFiles(directory="estáticos"), name="estáticos")

Plantilla = Jinja2Templates(directory="plantillas")

@app.get("/inicio/", response_class=HTMLResponse)
async def read_item(request: Request):
    return Plantilla.TemplateResponse("index.html",{"request":request})

@app.get("/integrantes/", response_class=HTMLResponse)
async def leer_integrante(request: Request, Matrícula: int, Nombre: str, APaterno:str, AMaterno:str, Edad: int, Correo:str, Teléfono:int, Carrera:str):
    return Plantilla.TemplateResponse("integrantes.html",{"request":request, "matri": Matrícula,
                                                            "nom":Nombre, "apat":APaterno, "amat":AMaterno, "edad":Edad, "correo":Correo, 
                                                            "teléfono": Teléfono, "carrera":Carrera})
