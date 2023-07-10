from fastapi import APIRouter

from text_analyzer_service.posts.infrastructure.api.views import post_router


router = APIRouter()
router.include_router(post_router, prefix="/posts", tags=["posts"])
