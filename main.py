import json, uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/getdata")
async def get_data():
    f = open("10blogs.json")
    data = json.load(f)
    json_file = {}
    i = 0
    meta,title,content,date,ids = [],[],[],[],[] 
    for element in data:
        content.append(element["content"])
        meta.append(element["meta"])
        date.append(element["date"])
        title.append(element["title"])
        ids.append(element["id"])
    json_file["ids"] = ids
    json_file["contents"] = content
    json_file["metas"] = meta
    json_file["dates"] = date
    json_file["titles"] = title
    json_file
    return json_file