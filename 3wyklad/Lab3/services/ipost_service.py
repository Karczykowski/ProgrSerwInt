from abc import ABC
from typing import Iterable

from domains.post import Post


class IPostService(ABC):
    async def get_posts_filtered_by_title(self, fragment: str) -> Iterable[Post]:
        pass

    async def get_posts_filtered_by_body(self, fragment: str) -> Iterable[Post]:
        pass

    async def save_to_json(self, posts: Iterable[Post]) -> str:
        pass