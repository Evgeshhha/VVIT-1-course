from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import wikipedia

# Создаем объект FastAPI
app = FastAPI()

# Схема для запроса с параметром в теле
class WikiRequest(BaseModel):
    query: str

# Роут с параметром path (путь)
@app.get("/wiki/{path}")
def read_wiki_path(path: str):
    try:
        # Получаем текст страницы Wikipedia по названию
        content = wikipedia.page(path).content
        return {"title": path, "content": content}
    except wikipedia.exceptions.DisambiguationError as e:
        raise HTTPException(status_code=400, detail=f"DisambiguationError: {e}")
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail=f"Page {path} not found")

# Роут с параметром query (параметры запроса)
@app.get("/wiki/search")
def search_wiki(query: str):
    try:
        # Выполняем поиск по запросу
        search_results = wikipedia.search(query)
        return {"query": query, "results": search_results}
    except wikipedia.exceptions.HTTPTimeoutError:
        raise HTTPException(status_code=504, detail="Timeout error")

# Роут с параметрами в теле запроса (body)
@app.post("/wiki/content")
def get_wiki_content(wiki_request: WikiRequest):
    try:
        # Получаем информацию о странице по запросу
        content = wikipedia.page(wiki_request.query).content
        return {"query": wiki_request.query, "content": content}
    except wikipedia.exceptions.DisambiguationError as e:
        raise HTTPException(status_code=400, detail=f"DisambiguationError: {e}")
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail=f"Page {wiki_request.query} not found")
