from data import ReadDatas
from fastapi import FastAPI
import os 

data = ReadDatas()
data.main()

root_path = os.getenv("ROOT_PATH", "")
app = FastAPI(
    title="介護施設取得 API",
    root_path=root_path
)

@app.get("/")
def hello():
    return "Hello! Please access /docs"

@app.get("/list/")
def get_data():
    return data.df.T

@app.get("/query/")
def do_query(q=None):
    return data.query(q).T

@app.get("/version/")
def get_version():
    return {"version": data.get_version()}