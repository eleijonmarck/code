#!/bin/bash

# get all the contents
INPUT=`find $1 -type f -exec cat {} \;`
USERS=`ls $1`
#INPUT=`find data/test/ -type f -exec cat {} \;`
#USERS=`ls data/test`
#echo $USERS
#echo """$INPUT"""

# get users s and c
for user in $USERS; do
  NOS=`echo """$INPUT""" | grep $user | grep -w S | wc -l`
  NOC=`echo """$INPUT""" | grep $user | grep -w C | wc -l`

  # get hours
  HOURS=""
  UNIQUE_HOURS=`echo """$INPUT""" | grep $user | cut -f 4 -d - | uniq`
  for hour in $UNIQUE_HOURS; do
    HOURS="$HOURS $hour `echo """$INPUT""" | grep $user | cut -f 4 -d - | grep $hour | wc -l`,"
  done
  
  # get subreddits
  SUBS=""
  UNIQUE_SUBS=`echo """$INPUT""" | grep $user | cut -f 3 -d , | uniq`
  for sub in $UNIQUE_SUBS; do
    SUBS="$SUBS $sub `echo """$INPUT""" | grep $user | cut -f 3 -d , | grep $sub | wc -l`,"
  done

  # get ops
  OPS=""
  UNIQUE_OPS=`echo """$INPUT""" | cut -f 4 -d , | sort | uniq`
  #echo $UNIQUE_OPS
  for op in $UNIQUE_OPS; do
    OPS="$OPS $op `echo """$INPUT""" | grep $user | cut -f 4 -d , | grep $op | wc -l`,"
  done
 
  # print resutls
  echo "$user:$NOS,$NOC:$HOURS:$SUBS:$OPS"
done

