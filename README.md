# Customer Churn Prediction for Streaming Service

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Our streaming service has seen a 15% increase in customer churn in the last quarter. This project aims to understand the drivers of this churn and develop a predictive model to identify at-risk customers. By proactively identifying these customers, we can implement targeted retention strategies to reduce churn and increase customer lifetime value.

## Stakeholder & User

The primary stakeholder is the **Head of Customer Retention**. The end-users of the project's output will be the **Customer Success team**, who will use the churn risk dashboard to prioritize their outreach efforts. They will access this information weekly to inform their retention campaigns.

## Useful Answer & Decision

The most useful answer is a **predictive model** that provides a churn risk score for each customer. This will enable the Customer Success team to decide which customers to target with retention offers. The final artifact will be an interactive dashboard that displays the risk score and the top three reasons for that score for each high-risk customer.

## Assumptions & Constraints

* We have access to at least six months of historical customer data, including viewing habits, subscription details, and customer support interactions.
* The data is clean and does not have significant gaps.
* The model needs to be updated monthly to reflect new data.
* We are constrained by a three-month project timeline.

## Known Unknowns / Risks

* The available data may not contain the key drivers of churn.
* The predictive model may not be accurate enough to be actionable.
* The Customer Success team may not have the resources to act on the model's predictions.

## Lifecycle Mapping

| Goal | Stage Deliverable |
| :--- | :--- |
| Identify Churn Drivers | Problem Framing & Scoping (Stage 01) |
| Build Predictive Model | Data Preparation & Modeling (Stage 02) |
| Deploy Dashboard | Deployment & Monitoring (Stage 03) |

## Repo Plan

* **/data/**: Raw and processed data.
* **/src/**: Source code for data processing and modeling.
* **/notebooks/**: Jupyter notebooks for exploratory data analysis.
* **/docs/**: Project documentation, including this README and stakeholder memos.
* Updates will be pushed to the repo at the end of each week.