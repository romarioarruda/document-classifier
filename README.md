## 🚧 Building...

## Document Classifier

The main goal is to build a document classifier that could be trained with new scenarios according to needs.

Once a new document needs to be classify, a human will input it into the system, classify it and specify the rules to extract data from document and indicates which are each fields to json output.

Now when a new document with the same stardard is inputed on system, the A.I will perform a database search looking for some similar document inputed previously.


## A.I Concepts

This is a Rule-Based A.I: Since you define manual classification rules that are refined over time.

The main idea is increase the system knowledgment according to user manual classification.


### Approach

1️⃣ Document Classification

The idea is perform a search for previously classification using a similarity algorithm.

Strategies for automatic classification:
- Get documents category already classified in the database.
- Perform a similarity calculation using Jaccard similarity index.
- Retrieve a most matching classification around 90% of similarity



2️⃣ Extraction of relevant data

To extract desired data will be necessary indicates the patterns to match with the informations we need.

- Regular expressions will used for recognize the data patterns
- Alongside with each expression must be related to a field that will be used as json output.

**For example:**

To extract a specific date that have a specific pattern in the document like this:

```
Issue Date: 2025-02-15
```

We will write an expression like this: `Issue\s*Date:\s*(\d{4}-\d{2}-\d{2})`

And specify which field this expression will represents: `issueDate`

Then the final result will be something like this:

```
{
    "issueDate": "2025-02-15"
}
```