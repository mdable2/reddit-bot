from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from logging.config import dictConfig
from log_config import log_config
from simpletransformers.conv_ai import ConvAIModel
from typing import List

personality = [
    "i like stocks",
    "i am from wallstreetbets",
    "i like reddit",
    "i love holding the stock"
]

model = ConvAIModel("gpt", "outputs", use_cuda=False)

dictConfig(log_config)
logger = logging.getLogger("reddit-broker-bot")

app = FastAPI()


class ChatPayload(BaseModel):
    message: str
    history: List[str]


@app.get("/health")
def health():
    logger.info("Health request received.")
    return "Service is online."


@app.post("/chatbot")
def chatbot(request: ChatPayload):
    try:
        logger.info("Chatbot request received.")
        response, history = model.interact_single(
            message=request.message, history=request.history, personality=personality)
        return response
    except Exception as e:
        logger.error("Server error: ", e)
        raise HTTPException(
            status_code=500, detail="Server error, try again soon!")
