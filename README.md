# 2023_statdm_project
statistical data mining project concerning clustering method in inventory management problem

## goal for 4/4 - until next meeting on 4/7 Fri. 14:00 at Burger King
### Goals - in biz aspect
- check feasibility of objectives, mainly 2) (because many directions are possible for obj2)
    - obj2 = Identify optimal inventory levels for each cluster
- identify performance goals 
    - reduce redundancy, increase independency
    - Define 4 performance goals:
        1) reduced inventory carrying costs
        2) optimize inventory levels
        3) increased product availability
        4) faster order fullfillment

### Goals - for dataset analysis
	1) identify which dataset best fit for our biz goal/purposes
    2) compare various clustering methods
	3) improve kmc(or other outstanding clustering method) in terms of performance metrics
	4) interpretation of resulting clusters as in most contributing features
		- are the clusters just artefactual result from particular datasets/clustering models?
	
## 0404 after class meeting: setting objectives
grouping products based on the demands
higher demand - group and logistic regression
/
regression on the demands
/
group based on the demands

## questions (thoughts before 0404)
- the problem statement on inventory management has specific, inherent, multiple restrictions related to business aspects -> objective is kind of in between data analytics and process optimization(which can turn very mathematical)

## what to keep
- Data = inventory data from manufacturing company
	- inventory levels, demand forecasts, product attr
	- Superstore Dataset (from Tableau)
	
- Method = cluster products based on demand patterns
	- K-means clustering to group products based on demand patterns for each product
	
- Objective = identify **optimal inventory levels** for each cluster
	- 1) Identify groups of products with similar **demand patterns**
		- reduce inventory cost (How so after identification of clusters?)
	- 2) Identify optimal inventory levels for each cluster<-
	
- Performance Goals = better inventory management 
	- 1) reduced inventory carrying costs
	- 2) optimize inventory levels -> efficient use of resources 
	- 3) increased product availability
	- 4) faster order fullfillment
	
## goal for midterm(thoughts before 0404)
- how are our dataset and objectives special? 
    - practicallity / generalizablility
	- since particular methods work best for particular data types 
        - reason with method-data type interactions
- probably more like a PoC


