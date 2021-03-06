Predict the fuel consumption of ships for optimizing operational efficiency.
============================================================================

Objective:
----------
The objective of this project is to create a performance model of a large commercial gas container ship, to predict the rate of fuel consumption on a set of features.

Data:
-----
The data used in this experiment are collected from the ship's sensors and from NOAA (National Oceanic and Atmospheric Administration) realted to weather and sea state. 

Structure: 
----------
The project's folder structure follows [cookie-cutter](https://github.com/drivendata/cookiecutter-data-science) style. The root folder contains the following subfolders and files.

- data: This folder contains raw, interim and processed datasets used in this project, in csv format.


- models: Contains trained candidate model saved as a pickle file.


- notebooks: This folder contains 4 jupyter notebooks featuring data preparation, exploratory analysis, feature generation and model building.


- reports: Jupyter notebook as a final report with a detailed end to end analysis.


- src: Contains scripts to train the Extra Trees ensemble model for scoring on new data.


- requirement: A text file with libraries used in this project and their versions.


Conclusions:
------------
- **Extra Trees Regression model, with tuned hyper-parameters outperformed the other predictive models which were tested during this experiment. Performance of the model on unseen data as indicated by Root Mean Square Error is 0.909**


- **Top contributing factors for fuel consumption rate are shaft speed, speed of ship in water, mean draft and type of fuel.**


- **The root mean squared error evaluation scores observed during model training using cross-validation is superior to similar scores obtained from other models.**


- **The model can be scored on a range of perdictor values to estimate the fuel consumption rate for this ship. However, the generalization of this model to predict fuel consumption rate for other ships will require further analysis.**


