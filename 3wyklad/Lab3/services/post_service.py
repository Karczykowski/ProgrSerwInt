from typing import Iterable

from repositories.post_repository import IPostRepository
from services.ipost_service import IPostService
from domains.post import Post
import json

class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def get_posts_filtered_by_title(self, fragment: str) -> Iterable[Post]:
        all_posts = await self.repository.get_all_posts_params()
        filtered_posts = []
        for post in all_posts:
            if fragment in post.title:
                filtered_posts.append(post)

        return filtered_posts


    async def get_posts_filtered_by_body(self, fragment: str) -> Iterable[Post]:
        all_posts = await self.repository.get_all_posts_params()
        filtered_posts = []
        for post in all_posts:
            if fragment in post.body:
                filtered_posts.append(post)

        return filtered_posts

    async def save_to_json(self, posts: Iterable[Post]) -> list[dict]:
        return [post.dict() for post in posts]