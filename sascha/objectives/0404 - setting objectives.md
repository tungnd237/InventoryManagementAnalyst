# 0404 - setting objectives
#학교/23-1/통계적데이터마이닝/project/prelim
grouping products based on the demands
higher demand - group and logistic regression
/
regression on the demands
/
group based on the demands


## questions
- the problem statement on inventory management has specific, inherent, multiple restrictions related to business aspects -> objective is kind of in between data analytics and process optimization(which can turn very mathematical)

## what to keep
- Data = inventory data from manufacturing company
	- inventory levels, demand forecasts, product attr
	- Superstore Dataset (from Tableau)
	
- Method = cluster products based on demand patterns
	- K-means clustering to group products based on demand patterns for each product
	
- Objective = identify optimal inventory levels for clusters
	- 1) Identify groups of products with similar **demand patterns**
		- reduce inventory cost (How so after identification of clusters?)
	- 2) Identify optimal inventory levels for each cluster<-
	
- Performance Goals = better inventory management 
	- 1) reduced inventory carrying costs
	- 2) optimize inventory levels -> efficient use of resources 
	- 3) increased product availability
	- 4) faster order fullfillment
	
## goal for 4/4
- goals in biz aspect
	-  if objective 2) is feasible:
		- 	- 2) Identify optimal inventory levels for each cluster<-
	- 4 performance goals with more specifications
- goals for analyzing dataset
	- ways to cluster in inventory data
		- improving basic kmc
	- which dataset best fit for our biz goal/purposes
		- reasons
	- interpretation of resulting clusters as in most contributing features
		- are the clusters just artefactual result from particular datasets/clustering models?
	
## goal for midterm
- how are our dataset and objectives special? -> practicallity / generalizablility
	- since particular methods work best for particular data types - method-data type interactions
- probably more like a PoC
![](0404%20-%20setting%20objectives/B8A360C4-1C17-4264-A1AA-326AEE2652D8.png)

## for final pt
- more focus on the implications of the statistical results
	- possibly with simulation with past data and our classfication model, validating performance in terms of business aspects as well as statistical significance
- it feels like we’re going to need to raise valid reasons for each step in the series of our decisions.
	- what combination of variables / silmilarity measures / clustering techniques led to the classifications
	- altering variables, choosing different similarity measure, concentrating on a particular subset
	- concerns about evaluation of clustering solutions
		- are the clusters real or arbitrary?
		- what other solutions are possible and which is better?
	- interpretation for how each clusters are grouped in the way they are?
refer: Dubes and Jain, 1979


