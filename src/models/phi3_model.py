from vllm import LLM, SamplingParams
from ray import serve

@serve.deployment(ray_actor_options={"num_cpus": 2})
class Phi3Model:
    def __init__(self):
        self.llm = LLM(model="microsoft/phi-3-mini-4k-instruct")
        self.sampling_params = SamplingParams(temperature=0.7, max_tokens=512)

    async def predict(self, prompt: str):
        response = self.llm.generate([prompt], sampling_params = self.sampling_params)
        return response[0].outputs[0].text
    
