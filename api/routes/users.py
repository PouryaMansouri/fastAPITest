from fastapi import APIRouter

router = APIRouter(
    tags=["users"],
    prefix="/users",
)


@router.get("/")
async def get():
    return {"message": "Hello users"}