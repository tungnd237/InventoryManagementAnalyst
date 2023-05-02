# 2023_statdm_project
statistical data mining project concerning clustering method in inventory management problem

[past README archive](./readme_archive.md)

group work history summary:

## [5] 5/8 MON 1900 Monet
1) solid analysis objectives - what form of results do we need, what details should we present for the audience to understand better
2) outline for the presentation, according to the theme(=pursuading why the company should try our method)
3) statistical validity, cluster interpretation validity checking procedures

## [4] 5/2 TUE 0930 = mid presentation
### Questions
- q1) how did we plan to handle time/seasonality effect (Ship/Order Date)
- q2) explanation on each cluster difficult to understand - example of product for each cluster?
- q3) still need to identify main characteristic for each cluster
	- how does the new suggested analysis incorporate into industry-common approach in dealing with product management? 
- q4) how does it predict the demand, variance to accomodate for each product?
- q5) more direct implications to inventory level improvement needed

### Feedbacks
- it's important to get ino the details about the clusteiring results
- check whether the results are consistent with our common sense to guarantee if we’re actually in the right direction
- look at the details about the result

### (Compare with other teams' feedback)
1. g1
- what can we do with the results?
- any interesting insights?
- clear proejct objective needed
2. g2
- try analyze with elementary methods FIRST
- which factors affect the exchange rate (target variable)
- have to look at histogram and elemenatry methods
- before considering complex models, have to look at the details of the data

### Overall Feedback
- not gentle/kind to the audience
- introduce terms and domain topics better
- problem, what you want to do -> dataset -> basic analysis  /eda -> basic modeling
- result should be consistent to the common sense - for the validity of the pursuation
- don’t need to explain the technical stuff
- consider more what content to introduce in the presentation in 10 mins
- prep more into delivery of the results than the analysis itself

- need to use easier word - for the delivery
- make presentation look as easy as possible

### Notice for final presentation
- final = live presentation
- assume audience have no prev knowledge
- write a report before the finals
- grading = report + presentation 


## [3] 4/17 MON 1900
1. quick progress 
	1. **i did ~**
2. objective 
	1. **in ppt, expecting ~** 
	2. **in ppt, there should at least be ~ items** 
	3. **how can our ppt be different from usual subjects?**
3. problem 
	1. **not sure about ~**
	2. **more of ~ because ~** 
4. role/goal setting
	1. storyboard & ppt
	2. explain the journey OR step the steps (depends on given time limit)
5. questions to TA: when to arrange a meeting? what questions should we ask?
---
#### New goals
- include interpretations for each clustering method 
- different approaches for the same method
	- setup likely groups of variables, and test each method with the selected groups of variables
		- based on the basic performance metrics (ex: silhouette) and visual representation of clusters

#### Questions
- about presentation
	- what are the required items to have in the ppt?
	- time limit of presentation (to decide the # of slides)
- about project
	- about the dataset & preprocessing (gp)
		- bias of the datasets (gp)
	- about evaluation with different performance metric  & clustering methods
		- objective: well separating product clusters? finding the right combination of features that lets better cluster separation?

- start with objective of the project
- feature selection methods - prior knowledge, autoselection packages(boruata)
- outlier handling (boundaries)

---
## 4/14 FRI 1500 (POSTPONED)
---
## [2] 4/7 FRI 1500
### 1. Data source = [Superstore](https://www.kaggle.com/code/seifmohmed/end-to-end-data-science-project-part-1-analysis)
	reasoning:
	1) optimal inventory levels inferrable
	2) consumer-specific data (not in UCI) 
	3) data is almost in raw form

### 2. Preprocessing
- check for anomalities in dataset

### 3. Clustering

	actual implications of clustering?
> can we identify cluster with high level of profit performance?

	assumption: certain products are of high popularity
- -> drop unrelated variables and start with important variables

### 4. Validation and Interpretation of Results
	1. improve performance of classification
	2. find meaningful interpretation/approach for each cluster
---
## [1] 4/4 TUE after class
### 1. basic approach = grouping products based on the demands

### 2. Objective
	1. Identify groups of products with similar demand patterns
	2. Identify optimal inventory levels for each cluster
### 3. Performance metrics
	1. inventory carrying costs 
	2. product availability
	3. order fullfillment speed
