# DS_project end to end (Wine_Quality_Prediction)

## Dataset Link:-`http://github.com/krishnaik06/datasets/raw/refs/heads/main/winequality-data.zip`

## Workflows - ML-Pipeline
1. Data Ingestion
2. Data Validation
3. Data Transformation -- Feature Engineering , Data Preprocessing
4. Model Training
5. Model Evaluation -- Mlflow , Dagshub

## Workflows
1. Update config.yaml 
2. Update schema.yaml (for validation)
3. Update params.yaml (for model parameters)
4. Update entity (to make the dataclass for each step)
5. Update the configuration manager in src config (to add the function of each step)
6. Update the components (to make the class for each step)
7. Update the pipeline (to call it in main.py)
8. Update main.py


## You can run it after cloning it into you device

### Steps:

1. Open your terminal 
2. git clone `https://github.com/smitngandhi/DS_project`
3. cd DS_project
4. python -m venv ds_venv (to create virtual environment)
5. ds_venv\Scripts\activate (to activate virtual environment)
6. python app.py (to run the flask app)
7. localhost:5000/train (to train)
8. localhost:5000/predict (to predict)