# Random Forest - v4
## General Information 
- Developed by: donat
- Model Type: Random Forest
- sklearn version: 1.5.2
- Python version: 3.12.7
## Training Details
- Parameters: 
    - `n_estimators` 50
    - `min_samples_split` 2
    - `max_depth` None
    - `min_samples_leaf` 4
    - `criterion` entropy
    
- Training started at: 17:27:58 2024-11-02
- Training ended at: 17:28:11 2024-11-02
## Evaluation
- `F1_micro score` 0.9649122807017544
- `Recall` 0.9649122807017544
- `F1_macro score` 0.9623015873015872
- `Accuracy` 0.9649122807017544
- `Precision` 0.9649122807017544
## Description
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum. Nulla facilisi. Fusce tincidunt, odio sit amet venenatis tincidunt, justo purus bibendum risus, eu semper urna nisl in libero. Proin euismod risus ac lectus bibendum, id accumsan quam tristique.
## How to use
```
trainAndLog(
    dataset = dataset,
    trainer = trainer,
    experimentName = experiment,
    datasetName = "brest_cancer.csv",
    modelName = "Lorem Ipsum",
    tags = {"dolor sit amet": "consectetur adipiscing elit"}
)
```
