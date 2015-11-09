#!/bin/bash
#set -x

DEFINED_BY_DATABASE_ANALYSER_GROUP=/home/ubuntu/analyser/data/test/*

function countreddits() {
	cat $1 |awk -F"," '{print $3}' | sort |uniq -c |sort -nr
}

function counthours() {
	cat $1 |awk -F"," '{print $2}' | awk -F"-" '{print $4}'| sort |uniq -c |sort -nr
}

