from fastapi import FastAPI
from ray import serve


app = FastAPI()

@serve.deployment
@serve.ingress(app)
class HelloWorld:
    @app.get("/")
    async def root(self):
        return {"message": "Hello from Ray Serve!"}

import time
if __name__ == "__main__":
    serve.run(HelloWorld.bind())
    while True:
        time.sleep(3600)