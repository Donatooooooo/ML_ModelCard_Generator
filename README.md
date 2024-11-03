# Machine Learning Model Cards Generator
The following repository contains a project designed to automate the cration of Model Cards, a type of documentation for Machine Learning models. With standardized experiment tracking, the software automates documentation creation by adopting CI practices to get Model Cards up-to-date throughout the model lifecycle. Through the use of MLFlow and GitHub Actions, the system can document models automatically, keeping track of crucial information to ensure transparency, reliability and explainability.

# Repository structure
```
|   .gitignore                              <- Files and directories to be ignored by Git version control.
|   README.md                               <- Project description file.
|
├───.github                                 <- Directory containing configurations for Github Actions.
|   └───workflows
├───ModelCards                              <- Directory containing Model Cards generated.
├───ModelCardsGenerator                     <- Directory containing the main software for automated model card creation.
|   ├───setup                               <- Directory containing files to setup the Model Cards generation.
|   |       IntegrateSetup.md               <- File used for setup of generation. 
|   └───src
|       |   generator.py                    <- Contains methods for creation of Model Cards.
|       |   main.py                         <- Script that starts generation.
|       ├───Templates
|       |       env.json                    <- Json file that contains comments used by GitHub Action Bot.
|       |       modelCard_template.md       <- Model Card template.
|       |       _part.md                    <- Integration template.
|       └───Utils
|               exceptions.py               <- Custom exceptions.
|               logger.py                   <- Manages the output of the Model Card creation program.
|               parser.py                   <- Parse IntegrateSetup.md file.
|               utility.py                  <- Contains support functions for Model Card creation.
├───ModelTracker                            <- Directory containing software to train and track ML models.
|   |   main.py                             <- Script that starts classification task.
|   |   MLFlowTracker.py                    <- Manages the tracking of models.
|   ├───Classifiers                         <- Directory containing classifiers.
|   ├───Dataset                             <- Directory containing datasets.
|   └───Utils                               <- Directory containing scripts and support files.
├───mlartifacts                             <- Directory used by MLflow to store artifacts.
└───mlruns                                  <- Directory used by MLflow to store experiments.
```
# How to use

## Setup
No complex procedures are required to run the software. To integrate it into your project, simply copy the subdirectory `ModelCardsGenerator/` and the subdirectory `.github/workflows/` into your main directory. The programme uses MLflow integration to collect the information needed to create Model Cards, so it is essential to use MLflow Tracking and Model Registry to store details about models and their versions.

**Important**: The software is designed to execute automatically via GitHub Actions when a pull request is created. Ensure that your repository is configured correctly to run workflows. To check this, go to _Settings>Actions_ and be sure "Allow all actions and reusable workflows" is check.

Currently, the generation software is based on a local MLflow server. However, with a simple change in the code, it is possible to configure it to connect to a remote server. If you decide to run a server locally, it is necessary to store the information in the main directory of your project.

## Generation step
The generation software is started automatically when a pull request is created if any changes are found in the MLflow storage files. It is not necessary to manually specify which models should be created: the software extracts the latest version of each model in the Model Registry. Should this solution not be optimal, it is possible to influence the behaviour of the programme by assigning the alias @champion to the version of the model whose Model Card is to be created using MLflow UI.

To start MLFlow user interface:
```
mlflow ui --host <server_ip> --port <server_port>
```
After starting the server, open your web browser and navigate to:
```
http://<server_ip>:<server_port>/
```

If you are using a local server:
```
mlflow ui     #in your project directory
```
And then navigate to:
```
http://127.0.0.1:5000/
```

## Integration step
It is possible to integrate the automatically generated Model Card by inserting files in Markdown format in the subdirectory `ModelCardsGenerator/setup/`. To carry out the integration, it is necessary to insert some commands with a very simple syntax into the file IntegrateSetup.md.

To specify which model to integrate:
```
integrate <model_name>
```

After this command, to specify which files should be used:
```
/your_file.md
```

Here an example:
```
integrate KNN
    /introduction.md
    /details.md
    /intended_usage.md
```
This commands can be repeated each time you want to integrate a new Model Card.

If the commands have been written correctly and the files have been added appropriately before the start of generation, integration takes place automatically.

### Forcing integration
If any errors occurred when creating the model card and it was not automatically integrated you can force the integration by specifying the version immediately after the model name.

To specify which model to force integration:
```
integrate <model_name> <version>
   /your_file.md
```

For more information read file `IntegrateSetup.md`.

# Model Card structure
All Model Cards follow a standardised structure and are generated using a predefined template. In the absence of specific model information, the Model Card structure adapts, ensuring that each card includes the core sections, even though some information may not be present.

---
### Model Name - version  
#### General Information  
- Developed by: indicates who developed the model  
- Model Type: specifies the model used  
- Library used for learning: indicates the name and version  
- Python Version: indicates the Python version used  

#### Training Details  
- Dataset: specifies the dataset used  
- Parameters: indicates the parameters used for learning  
   - `List of parameters`  
- Training started at: specifies when the training started  
- Training ended at: specifies when the training ended  

#### Evaluation  
   - `List of metrics`: list of all metrics used to evaluate the model  

#### Any integrations
   - Text retrieved from files in ModelCardsGenerator/setup/
---