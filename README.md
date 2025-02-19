## Document Classifier

The main goal is to build an A.I model to act as a document classifier.

Firstly I'll conduct this project to identify tax documents such as bills, invoices, etc.


**Machine Learning**

Aprendizado Baseado em Regras (Rule-Based Learning): Já que você define regras de classificação manuais que vão sendo aprimoradas.

Aprendizado Semi-Supervisionado (caso o sistema use tanto regras manuais quanto exemplos classificados pelos usuários para melhorar a classificação futura).

Aprendizado Baseado em Casos (Case-Based Reasoning - CBR): O sistema armazena decisões passadas e usa elas para classificar novos casos semelhantes.


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