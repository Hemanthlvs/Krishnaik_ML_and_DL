# Understanding of Lemmatization

- used in scenarios like Q&A,chatbots,text summarization

## What is Lemmatization?
Lemmatization is a process in Natural Language Processing (NLP) that reduces words to their base or root form, known as a "lemma." This helps in understanding the meaning of words in context.

### Example:
The words "running," "ran," and "runs" are all lemmatized to "run."
The word "better" is lemmatized to "good."

## Difference Between Lemmatization and Stemming
### Lemmatization:
Reduces words to their base form based on their meaning.
Uses a dictionary to find the correct lemma.
### Example: 
"was" → "be"
### Stemming:
Cuts off prefixes or suffixes to reduce words to their root form.
May not always produce a real word.
### Example: 
"running" → "run"

## Advantages of Lemmatization
### Accuracy: 
Provides more accurate results by considering the context and meaning of words.
### Meaningful Output: 
Produces real words, making it easier to understand.
## Disadvantages of Lemmatization
### Complexity: 
Requires more computational resources and time due to the need for a dictionary.
### Dependency on Language: 
May not work well for all languages or dialects.