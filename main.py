from fastapi import FastAPI
import crawl4ai

app = FastAPI()

@app.get("/crawl")
async def crawl(url: str):
    result = crawl4ai.crawl(url)
    return result.markdown

@app.get("/")
async def health_check():
    return {"status": "ok 2"}
