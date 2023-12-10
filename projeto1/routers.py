from fastapi import APIRouter

router = APIRouter()

@router.get("/converter")
def convert():
    return "converter"