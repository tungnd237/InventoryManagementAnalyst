# Evaluation on the past observation on clusters

## 1. Customer Segmentation(Kmeans, k=3, depth=3)

[plot link](./0502_interpretable_clustering/0502_customer_segment_depth3.pdf)

1. Cluster1

### c1 - past observation

    - Cluster1 is Low recency and low monetary:
    - Insights: These customers have made purchases recently but haven't spent much on their purchases. They might be new or occasional customers who are still evaluating your products or services.

### c1 - new interpretation

- f = total number of orders by the unique customer
- r = last order of the unique customer is more recent if it's close to 0
- m = total revenue generated by the unique customer

- c1 = 368 + 5 = **373** over total of 634 unique customer samples
  - **Majority = 368**: f <= 17, r <= 293, m <= $4432.65
  - 5: 17.5 < f <= 20.5, m <= $1960.58

> why is the second group(5 samples) not filtered with recency?

- the majority of c1 tend to make less orders (maximum totoal order = 17)
- the oldest order in c1 was made 293 days ago, which is rel recent.
- c1 customers tend to pay a wide range of prices, at most $4432.65.
- a minority of c1 customers who has placed 17-20 orders in total tend to buy less(<$1960)
- in all, the majority(368) of c1 can be seen as:
  - 1. wide range of purchasing powers up to medium-high spendings
  - 2. fewer orders than other segmentations
  - 3. more recent activity observable
- while a minority(5) has the following properties:
  - 1. total order between 17 and 20
  - 2. total spending under $1960 (relatively small)

### c1 - evaluation on the past observation

- *low recency*: (**NEGATIVE**)
  - c1 looks more like a high recency group
  - c1 has relatively recent customers with r<=293, considering c2 has r>623 and c1 has r<=623.
  - c1 is more like an *active segmentation* among the 3 clusters.
- *low monetary*: (**NEGATIVE-TENTATIVE**)
  - just because m<$4432 for the majority doesn't mean c1 as a whole is a low spending group.
  - it depends. there are people who spent at most $4432 and some under $1960. Unless we check the proportion of them, can't conclude it's a low monetary group.
  - the majority of c1(368/373) could represent most of the normal customers for this company, as the spending can range from the lowest to medium-high
- *recent purchase but low purchasing power*:(**POSITIVE(recency)-NEG/TENT(purchasing power)**)
  - True, the majority of c1 exhibits relatively recent orders
  - but can't determine if they are all low in purchasing power. 
    - the statement holds for 17<freq<20 & buy<1960 group is in c1, which is a minority(5) of c1.
  - also the majority has m<=$4432, which should be around med-high spending among all samples. c1 could be far from low purchasing power
- *new or occasional, still evaling the company* (**TENTATIVE**)
  - all 3 statements seems rough just with the evidence from the decision tree
  - 1) new? ((**TENTATIVE-NEGATIVE**))
    - If there actually exist new customers, they are most likely to be in c1 among the 3 clusters.
    - but if their last purchase was in 290 days or so, they are **not new customers** in a common sense
  - 2) occasional? (**TENTATIVE**)
    - on occasionality of a purchase, we have to look at the date differences between each orders. just looking at the total number of purchases and the most recent buy date doesn't really tell about how frequently the person visited the service. 
    - it's even possible he binge-bought the products in a series of days and never came back.
  - 3) evaling? (**NEGATIVE**)
    - if a customer is evaluating, one would spend little, or order fewer times.
    - but even if we look at the minority(5) group with m<$1960 spending, which is certainly not a small spending in the first place, 
    - they are ordering 17+ times, which is also far from being a tentative customer.

2. Cluster 2

### c2 - past observation

    - Cluster 2 is high monetary and low recency:
    - Insights: These customers have made purchases recently and contributed significant revenue to the business. They are likely to be your most valuable and loyal customers.
    - Actions:
            - Prioritize customer retention and maintain strong relationships with these customers through personalized communication and tailored offers.
            - Offer loyalty program benefits or exclusive rewards to encourage continued engagement and spending.
            - Gather feedback from these customers to understand their preferences and identify opportunities for improvement in products or services.

### c2 - new interpretation

- c2 = a more specific, smaller group of customers

- c2: 48 + 5 + 2 + 119 = **174** out of 634
  - 119: f>17, mon>$1960, rec<=623
  - 48: f<=17, rec<=293, mon>$4432
  - 5: f>17, rec>293, mon>$4956
  - 2: f>17, mon<=$1960, freq>20

- for customers in c2 with total order less than 17, they tend to have recently visited(rec<293), and paid m>$4432, or less recently visited(r>293) and paid more than $4956
- for customers with total order more than 20 times, they tended to buy less (m<$1960).
- for customers with total order more than 17 times, if they have not visited in a long time (r<623) also tended to buy less (m>$1960).

### c2 - evaluation on the past observation

- *low recency*: (**NEGATIVE-TENTATIVE**)
  - some customers(48/174) are r<293 and the majority(119/174) r<623
  - which is insufficient to conclude as low recency, while a part of the group(48/174) does satisfy as a low recency.
  - if this statement actually holds, we need to see a left-heavy distribution on recency for the majority group of c2(119/174) with r<623
- *high monetary*: (**TENTATIVE**)
  - counterexample:
    - the majority (119/173) of c2 is m>$1960, which is small-med spending
    - there are also people(2/173) who made a lot of orders (f>17) and spent little (m<$1960).
  - evidence for the statement:
    - only (48+5/174) in c2 satisfy for the statement:
    - for someone who didn't buy a lot of times (f<17) one could have bought a lot.(m>$4956 or m>$4432)
  - there are big spenders in c2, but c2 as a whole looks more like two groups into one:
    - old customers who spend little but done more number of orders+ more recent customers spending more with less number of orders
  
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

- c3: 86 + 1 = **87** out of 634
  - 86: f < 17 times, r > 293 days, m < $4956
  - 1: f > 17 times, r > 623 days, m > $1960

### evaluation on the past observation

- *low recency*: (**NEGATIVE**)
  - Unlikely as we have this counterexample: [f > 17 times, r > 623 days, m > $1960]

- *significant monetary*: (**NEGATIVE-TENTATIVE**)
  - Unlikely as it's more probable that we have customers with $1960 < m < $4956. This is a median-spending group for our dataset.

- *inactive or at risk of churning*:(**POSITIVE-TENTATIVE**)
  - True for this particular group: f > 17 times, r > 623 days, m > $1960
  - We do also have relatively low recency group as well in this c3: f < 17 times, r > 293 days, m < $4956