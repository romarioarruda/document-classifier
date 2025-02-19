## Document Classifier

The main goal is to build an A.I model to act as a document classifier.

Firstly I'll conduct this project to identify tax documents such as bills, invoices, etc.


**Machine Learning**

This project is building in Rule-Based Learning: Since you define manual classification rules that are refined over time.


### Approach

1️⃣ Document identification

The idea is find unique patterns in each document. 

Strategies:
- Look for key-words or specific sentences tha only appear in specific documents.
- Validating structures like tax id, dates or specific headers.



**How it'll work ?**
- For each type of documents there are specific regex to identify pattern into given text.
- If a pattern is found, then return the matching type
- Otherwise classifies as 'unknown'


2️⃣ Extraction of relevant data

- After identify the document, we'll extract key informations using regex.