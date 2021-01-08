import json
from typing import Optional
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open('test.json', 'r') as testfile:
    data = testfile.read()


@app.get('/', response_class=HTMLResponse)
def read_root():
    return 'Hello World!'


objs = json.loads(data)

@app.get('/todo/getall')
def read_get(request: Request):
    return templates.TemplateResponse('text.html', {'request': request, 'objs': objs})


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get('/todo/create', response_class=HTMLResponse)
def create_test():
    return 'Created!'


@app.get('/todo/update', response_class=HTMLResponse)
def update_test():
    return 'Updated!'


@app.get('/todo/delete', response_class=HTMLResponse)
def delete_test():
    return 'Deleted!'


if __name__ == "__main__":
    uvicorn.run(app=app)
