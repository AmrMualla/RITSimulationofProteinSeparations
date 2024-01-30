from fastapi import FastAPI

import API.APIRequests.startup as startup
import API.APIRequests.Electro1D.simulation as electro_1d_simulation

"""
HOW TO START UP API SERVER:

1. In the terminal, redirect to the API server by doing:
      "cd {project_directory}/backend/API"
   
2. Run the command: uvicorn server:app --reload
   This activates the FastAPI system. The terminal window will
   have to stay open for as long as you have the server running
   
3. Open up http://127.0.0.1:8000/ in your browser.
   You should see the message:
   { "message": "Ready to go" }
   This means the API server is up and running!
   
4. To close the API server, either close the terminal window
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

app.include_router(startup.router)
app.include_router(electro_1d_simulation.router)
