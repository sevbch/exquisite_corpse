# Twitter bot
A twitter bot regularly posting exquisite corpses (cf [Wikipedia article](https://fr.wikipedia.org/wiki/Exquisite_Corpse)).

See https://twitter.com/botsevbot for a live example.
## Requirements
In order to work, this bot needs two files:
1. a file named `secrets.py` with the following info:
```
consumer_key = "your twitter consumer_key"
consumer_secret = "your twitter consumer_secret"
access_token = "your twitter access_token"
access_token_secret = "your twitter access_token_secret"
```
2. a file named `exquisite_data.csv` with your data:

| `subject` | `verb` | `adverb` | `object` |
|---------|------|--------|--------|
|...      |...   |...     |...     |
- `subject` includes nominal groups, third person singular. They can be used as subject and object of the sentence
- `verb` includes transitive verbs conjugated in the third person singular
- `adverb` includes adverbs, adverbial phrases, circumstantial supplements (they are put in a sentence 25% of the time)
- `object` includes nominal groups which can only be a direct object complement to the sentence (which means, they are not in the third person singular).

###### Special thanks
This bot was computed thanks to [this tutorial](https://spinecone.gitbooks.io/build-a-bot-workshop/content/).