# Superstore Sales and Inventory Analysis

## Introduction
This repository contains an analysis of sales and inventory data from a fictional superstore using Python's Pandas, Numpy, Scikit-Learn, Seaborn, and Matplotlib libraries. The main goal of this analysis is to discover patterns and insights that could be useful for inventory management.

The notebook covers the following areas:
1. Loading and exploring the dataset.
2. Demand-based product analysis.
3. Data normalization and clustering using K-means and DBSCAN.
4. Mean sales and quantity calculation for each cluster.
5. Suggestions for inventory management based on the clustering results.
6. Feature selection and one-hot encoding.
7. Further clustering and exploration of clusters.
8. Exploration of additional features and trends.
9. Customer segmentation and action suggestions.
10. Product segmentation.

## Installation

Clone the repository and install the necessary dependencies:

...
git clone [<repository_url>](https://github.com/tungnd237/InventoryManagementAnalyst)
pip install pandas numpy scikit-learn seaborn matplotlib
...

## Dataset

The dataset used is a CSV file named 'superstore.csv'. It contains information on various sales transactions like sales amount, quantity, profit, discount, etc., for different products. The dataset should be placed in the 'data' directory.

## Usage

To run the analysis, open the notebook file in a Jupyter environment and execute the cells.

## Notebook Organization

The notebook is organized as follows:
* **Data Loading and Exploration**: Load the data and inspect its content and structure.
* **Data Cleaning and Preprocessing**: Clean the data by removing unnecessary columns and normalizing numeric features.
* **Clustering**: Perform K-means and DBSCAN clustering to group products based on sales and quantity.
* **Inventory Management Suggestions**: Provide inventory management suggestions based on the mean sales and quantity of each cluster.
* **Further Clustering and Exploration**: Carry out further clustering using additional features and investigate the properties of each cluster.
* **Customer Segmentation**: Calculate RFM (Recency, Frequency, Monetary) values and cluster customers based on these features.
* **Product Segmentation**: Group products based on product ID and calculate the sum of sales and quantity.

## Contributing

We welcome contributions to improve this analysis. Please feel free to fork the repository, make changes, and create pull requests.


