# Machine Learning Model Cards Generator
The following repository contains a project designed to automate the cration of Model Cards, a type of documentation for Machine Learning models. With standardized experiment tracking, the software automates documentation creation by adopting CI practices to get Model Cards up-to-date throughout the model lifecycle. Through the use of MLFlow and GitHub Actions, the system can document models automatically, keeping track of crucial information to ensure transparency, reliability and explainability.

# Project Organization
```

    ├── LICENSE
    ├── Makefile                                        <- Makefile with commands like `make data` or `make train`
    ├── README.md                                       <- The top-level README for developers using this project.
    ├── data                                            <- Data used in this project.
    ├── docs                                            <- Main software for automated model card creation.
    |   ├───ModelCards                                  <- Model Cards generated.
    |   ├───setup                                       <- Files to setup the Model Cards generation.
    |   |       config.yml                              <- File used for setup of generation. 
    |   └───src                      
    |       |   generator.py                            <- Methods for creation of Model Cards.
    |       |   main.py                                 <- Script to start generation.
    |       ├───Templates
    |       |       evaluation_template.jinja           <- Evaluation template.
    |       |       generalinformation_template.jinja   <- Information template.
    |       |       modelCard_template.jinja            <- Model Card deault template.
    |       |       title_template.jinja                <- Title template.
    |       |       trainingdetails_template.jinja      <- Training template.
    |       |       _part.jinja                         <- read from file template.
    |       └───Utils
    |               exceptions.py                       <- Custom exceptions.
    |               logger.py                           <- Manages the output of the Model Card creation program.
    |               parser.py                           <- Parse config.yml configuration file.
    |               utility.py                          <- Contains support functions for Model Card creation.
    ├── models                                          <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks                                       <- Jupyter notebooks.
    ├── references                                      <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports                                         <- Generated analysis as HTML, PDF, LaTeX, etc.
    ├── requirements.txt                                <- The requirements file for reproducing the analysis environment.
    ├── setup.py                                        <- makes project pip installable so src can be imported.
    ├── src                                             <- Source code for use in this project.
    │   ├── __init__.py                                 <- Makes src a Python module.
    │   ├── data                                        <- Scripts to download or generate data.
    │   │   └── make_dataset.py
    │   ├── features                                    <- Scripts to turn raw data into features for modeling.
    │   │   └── build_features.py
    │   ├── models                                      <- Scripts to train models and then use trained models to make predictions.
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   └── visualization                               <- Scripts to create exploratory and results oriented visualizations.
    │       └── visualize.py
    └── tox.ini                                         <- tox file with settings for running tox.
```
# User Guide
No complex procedures are required to run the software. The program uses MLflow integration to collect the information needed to create Model Cards, so it is essential to use MLflow Tracking and Model Registry to store details about models and their versions. The software is designed to execute automatically via GitHub Actions. Ensure that your repository is configured correctly to run workflows. To check this, go to _Settings>Actions_ and be sure "Allow all actions and reusable workflows" is check.

The generation software is started automatically when the last commit in a pull request is "modelcards". It is not necessary to manually specify for which models Model Cards should be created: the software extracts the latest version of each model in the Model Registry. If this solution is not optimal, it is possible to influence the behaviour of the program by assigning the alias @champion to the version of the model whose Model Card is to be created using MLflow UI.

## Configuring Model Cards
You can predefine Model Card configurations before starting the program by modifying the config.yml file located in docs/setup/. This file is written in YAML format, which ensures that your IDE can validate the syntax and notify you of potential errors. Follow the steps below to configure the Model Cards:

### Syntax Overview
To define the structure of a Model Card, use the `structure` command followed by the _model name_. You can specify different sections within the Model Card, and associate them with specific Markdown files. Here's the syntax:
```
structure <model name>:
   - <your_section>:
       file: <your_file>.md
   - General Information
   - Training Details
   - <your_section>:
       file: <your_file>.md
   - Evaluation
```
- You can repeat the `structure <model name>` command for each model you want to integrate. Each block will define the sections for that specific model.
- For sections that require detailed content, you have to associate a specific Markdown file using the file attribute and putting file in setup directory. Ensure these files are correctly named and placed in the appropriate directory before running the program.
- While you can define custom sections, it's recommended to include key sections like General Information, Training Details, and Evaluation to maintain consistency across Model Cards. You can override this sections using files.

**Important**: If a configuration is missing or contains errors, the system will generate a default Model Card for that model using information from MLflow.

### Example
```
structure ESNE:
  - Description:
      file: ESNEdescription.md
  - General Information
  - Training Details
  - How to use:
      file: howtouse.md
  - Intended usage:
      file: use.md
  - Evaluation

structure Istological Grading System:
  - Description:
      file: IGSdetails.md
  - General Information
  - How to use:
      file: howtouse.md
  - Training Details
  - Evaluation
  - Limitations:
      file: limitation.md
```

# Model Card structure
If no configuration is provided, a basic model card template is used. In the absence of certain details, the structure of the model card is adjusted to ensure that all essential sections are included, even if some information is missing.

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
---
