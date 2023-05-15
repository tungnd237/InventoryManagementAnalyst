# 0407 1500

## project objective
* Objective = ::identify **optimal inventory levels** for each cluster::
		* Identify groups of products with ::similar **demand patterns**::
> traditional approach to optimal inventory level = demand based = more inventory for more popular products
> our case -> setup different peformance index rather than just on the demand(profits and # of orders) to decide the inventory levels

> first find clusters for the products 
> -> then maybe for customers and add up 
> -> then we might go for time series approach for each of the product clusters

## data 
#### Which data to use: 
1. UCI(row = individual SKU result) 
[kaggle_ref1](https://www.kaggle.com/code/seifmohmed/end-to-end-data-science-project-part-1-analysis) -  build a Regression model to predict Sales or Profit
> UCI if main focus = optimal inventory levels

::2. Superstore(row = individual order)::
- 1) can infer about the optimal inventory levels 2) also has consumer-specific data (not in UCI) 3) data is not yet preprocessed well enough 
> Superstore -> can infer about optimal inventory levels from demand patterns

> actual implications of clustering?
> cluster with high level of profit performance index

#### goal in data analysis method
[image:33F7248E-6AB1-47E8-ACD7-09801115C95F-7296-0002EF9D5B216EF0/3EC42386-C9B1-4A18-8FE7-697297152AE0.png]
- starting with no prior background hypothesis about the data
#### clustering
> certain products with high popularity

> start from finding feature importance

> take out specific columns related to specific objectives
> - making groups of columns to certain objective?

---
### Goals - for dataset analysis
- [x] identify which dataset best fit for our biz goal/purposes  (4/7)

- [ ] 0. preprocessing
	- [x] preprocess the data <- need more checking
	- [x] choose only relevant columns
[image:750A97C3-E40B-426C-AB73-2B78E96D59AD-7296-0002F0B11649997D/62C3A397-9C0F-4784-BB97-F55DE5245F23.png]
	- [ ] choose the right ::encoding methods:: for each types of columns

- [ ] 1. methods
> first find clusters for the products 
> -> then maybe for customers and add up 
> -> then we might go for time series approach for each of the product clusters
	- [ ] explore various methods on our own
		- [ ] drop columns according to certain background knowledge(like according to product-specific columns)
		- [ ] choose the relevant ::similarity index:: for each method
	- [ ] compare various clustering methods
		- [ ] find the right number of clusters
		- [ ] ex) PCA into KMC 
		- [ ] comparison with DBSCAN, SOM, RNN
[image:E7034AF1-35B5-4477-8C31-E24705E3E432-7296-0002F10C0B748F8B/B37DAD2E-CC0A-401B-B125-E4F3306B9C85.png]
2. Validation of models
	- [ ]  improve kmc(or other outstanding clustering method) in terms of performance metrics
		- [ ] ex) Improving KMC Performance: cross validation, elbow
3. Interpretation according to business objective
- [ ] interpretation of resulting clusters as in most contributing features
	- are the clusters just artefactual result from particular datasets/clustering models?
---
role assignments 
- 4/7 roles -> testing out different clustering methods to find the right/well-defined clusters
	- [jupyter notebook] suggest on Github: method-performance index as a pair 
		- give simple reasoning
	- the suggestor try out the method and post the result & performance on Github
	- do this in parallel and could go serial working if you see something more could be done for some methods -> ex) visualization could be more efficient in some methods