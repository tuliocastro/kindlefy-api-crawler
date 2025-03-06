from fastapi import FastAPI
from crawl4ai import WebCrawler

app = FastAPI()
crawler = WebCrawler()

@app.get("/crawl")
async def crawl(url: str):
    crawler.warmup()
    result = crawler.run(url)
    return result.markdown

@app.get("/")
async def health_check():
    return {"status": "ok 2"}
