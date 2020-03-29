# Wikipedia Link Retrieval

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each Wikipedia article has a number of hyperlinks. Sometimes a user may need to know what are all the other Wikipedia articles that are linked to word he searched so that they can have complete understanding of the topic. Going over each and every hyperlink line by line is a cumbersome task.

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This program gets the input word and displays all the Wikipedia links associated with it that are semantically related. It also retrieves related terms from user's search history based on its similarity degree measure with that of user's input.

## Steps :
  1. Construct a valid URL from user's input
  2. Fetch the page located by the URL
  3. Filtering only wiki links
  4. Finding the synonyms or words related to the input
  5. Display result to the user
  6. Retrieve user's search history and find terms similar to the user input
  7. Update search history

## Prerequisite :
  &nbsp;&nbsp;&nbsp;&nbsp;Make sure you have Python 3
  * Install modules - requests,pickle,nltk
  * To install wordnet :
      1. nltk.download()
      2. Select wordnet from the list and click 'Download' button

## How to run :
```python
  python3 main.py enter_your_term_here
 ```
