from dependency_injector.wiring import Provide

import asyncio

from services.ipost_service import IPostService
from container import Container


async def main(
        service: IPostService = Provide[Container.service]
) -> None:

    print(await service.get_posts_filtered_by_title('eum'))
    print(await service.get_posts_filtered_by_body('dolore'))
    print(await service.save_to_json(await service.get_posts_filtered_by_title('eum')))

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())
