from fastapi import APIRouter

router = APIRouter()

@router.get("/image")
def image():
    return {'image':'Yash.jpg'}