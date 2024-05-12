from fastapi import APIRouter, Request, WebSocket
from typing import List
import logging
router = APIRouter()

# Store all connected WebSocket clients
clients: List[WebSocket] = []

output_data = "Output will appear here."

# @router.post("/input")
# def read_input(request: Request):
#     key = request.query_params.get("key")
#     output_data = key
#     return {"input": key}

logger = logging.getLogger("router")
logger.setLevel(logging.DEBUG)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # clients.append(websocket)
    global output_data
    while True:
        try:
            logger.error(str("received: " + output_data))
            await websocket.send_text(str(output_data))
            output_data= await websocket.receive_text()
        except :
            # clients.remove(websocket)
            break
