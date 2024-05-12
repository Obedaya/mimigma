from fastapi import APIRouter, Request, WebSocket
from typing import List

router = APIRouter()

# Store all connected WebSocket clients
clients: List[WebSocket] = []

output_data = "Output will appear here."

@router.post("/input")
def read_input(request: Request):
    key = request.query_params.get("key")
    # create_output(key) 
    output_data = key
    return {"input": key}



@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    global output_data
    while True:
        try:
            
            await websocket.send_text(output_data)
            output_data = await websocket.receive_text()
            print("received: ",output_data)
            # Send the new data to the client
            # Your logic to generate or retrieve new data
            
        except WebSocketDisconnect:
            clients.remove(websocket)
            break
