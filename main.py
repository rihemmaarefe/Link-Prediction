import json
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# with open("data.json", "r") as d:
#     data = json.load(d)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

prediction_data = [
  { "node1": 0, "node2": 1, "pred": 0},
  { "node1": 0, "node2": 476, "pred":0.352956 },
  { "node1": 0, "node2": 494, "pred":0.769988 },
  { "node1": 1, "node2": 505, "pred":0.463901 },
  { "node1": 9, "node2": 68 , "pred":1.238807},
  { "node1": 15, "node2": 408, "pred":0.204171 },
  { "node1": 18, "node2":549 , "pred":0.204171 },
  { "node1": 60, "node2": 227, "pred":0.204171 },
  { "node1": 199, "node2": 220, "pred":0.245246 },
  { "node1": 170, "node2": 570, "pred":0.509272 },
  { "node1": 148, "node2": 570, "pred":0.204171 },
  { "node1": 151, "node2": 384, "pred":0.204114 },
  { "node1": 232, "node2": 337, "pred":0.285999 },
  { "node1": 446, "node2": 509, "pred":0.291206 },
  { "node1": 510, "node2":576 , "pred":0.495378 },
  { "node1": 571, "node2":589 , "pred":0 },
  { "node1": 585, "node2":596 , "pred":0.245243 },
  { "node1": 446, "node2":509 , "pred":0.291206 },
  { "node1": 375, "node2":383 , "pred":0.46390 },
  { "node1": 461, "node2":462 , "pred":0 }
    ]

# Home page
@app.get("/", response_class=HTMLResponse)
async def Home(request: Request):
    return templates.TemplateResponse("Interface.html", {"request": request})
    
# Prediction
@app.get("/prediction/{node1,node2}", response_class=HTMLResponse)
async def gets(request: Request, node1: int, node2: int):
    matching = list(filter(lambda x: x['node1'] == node1 and x['node2'] == node2, prediction_data))
    mt = matching[0]['pred'] if matching else None
    return templates.TemplateResponse("Interface.html", {"request": request, "mt": mt})

# available data
@app.get("/data/")
async def get_all_predictions(skip: int = 0, limit: int = 10):
    return prediction_data[skip : skip + limit]




# @app.get("/data/{node1,node2}")
# async def getPredOfN1andN2(node1: int, node2: int):
#     matching = list(filter(lambda x: x['node1'] == node1 and x['node2'] == node2, prediction_data))
#     return matching[0]['pred'] if matching else None