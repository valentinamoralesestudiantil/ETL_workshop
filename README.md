# ETL_workshop
This repository contains the workshop development by Valentina Morales.
# Desarrollo de caso

A company has a CSV file with 50,000 rows of candidate request data from technical selection processes where each row represents a candidate request. With this, we want to be able to generate analytical queries and key performance indicators so that they are easy to interpret.

The first step that was taken into account is the realization of the requirements where it was understood that the company needed to respond with this from that the respective KPIs that were related to the requirements were made. Through the use of the grain, it was determined which dimensions were needed and what was going to be the level of complexity of each of them, dividing an attribute such as the Application Date into 3 new attributes (Day, month and year), in addition to adding other attributes that were considered important to answer the KPIs. Among other things, each of the attributes was divided by the dimensions we had decided.

## Grain table

| **First Name** | **Last Name** | **Email** | **Application Date = Day, month, year** | **Country** | 
|:--------------:|:-------------:|:---------:|:--------------------------------------:|:-----------:|
| <span style="background-color: F54927">YOE</span> | <span style="background-color: #90EE90">Seniority</span> | <span style="background-color: #FFFF00">Technology</span> | <span style="background-color: #FF6347">Approved by the Code Challenge</span> | <span style="background-color: #FF69B4">Approved by the Technical Interview</span> | 
| <span style="background-color: #FF6347">Approved in both tests</span> | <span style="background-color: #FF6347">Code Challenge Score</span> | <span style="background-color: #FF6347">Technical Interview Score</span> |


## Table related to KPIs

It was decided to create a table of facts called **Application** this will contain 5 attributes of which 3 of them will be created by me because they are not in the original database, this to supply the need to have specific data that in this case will be BOOLEAN to more easily answer the doubts that are presented in the KPIs where it is asked to recognize which are the candidates who were hired in addition to information related to their scores in the tests, following the approval standards of the company, the rest of these attributes will represent the scores obtained in the tests by the candidates.

It also considered the dimension with which it was going to be related, the type of visualization and the justification of its commercial value for each of the KPIs to have a clearer knowledge of what was needed.
