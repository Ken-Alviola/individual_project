# Individual-Project-Semiconductor

### Description 
- Project in creating a classification model to predict if an IC chip will pass or fail after the manufacturing process
- Data is downloaded from UCI http://archive.ics.uci.edu/ml/datasets/SECOM
- The main challenge is to narrow down 591 features for use in predictive modeling

### Goals
- Narrow down features through analysis, feature engineering, and clustering to create a classification model that predicts whether a chip will fail or not

---------------------------------
### Data Dictionary
---
| Column | Definition | Data Type |
| ----- | ----- | ----- |
|0-589| 590 signals/measurements during the manufacturing process| float|
|timestamp| date and time the chip was evaluated| object|

---------------------------------------------------
| Target | Definition | Data Type |
| ----- | ----- | ----- |
|defect| 1 if failed after manufacturing process 0 if not| int|

--------------------------------------------------
### Hypotheses
**1. Is there a significant difference in the average ?**
- null_hypothesis = 
- alternative_hypothesis = 

--------------------------------------------------

### Project Plan
1. Acquire data from UCI page 
2. Prepare data by removing unnecessary/redundant columns, dealing with nulls, and scaling variables for use with ML models
3. Explore data using functions in explore.py as well as jointplot, pairplot, and heatmap.
4. Cluster the data into relevant groups if possible
5. Create ML models based on clusters and choose best performing for test data
6. Present findings and model performance

---------------------------------------------------
### Project Takeaways
- 

--------------------------------------------------
### How to re-create
- All necessary files are in this repository so the best method would be to git clone and read csv
- Run  notebooks
- Adjust exploration and modeling to your liking


