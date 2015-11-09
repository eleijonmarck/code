#!/bin/sh

FILENAME="/tmp/aggregator_data_do_not_mess_with_this"
SUBREDDITS="/tmp/subreddits"
OPS="/tmp/ops"
CREATED="/tmp/created"

fetch_content()
{
   USERNAME=$1
   TYPE=$2
   URL="https://www.reddit.com/user/$USERNAME/$2.json"

   # TODO check if USERNAME exist. Make func please
   if [ "$2" = "submitted" ]; then
      char='S'
      author_field='author'
   else
      char='C'
      author_field='link_author'
   fi

   curl $URL > $FILENAME 2> /dev/null

   sed -i 's/,/\n/g' $FILENAME 
   cat $FILENAME | awk '/"subreddit":/ { print $2 }' >> $SUBREDDITS
   cat $FILENAME | awk '/"'${author_field}'":/ { print $2 }' >> $OPS
   cat $FILENAME | awk '/"created":/ { print $2 }' | xargs -n1 -i{} date -d@"{}" +"${char},%Y-%m-%d-%H-%M-%S" >> $CREATED
}

get_submitted()
{
   fetch_content $1 "submitted"
}

get_commented()
{
   fetch_content $1 "comments"
}

rm -f $FILENAME $SUBREDDITS $OPS $CREATED

while true; do 
   for user_id in `ls -1rt data/`; do
     echo "New requests!"
     user=$(cat data/$user_id)
   
     mv data/$user_id data/${user_id}.processing
   
     # submitted content
     get_submitted $user
     
     # commented content
     get_commented $user
     
     # db preparations
     mv data/${user_id}.processing data/${user_id}.db
     paste -d ',' /tmp/created /tmp/subreddits /tmp/ops > /tmp/almost_there
     sed -i 's/"//g' /tmp/almost_there
     
     mkdir -p ~/analyser/data
     cp /tmp/almost_there ~/analyser/data/$user
     cat ~/analyser/data/$user
   
     # clear
     rm data/${user_id}.db
   
   done
   sleep 1;
done
  
## Alternative 
# awk '/subreddit":/ { print $2 } /author":/ { print $2 }' /tmp/aggregator_data_do_not_mess_with_this

