# ESNE - v4
## Description
Event Severity Network Estimator (ESNE) is designed to address a regression task aimed at predicting a BaseScore value based on network event data. This model utilizes a set of features extracted from a network event dataset to calculate the BaseScore for each new network event.

The prediction is based on a series of quantitative measurements, which are processed by the model to accurately estimate the BaseScore. The features analyzed include parameters such as attack type, malware indicators, anomaly scores, and various network-related information like traffic type, firewall logs, and system information. These data are processed using regression techniques to provide an accurate prediction of the BaseScore for each network event.

More info about BaseScore: https://nvd.nist.gov/vuln-metrics/cvss
## General Information 
- Developed by: donatooooooo
- Model Type: Sequential
- keras version: 3.3.3
- Python version: 3.12.7
## Training Details
- Training started at: 19:01:41 2024-11-20
- Training ended at: 19:18:01 2024-11-20
## How to use
```
trainer = model_name(target value, [drop column], dataset)
trainer.findBestParams()
print(trainer.getParams())
trainer.run()
print(trainer.getMetrics())
```
## Intended usage
1. **Real-time Network Intrusion Detection**: ESNE can be deployed in network security systems to provide real-time estimates of the severity of network events. By analyzing network traffic and identifying potential security incidents, ESNE can help security teams prioritize responses, allocate resources more effectively, and reduce the time to mitigate potential threats. For instance, if the model detects an anomalous traffic pattern indicative of a malware attack, it can calculate a BaseScore to assess the severity of the threat, guiding immediate remediation efforts.

2. **Automated Incident Reporting and Analysis**: ESNE can be used in automated network monitoring tools to generate detailed reports on network events. After processing network data, the model can output a BaseScore that reflects the severity of each event. This can assist in incident analysis, enabling teams to identify high-priority events for further investigation. The system could automatically flag events that exceed a certain severity threshold, streamlining the incident response process and enhancing overall network security operations.
## Evaluation
- `MSE` 0.00029981498039876524
- `MAE` 0.01062148691741136
- `RMSE` 0.017315166196105805
- `MSLE` 0.00014200802544476842
