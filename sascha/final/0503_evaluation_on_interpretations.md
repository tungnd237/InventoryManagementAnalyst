# Evaluation on the past observation on clusters

## 1. Customer Segmentation(Kmeans, k=3, depth=3)

[plot link](./0502_interpretable_clustering/0502_customer_segment_depth3.pdf)

1. Cluster1

### c1 - past observation

    - Cluster1 is Low recency and low monetary:
    - Insights: These customers have made purchases recently but haven't spent much on their purchases. They might be new or occasional customers who are still evaluating your products or services.

### c1 - new interpretation

- c1 customers made at most 20 orders in total, and the last order was made at most in the last 293 days.
- c1 customers who orders less (<=17) tend to pay a wide range of prices, at most $4432.65.
- c1 customers who has placed 17-20 orders in total tend to buy less(<$1960)

### c1 - evaluation on the past observation

- *low recency*: (**NEGATIVE**)
  - c1 has relatively recent customers, considering c2 has rec>623 and c1 has rec<=623. c1 is more like a relatively high recency group among the 3 clusters.
- *low monetary*: (**TENTATIVE**)
  - it depends. there are people who spent at most $4432 and some under $1960. Unless we check the proportion of them, can't conclude it's a low monetary group.
- *recent purchase but low purchasing power*:(**TENTATIVE**)
  - true c1 contains relatively recent customers, but can't determine if they are all low in purchasing power. 17<freq<20 & buy<1960 group is in c1, but can't conclude if they actually have property of a recent purchase.
- *new or occasional, still evaling the company* (**TENTATIVE**)
  - it's likely there are people who are new in c1 than any other groups but if their last purchase was in 290 days or so, we can't really say they are of value to track as such new customers.
  - on occasional buy, we have to look at the date differences between each orders. just looking at the total number of purchases and the most recent buy date doesn't really tell about how frequently the person visited the service. it's even possible he binge-bought the products in a series of days and never came back.


2. Cluster 2

### c2 - past observation

    - Cluster 2 is high monetary and low recency:
    - Insights: These customers have made purchases recently and contributed significant revenue to the business. They are likely to be your most valuable and loyal customers.
    - Actions:
            - Prioritize customer retention and maintain strong relationships with these customers through personalized communication and tailored offers.
            - Offer loyalty program benefits or exclusive rewards to encourage continued engagement and spending.
            - Gather feedback from these customers to understand their preferences and identify opportunities for improvement in products or services.

### c2 - new interpretation

- for customers in c2 with total order less than 17, they tend to have recently visited(rec<293), and paid >$4432, or less recently visited(rec>293) and paid more than $4956
- for customers with total order more than 20 times, they tended to buy less (<$1960).
- for customers with total order more than 17 times, if they have not visited in a long time (rec<623) also tended to buy less (>$1960).

### c2 - evaluation on the past observation

- *low recency*: (**TENTATIVE**)
  - some customers are rec<293 and some rec<623, which is insufficient to conclude as low recency, while a part of the group satisfy as a low recency.
- *high monetary*: (**TENTATIVE**)
  - for someone who didn't buy a lot of times (freq<17) and didn't visit for a long time(rec>293) he could have bought a lot.(mon>$4956)
  - But there are also people who made a lot of orders (freq>17) and spent little (mon<$1960). Therefore until we check those intra-groups' proportions it's a tentative analysis.
- *recent purchase & significant revenue sources*:(**POSITIVE-TENTATIVE**)
  - True. for c2 customers who recently visted(rec<293), they generated over $4432 each.
  - However, that isn't always the case as there are also people with rec<623 who paid more than $1960 in total, a relatively small revenue.

- *likely to be VIP&loyal customers* (**POSITIVE-TENTATIVE**)
  - True that c2 has relatively more people with high revenue sources (mon>$4936) than other groups. But we have to be more careful not to determine the whole c2 as a VIP cluster, as there are also people with mon<$1960. But these people spent less but ordered more times than the most others.
  - so depending on how we decide who is the VIP customer for the company, the conclusion will be tentative.

- *Overall Action Plans* (**TENTATIVE**)
  - As not all of the customers in c2 can be concluded as VIP customers, we can't be sure how often the action plan which was aimed for such VIPs will actually be effective.

3. Cluster 3

### past observation

    - Cluster 3 is high recency and high monetary:
    - Insights: These customers have spent a significant amount of money in the past but haven't made any recent purchases. They might be inactive or at risk of churning.
    - Actions:
        - Implement re-engagement strategies, such as sending personalized offers, reminders, or win-back campaigns to bring them back to your business.
        - Identify the reasons for their inactivity, such as dissatisfaction with a product or service, and address these issues.
        - Offer incentives or special deals to encourage them to make a purchase and re-establish their connection with your business.
        - Monitor the success of your re-engagement efforts and adjust your strategies accordingly.

### new interpretation

- f < 17 times, r > 293 days, m < $4956
- f > 17 times, r > 623 days, m > $1960

### evaluation on the past observation

- *low recency*: (**NEGATIVE**)
  - Unlikely as we have this counterexample: [f > 17 times, r > 623 days, m > $1960]

- *significant monetary*: (**NEGATIVE-TENTATIVE**)
  - Unlikely as it's more probable that we have customers with $1960 < m < $4956. This is a median-spending group for our dataset.

- *inactive or at risk of churning*:(**POSITIVE-TENTATIVE**)
  - True for this particular group: f > 17 times, r > 623 days, m > $1960
  - We do also have relatively low recency group as well in this c3: f < 17 times, r > 293 days, m < $4956