# 2023_statdm_project
statistical data mining project concerning clustering method in inventory management problem

[past README archive](./readme_archive.md)

group work history summary:

## [7] 5/26 TUES 1900 Building#4 Room#309

## [6] 5/10-11 TA meeting 
- 5/10 WED - after 2000
- 5/11 THURS - after 1900
- if you need to arrange the questions before the TA meeting come 20-30 mins before

## [5] 5/8 MON 1900 Monet
1) solid analysis objectives - what form of results do we need, what details should we present for the audience to understand better
2) outline for the presentation, according to the theme(=pursuading why the company should try our method)
3) statistical validity, cluster interpretation validity checking procedures

### outline for the final presentation
> rough sketch for the outline of the final presentation
1. **solid objective** <- other than just “inventory objective”
2. business objective to decide the hyperparameters
3. model base
	1. would the performance metrics like silhouette & calinski charts useful for the audiences
4. interpretation of model results(clusters)
	1. how should we visualize the various decision trees used for interpretation of each clusters
5. how we use the clusters to improve AS-IS
	1. what is as-is and what are the pros & cons
	2. domain knowledge <- what stat method are inventory managing companies using these days?
	3. present the comparison between as-is based clustering and our clustering (one way to do a comparison - there could be better distinguishing ways to pursuade the audience)
6. final persuasion conclusions

### talk
# 2023/05/08
1. interpretating clusters with decision tress
### good = it works
- good way to summarize what the clusters mean - how many data points go into each cluster and the conditions in which those data points exhibit

### bad = too much effort - both in text and visually
- information is overly dense in the decision tree plots.
	- there’s a lot for an researcher to hypothesis and analyze about the decision tree in order to make a valid inference onto the business insights
	- since it takes a lot of effort into interpreting clusters with decision trees, we are goint to have to identify the best clustering methods according to the solid objectives (mathematical, business objective, or just aggregate feature wise)
- even when the decision tree provides a valid way to understand the clusters, it’s a bad visualization in a default setting - hard to navigate on the presentation if it’s a high resolution
	- if we’re to take decision tree to explain the clusters in the presentation we are going to have to use less depth of the trees or use a summarization of the representative leaves

2. make the business objective to optimize more solid (main objective of the project = optimization of inventory management)
- compare with demand based clusters vs optimized clusters - we need information on the original time durations between order-ship dates
	- take time series data - ship/order dates into the model
	- maybe just a feature introduction - difference between the ship/order dates
- should include more AS-IS manangement based approach on inventory management (something like control group for a comparison)

3. how we should present the results - presentation wise
- approach as in business objectives
- come up with business wise reasons as to why they should switch to our method


---
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
