#!/bin/bash

. $(dirname $0)/common.sh


function subreddits(){
    file=$1
    echo "inputfile: $file"
    echo "user: $(basename $file)"
    subreddits=$(cat $file | cut  -d ','  -f 3 | sort |uniq -c |sort -nr | awk -F" " '{print $2}')
    subreddits=$(echo "$subreddits"|     tr '\n' ',')

    subreddits="[${subreddits::-1}]"
    echo "subreddits: $subreddits"
}

for file in $INPUTFILES; do
    subreddits $file
done

