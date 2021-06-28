# Profiling Hate Speech Spreaders on Twitter
**I got 4th position on [leaderboard](https://pan.webis.de/clef21/pan21-web/author-profiling.html) at PAN in this competetion.**  
## Task  
Hate speech (HS) is commonly defined as any communication that disparages a person or a group on the basis of some characteristic such as race, colour, ethnicity, gender, sexual orientation, nationality, religion, or other characteristics. Given the huge amount of user-generated contents on Twitter, the problem of detecting, and therefore possibly contrasting the HS diffusion, is becoming fundamental, for instance for fighting against misogyny and xenophobia. To this end, in this task, we aim at identifying possible hate speech spreaders on Twitter as a first step towards preventing hate speech from being propagated among online users.

After having addressed several aspects of author profiling in social media from 2013 to 2020 (fake news spreaders, bot detection, age and gender, also together with personality, gender and language variety, and gender from a multimodality perspective), this year we aim at investigating if it is possbile to discriminate authors that have shared some hate speech in the past from those that, to the best of our knowledge, have never done it.

## Dataset  
Data is taken from [PAN website](https://pan.webis.de/clef21/pan21-web/author-profiling.html)
The data uploaded on this github repo is password protected. You need to replace it with your data.   


## Codes
In order to reproduce the result, run all notebooks presents in for a particualar task. Each notebook produce two csv files.
Put all csv files produced by all notebooks of a particular task in a folder such as `submissions` in our case and run the script.py file to average the predictions. 

## Result
### Validation result  
Five fold cross validation result  
English: 75%   
Spanish: 85%   
### Test result 
English: 72%   
Spanish: 82%

### Paper  
TBA 
