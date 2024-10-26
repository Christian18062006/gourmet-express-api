from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
app=FastAPI()
foods_db = [
    {"name": "Spaghetti Bolognese", "author": "Carlos Christian", "recipe": "Cozinhe o espaguete com molho bolonhesa", "preparation_time": 30},
    {"name": "Feijoada", "author": "Ana Maria", "recipe": "Feijão preto com carne de porco e linguiça", "preparation_time": 120},
    {"name": "Sushi", "author": "Kenji Yamamoto", "recipe": "Enrole o arroz e peixe fresco em algas", "preparation_time": 45},
    {"name": "Tacos", "author": "José Hernandez", "recipe": "Prepare a carne e recheie as tortillas", "preparation_time": 20},
    {"name": "Paella", "author": "Luis García", "recipe": "Misture frutos do mar, arroz e açafrão", "preparation_time": 60},
    {"name": "Biryani", "author": "Amit Sharma", "recipe": "Cozinhe arroz com especiarias e carne", "preparation_time": 90},
    {"name": "Ratatouille", "author": "Marie Dupont", "recipe": "Refogue vegetais com azeite e ervas", "preparation_time": 40},
    {"name": "Hamburguer", "author": "John Smith", "recipe": "Grelhe a carne e monte o sanduíche", "preparation_time": 15},
    {"name": "Pizza Margherita", "author": "Giulia Rossi", "recipe": "Asse a pizza com molho, queijo e manjericão", "preparation_time": 25},
    {"name": "Pad Thai", "author": "Arun Chaiyaphat", "recipe": "Frite o macarrão de arroz com camarão e molho tailandês", "preparation_time": 30},
    {"name": "Falafel", "author": "Khalid Mahmood", "recipe": "Frite bolinhos de grão-de-bico com especiarias", "preparation_time": 20},
    {"name": "Brigadeiro", "author": "Maria Silva", "recipe": "Cozinhe leite condensado e chocolate até engrossar", "preparation_time": 15},
    {"name": "Ceviche", "author": "Pablo Torres", "recipe": "Marinhe peixe fresco em suco de limão e ervas", "preparation_time": 15},
    {"name": "Goulash", "author": "Eva Nagy", "recipe": "Cozinhe carne com páprica e vegetais", "preparation_time": 180},
    {"name": "Churrasco", "author": "Carlos Mendes", "recipe": "Grelhe cortes de carne na churrasqueira", "preparation_time": 90},
    {"name": "Croissant", "author": "Pierre Leclerc", "recipe": "Asse a massa folhada em formato de meia-lua", "preparation_time": 180},
    {"name": "Pho", "author": "Thanh Nguyen", "recipe": "Prepare caldo de carne com macarrão de arroz", "preparation_time": 120},
    {"name": "Moussaka", "author": "Eleni Papadopoulos", "recipe": "Monte camadas de berinjela, carne e molho bechamel", "preparation_time": 90},
    {"name": "Empanadas", "author": "Sofia Fernández", "recipe": "Recheie a massa com carne e asse ou frite", "preparation_time": 40},
    {"name": "Poutine", "author": "Luc Tremblay", "recipe": "Cubra batatas fritas com queijo e molho", "preparation_time": 20}
]
@app.get("/")
async def root():
    return {"":"Hello welcome to gourmet express."}
@app.get("/foods",response_model=List[Food])
async def list_foods():
    return foods_db
class Food(BaseModel):
    name:str
    author:str
    recipe:str
    preparation_time:int