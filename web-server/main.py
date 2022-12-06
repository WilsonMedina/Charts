import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def get_list():
    return"""
        <h1>Hola soy una pagina de prueba</h1>
        <a href='/contact'>Ir a contacto</a>
        <p>soy un parrafo</p>
            """ 

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy la pagina de contacto</h1>
        <a href="https://www.youtube.com/@MatematicasprofeAlex">Por aca puedes aprendes un poco de matematicas</a>
            """
    

def run():
    store.get_categories()

if __name__ == '__main__':
    run()