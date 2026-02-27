# ETL_workshop
This repository contains the workshop development by Valentina Morales.
# Desarrollo de caso

A company has a CSV file with 50,000 rows of candidate request data from technical selection processes where each row represents a candidate request. With this, we want to be able to generate analytical queries and key performance indicators so that they are easy to interpret.

The first step that was taken into account is the realization of the requirements where it was understood that the company needed to respond with this from that the respective KPIs that were related to the requirements were made. Through the use of the grain, it was determined which dimensions were needed and what was going to be the level of complexity of each of them, dividing an attribute such as the Application Date into 3 new attributes (Day, month and year), in addition to adding other attributes that were considered important to answer the KPIs. Among other things, each of the attributes was divided by the dimensions we had decided.

## Grain table

| **category**            | **attribute**  | **attribute** | **attribute** | **attribute** |
|-------------------------|----------------|---------------|----------|---------|
| **Candidate dimension** | **First Name** | **Last Name** | **Email**|  **YOE**|
| **Seniority dimension** | **Seniority**  |               |          |         |
| **Country dimension**   | **Country**    |               |          |         |
| **Date dimension**      | **Application Date = Day, month, year** | |          |         |
| **Fact Table**          | **Approved by the Code Challenge** | **Approved by the Technical Interview** | **Approved in both tests** | **Code Challenge Score** | **Technical Interview Score** |


## Table related to KPIs

It was decided to create a table of facts called **Application** this will contain 5 attributes of which 3 of them will be created by me because they are not in the original database, this to supply the need to have specific data that in this case will be BOOLEAN to more easily answer the doubts that are presented in the KPIs where it is asked to recognize which are the candidates who were hired in addition to information related to their scores in the tests, following the approval standards of the company, the rest of these attributes will represent the scores obtained in the tests by the candidates.

It also considered the dimension with which it was going to be related, the type of visualization and the justification of its commercial value for each of the KPIs to have a clearer knowledge of what was needed.

| Requirements | KPIs | Dimensions | Visualization Type | Commercial Value Justification |
|--------------|------|------------|--------------------|--------------------------------|
| How many hirings are there for each of the technologies? | Hires by Technology | Technology | Bar chart | Allows the company to see which technologies are most demanded by the company and which ones have the highest hiring index. |
| How many hires are there for each year? | Hires by Year | Date | Line graph | Allows the company to see in which years more hiring was made and in which not to evaluate how growth is going in addition to planning a budget. |
| How many hires are there according to the Seniority level? | Hires by Seniority | Seniority | Bar graph | Allows the company to see which seniority of technologies is the most hired and which not in order to control salaries and measure if more is being invested in experienced talent or internal training in the company. |
| How many hires are there for each country? | Hires by Country over Years (Focus on USA, Brazil, Colombia, Ecuador) | Country | Multiple line graph | Allows the company to see which are the countries from which most staff was hired, this allows to analyze international expansion and where the market should be prioritized. |
| What is the average score obtained by the candidates in the Code Challenge? | Average score of the Code Challenge | Candidate | KPI Card | Allows the company to see what are the average scores obtained by the candidates who apply, this serves to evaluate how the performance in the tests is being and whether the results obtained are higher or lower than expected, thus identifying skills gaps and the effectiveness of the selection process. |
| What is the percentage of hiring in the registered years? | Hiring percentage | Candidate | Pie chart | Allows the company to see how many of the registered candidates have been hired for passing the tests. This is representative because they estimate how the quality of the applicants is being to pass the proposed requirements and helps to optimize selection costs. |
| What is the average year of experience of the people who were hired? | Average years of experience | Candidate | KPI Card | Allows the company to estimate the years of experience of the people who are hiring in order to evaluate the general level of experience of the contracted people, help balance the work teams and help in salary decisions. |

This process resulted in the division into 5 dimensions because each of them is an essential source to answer the KPIs so the information can be obtained more easily in a more optimized way looking for the search and use to be as efficient as possible, resulting in a star-type dimensional data model that can be seen.

![Dimensional Data Model](./Lab4/sql/dimensional_data_model.png)

##libraries required for its use

1. 
2. 
3. 
4.
5.
6.
7.
8.
9.
10.
