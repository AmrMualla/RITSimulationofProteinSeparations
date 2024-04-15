import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import backend.API.APIRequests.startup as startup
import backend.API.APIRequests.Electro1D.simulation as electro_1d_simulation

"""
HOW TO START UP API SERVER:
   
1. Run the command: uvicorn server:app --reload
   This activates the FastAPI system. The terminal window will
   have to stay open for as long as you have the server running
   
   (or if this is for debugging, you can start it up using the start up call at the bottom.
   it is recommended you co the command line start however.)
   
2. Open up http://127.0.0.1:8000/ in your browser.
   You should see the message:
   { "message": "Ready to go" }
   This means the API server is up and running!
   
3. To close the API server, either close the terminal window
   that you started or do the command CTRL^C (Windows or Linux)
   or Command-C (MacOS)
   
VIEWING API DOCUMENTATION:
1. If API is running on a server with a domain name (ex: https://www.projectwebsite.com/api),
   navigate to the url that would be the base for the api calls, followed by /docs.
   (ex: https://www.projectwebsite.com/api/docs)
   
2. If on local system: go to http://127.0.0.1:8000/docs
   
Good luck developing!
-Beck Anderson
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],  # You can also specify just ["GET", "POST"] etc.
    allow_headers=["*"],  # Specify your headers or use ["*"] for all
)

app.include_router(startup.router)
app.include_router(electro_1d_simulation.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
