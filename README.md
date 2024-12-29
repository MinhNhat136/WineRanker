# Wine Quality Scoring Application

## Project Description
This project involves developing a machine learning model to predict the quality score of wine based on various input metrics, such as acidity, sugar level, residual sugar, chlorides, free sulfur dioxide,... The project is accompanied by a simple and user-friendly Flask web application that allows users to interact with the model. 

## Project Technical
1. Machine Learning - Elastic Met
2. MLFlow
3. Dagshub
4. Github Action 
5. Docker

## Install, Setup and Run
1. Git clone 
2. Open folder with vs code
3. Open terminal 
2. Run conda create -p venv python==3.12 -y
3. Run conda init
4. Run conda activate venv/
5. Run pip install -r requirements.txt
6. Run python app.py
7. Copy link to web browser
8. Add subdirectory '/train' at the end of the link (Example: http:/127.0.0.1:8080/train) and wait about 1 minute for model generate
9. Replace '/train' with '/predict' and experiment

## Project Structure
├── src
│   └── {PROJECT_NAME}
│        ├── __init__.py
│        ├── components
│        |    ├── __init__.py
│        |    └── tests
│        ├── utils
│        │    ├── __init__.py
│        │    └── common.py
│        ├── config
│        │    ├── __init__.py
│        │    └── configuaration.py
│        ├── pipeline
│        │    └── __init__.py
│        ├── entity
│        │    ├── __init__.py
│        │    └── configuaration.py
│        └── constants
│           └── __init__.py
├── config
│    └── config.yaml
├── params.yaml
├── schema.yaml
├── main.py
├── requirements.txt
├── Dockerfile
├── setup.py
├── research
│    └── research.ipynb
└── templates
     └── index.html

## Workflows Pipeline
1. Data Ingestion
2. Data Validation
3. Data Transfomation
4. Model Trainer
5. Model Evaluation

## Dagshub - MLflows
We use Dagshub to manage the project's life cycle.
1. Experiment Tracking
MLflow was used to track all experiments conducted during the development of the ML model. Key aspects such as hyperparameters, performance metrics, and artifacts were recorded automatically. These experiments were stored on Dagshub, providing a centralized location for all experiment results.
2. Model Management
MLflow’s model registry was leveraged to manage multiple versions of the trained models. Each version was assigned a status to streamline deployment and testing. This ensured smooth transitions between model iterations.
3. Data Version Control
Dagshub’s integration with DVC (Data Version Control) enabled precise versioning of the datasets. For our project, the data is imported from a static data source so the data version stays unchanged.
4. Collaboration
Dagshub served as a collaborative hub for the team, combining versioned datasets, tracked experiments, and Git-managed code into one unified platform. This made it easier for team members to review and analyze progress, fostering effective collaboration.

## Github Actions - Testing
GitHub Actions was implemented in this project to streamline the development and deployment process by automating key workflows.
1. Continuous Integration (CI)
We utilized GitHub Actions to automatically run tests every time new code was pushed to the repository. This ensured that any code changes did not break existing functionality. For example, unit tests were executed to verify the correctness of critical components.
2. Continuous Deployment (CD)   
GitHub Actions facilitated the automatic deployment of the application to the production environment. Whenever changes were merged into the main branch, the code was built, containerized using Docker, and deployed to the cloud platform.
3. Code Quality Checks
Workflows were created to run static analysis tools and linters to enforce coding standards. These checks were integrated into the pipeline to maintain high code quality and consistency across the project.

## Workflows Jobs Continous Integration
1. Config.yaml
2. Params.yaml
3. Config entity
4. Configuration Manager
5. Update the components
6. Create Pipeline
7. Front end-- Api's, Training Api's, Batch Prtediction API's

## Docker 
Docker was utilized in this project to containerize the application, ensuring consistent environments across development, testing, and deployment. By packaging the application and its dependencies into lightweight containers, Docker facilitated efficient development and seamless deployment workflows.

