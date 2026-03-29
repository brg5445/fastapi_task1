from fastapi import APIRouter, status, HTTPException

from src.schemas import Post


router = APIRouter()


@router.get("/hello_world", status_code=status.HTTP_200_OK)
async def get_hello_world() -> dict:
    response = {"text": "Hello, World!"}

    return response


@router.post("/test_json", status_code=status.HTTP_201_CREATED, response_model=Post)
async def test_json(post: Post) -> dict:
    if len(post.text) < 3:
        raise HTTPException(
            detail="Длина поста должна быть не меньше 3 символов",
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )

    response = {
        "id": 0,
        "author": {
            "login": "string",
            "id": 0,
            "created_at": "2026-02-27T07:00:40.369Z"
        },
        "category": {
            "title": "string",
            "description": "string",
            "is_published": "true"
        },
        "text": "string",
        "datetime_to_publish": "2026-02-27T07:00:40.369Z",
        "created_at": "2026-02-27T07:00:40.369Z"
    }

    return Post.model_validate(obj=response)


@router.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: Post):
    return Post.model_validate({
        "id": post_id,
        "text": post.text,
        "author": {
            "login": "updated_user",
            "id": 1,
            "created_at": "2026-02-27T07:00:40.369Z"
        },
        "category": {
            "title": "updated",
            "description": "updated",
            "is_published": True
        },
        "text": post.text,
        "datetime_to_publish": "2026-02-27T07:00:40.369Z",
        "created_at": "2026-02-27T07:00:40.369Z"
    })


@router.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    return {"message": f"Post {post_id} deleted"}