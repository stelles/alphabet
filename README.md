# Alphabet Soup

### Problem
Given a list of words sorted in alphabetical order by an unknown alphabet, determine the alphabet for the given words.

### Solution
1. Create a directed acylic graph (DAG) and add every distinct letter from the words as a vertex.
2. Iterate through the sorted words, find the first letter difference between each word.
3. Take that letter and the corresponding suffix letter and add it as an edge with letter -> suffix.
4. Once our graph has been created, traverse the graph with depth first search (DFS) while keeping track of our path (letters).
5. With a DFS traversal, we find the last suffix in the graph first, then each known prefix until we're finished. After reversing our DFS path, we get the alphabetical order for the given words.


## Requirements

Written in `python3` with version (Python 3.8.5)[https://www.python.org/downloads/release/python-385/] however any python version greater than 3.2 should work.

## Usage
The bread and butter functionality comes from [alphabet.py](alphabet.py)

```python3
>>> from alphabet import determine_alphabet
>>> determine_alphabet(["bca","aaa","acb"])
['b','a','c']
```
or 
```python3
from alphabet import Alphabet
>>> Alphabet.determine_alphabet(["bca","aaa","acb"])
['b','a','c']
```

### Tests
To run all the tests - in the root folder run:
```bash
python3 -m unittest
```
Test cases are broken up in two files
1. [test_cases.py](tests/test_cases.py)
`test_cases.py` focuses on random alphabets and their created words
2. [test_alphabet.py](tests/test_alphabet.py)
`test_alphabet.py` focuses on creating tests around the assumption that the given alphabet is ['a','b','c']. I found it easier to test against a known alphabetical order.

## Thoughts
I had quite a bit of fun on this problem as it dives back into graph theory which I really enjoy but rarely use. I ended up going through a few iterations of my solutions ss I expanded my test cases which would fail my previous solution.
### Challenges
- I assumed given the words ["a", "ab"], I could assert that 'a' came before 'b' however that's not true. The above words give zero information about an alphabet.
- I created a directed graph for each letter and all their predecessors however that created a directed graph that couldn't differenciate priority between letters.
- I hate to admit it but it took a few iterations to realize how to find the difference between important suffixes and throw aways.
- I even looked up [alphabetical order](https://en.wikipedia.org/wiki/Alphabetical_order) on wikipedia to find this tidbit:`If a position is reached where one string has no more letters to compare while the other does, then the first (shorter) string is deemed to come first in alphabetical order.`



