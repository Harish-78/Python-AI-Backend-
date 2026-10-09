from fastapi import FastAPI
from app.api.routes import rag, agents
app= FastAPI(title="AI Agents & RAG System")


app.include_router(agents.router,prefix="/agents",tags=["agents"])
app.include_router(rag.router,prefix="/rag",tags=["rag"])

@app.get("/health")
def get_health():
    return {"status":"running"}


@app.get("/")
def root():
    return {"message":"AI Agents svc is running!"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)