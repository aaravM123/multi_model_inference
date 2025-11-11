from fastapi import FastAPI
from pydantic import BaseModel
from ray import serve
from models.phi3_model import Phi3Model

app = FastAPI()

class InferRequest(BaseModel):
    prompt: str

@serve.deployment
@serve.ingress(app)
class Phi3Service:
    def __init__(self):
        self.model = Phi3Model.bind()

    @app.post("/infer")
    async def infer(self, req: InferRequest):
        handle = serve.get_deployment_handle("Phi3Model")
        result = await handle.remote(req.prompt)
        return {"response": result}
    

if __name__ == "__main__":
    serve.run(Phi3Service.bind())