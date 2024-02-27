# JBioFramework Web Application
> The JBioFramework Web Application is a more efficient and accurate method of performing 1-Dimensional
> and 2-Dimensional Electrophoresis through the use of a browser and file selection in the format of 
> FASTA files.

## Project Sponsor
- [Dr. Paul Craig](mailto:pac8612@rit.edu)
![PaulPhoto.jpg](frontend%2Fjbio-web-app%2Fsrc%2Fcomponents%2Fabout_images%2FPaulPhoto.jpg)
## Download and Installation:
### Git

```bash
git clone https://github.com/AmrMualla/RITSimulationofProteinSimulations.git
cd RITSimulationofProteinSimulations/
pip install -r requirements.txt
```

### Software Requirements
- Python v3.x
- Node.js v21.x
- React v18.2.0

## Usage for Development
Navigate to the top level directory by typing in the command line:
```bash
cd RITSimulationofProteinSimulations/
```

Launch the API server by typing in the command line:
```bash
uvicorn server:app --reload
```

Navigate to the jbio-web-app subdirectory by typing in the command line:
```bash
cd frontend/jbio-web-app/
```

Launch the application by typing in the command line:
```bash
npm start
```

A browser will open with the URL: http://localhost:3000/
![Screenshot 2024-02-26 at 7.40.48 PM.png](..%2F..%2F..%2Fvar%2Ffolders%2Fq_%2Fj5jyjbjj0390ypys98sgrxxm0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_mvcqLL%2FScreenshot%202024-02-26%20at%207.40.48%E2%80%AFPM.png)

Press the **`1D Electrophoresis`** button on the left.

Follow the instructions listed beneath the simulation to load the desired FASTA files.

## Testing Usage

### Frontend Guide:

https://docs.google.com/document/d/1RC6fCA68hfXEZ6a9vKcZgl09WIAgKEhDagDs7LhIvmU/edit?usp=sharing

### Backend Guide:

Navigate to the Electro1DTests subdirectory by typing in the command line:
```bash
cd ~/RITSimulationofProteinSimulations/backend/Electro1DTests
```

Type in the command line to run the tests:
```bash
python3 -m unittest backend.Electro1DTests.ProteinTest
```

OR

Some IDEs have a built-in run function for files that can be executed. If you wish to do this, navigate to the ProteinTest.py or any other test file and click the run button.

Analyze results from the tests being run and modify the test or method being tested if failed.

### API Guide:


## Project Team

- Fall 2023 to Spring 2024:
  - Coach:
    - [Mark Wilson](mailto:mwvse@rit.edu)
  - Developers:
    - [Chase Amador](mailto:cma6320@rit.edu)
    - [Beck Anderson](mailto:bea1935@rit.edu)
    - [Landon Heatly](mailto:lbh1442@rit.edu)
    - [Mack Leonard](mailto:mml2034@rit.edu)
    - [Amr Mualla](mailto:am3576@rit.edu)
  