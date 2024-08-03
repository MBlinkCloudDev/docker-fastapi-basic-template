from fastapi import FastAPI
import numpy as np
import logging

logger = logging.getLogger(__name__)
logging.info(12)

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger.info('Started432')
print(1)

app = FastAPI()
glob = []

#@app.get("/")
def read_root():
    print(2)
    return {"Hello": "World..."}


@app.get("/")
async def root():
    print(3)
    logging.info(13)
    loc = []
    r = np.random.rand()
    glob.append(r)
    loc.append(r)
    return {"message": f"Hello World...  --  {r}  --  {glob}  --  {loc}"}

