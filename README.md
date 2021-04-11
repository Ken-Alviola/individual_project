# Individual-Project-Semiconductor

### Description 
- Project in creating a classification model to predict if an IC chip will pass or fail after the manufacturing process
- Data is downloaded from UCI http://archive.ics.uci.edu/ml/datasets/SECOM
- The main challenge is to narrow down 591 features with no descriptions for use in predictive modeling

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
**1. Is the mean defect rate significantly different for July/August than Sept/Oct?**
- null_hypothesis = "The mean defect rates are the same between July/Aug and Sept/Oct"
- alternative_hypothesis = "The mean defect rates are significantly different between July/Aug and Sept/Oct"

--------------------------------------------------

### Project Plan
1. Acquire data from UCI page 
2. Prepare data by removing unnecessary/redundant columns, dealing with nulls, and scaling variables for use with ML models
3. Explore data using functions in explore.py as well as jointplot, pairplot, and heatmap.
4. Cluster the data into relevant groups if possible
5. Create ML models based on clusters and choose best performing for test data

---------------------------------------------------
### Project Takeaways
- Not enough observations to create a better performing model than baseline
- Data is skewed towards passing chips
- Clustering might have helped
- With so many undescriptive features it will require a lot more time to determine which ones are actually important

--------------------------------------------------
### How to re-create
- All necessary files are in this repository so the best method would be to git clone and run wrangle_semicon()
- Exploration and data cleaning notebooks are available as well and can be experimented with.
- Run Final_semicon notebook. 
- Adjust exploration and modeling to your liking


