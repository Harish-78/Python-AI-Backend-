from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def get_agents_ping():
    return {"route":"agents","ping":"success"}