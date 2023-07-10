# type: ignore

import uvicorn

from conf import settings
from conf.asgi import get_asgi_application


app = get_asgi_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=settings.DEBUG)
