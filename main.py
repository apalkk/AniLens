from fastapi import Form, File, UploadFile, Request, FastAPI
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os
import webbrowser

app = FastAPI()
#vidapi = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/search/{name}")
def main(request: Request,name:str):
    output_file = open('sample.json').read()
    output_json = json.loads(output_file)
    for d in output_json:
        if name in d:
            #yield d[name]['link']
            return templates.TemplateResponse("video.html", {"request": request, "id": d[name]['link']})
        #else: return("End")
