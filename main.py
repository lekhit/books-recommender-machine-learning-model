from helper import rem,df,top,send_index
rem()
print('started')

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/book")
async def book1(book_isbn:str):
		index=0
		for i in df['isbn']:
			if i==book_isbn:
				break
			index+=1
		rs=rem(index)
		return {'result':rs}
	
@app.get("/")
async def root(page:int =0):
	rs=top(page*20,page*20+20)
	return rs
@app.get("/index")
async def give_recommendation(index:int=0):
	rs=send_index(index)
	return rs

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

