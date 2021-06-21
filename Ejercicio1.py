from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def mostar_inicio():
    contenido_html = """
    <html>
    <head>
        <title>Equipo1</title>
    </head>
    <body>
        <h3>Bienvenidos</h3>
        <p>Este sitio pertenece al Equipo1 y mostrará los datos de los integrantes</p>
		<a href="claudia.html"> Claudia Arely </a>
        <a href="fabian.html"> Fabian CG </a>
        <a href="daniel.html"> Daniel VV </a>
        <a href="giobanni.html"> giobanni sdc </a>
    </body>
	</html>
    """
    return HTMLResponse(content=contenido_html, status_code=200)
	