import asyncio
from fastapi import FastAPI

app = FastAPI()

class foo:
    def __init__(self):
        self.bar = 1

    async def get_bar(self):
        tmp  = self.bar
        self.bar += 1
        await asyncio.sleep(1)
        return tmp

obj =  foo()
car = 0

@app.get("/")
async def read_root():
    # bar = await obj.get_bar()
    global car
    tmp = car
    car += 1
    await asyncio.sleep(1)
    return f"Hello {tmp}"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

def run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run()