#! /bin/bash
# user:S times,C times:HH times,HH times,HH times:subreddit times,subreddit times:op times,op times

# [catperson:catperson2:catperson3],10-54:20-33,[mostPrevalentSubreddit,secondPrevalentSubreddit]
while read line; do
echo $line |cut -d : -f 1
echo $line |cut -d : -f 3
echo $line |cut -d : -f 4
echo $line |cut -d : -f 5
done <./output/testData
