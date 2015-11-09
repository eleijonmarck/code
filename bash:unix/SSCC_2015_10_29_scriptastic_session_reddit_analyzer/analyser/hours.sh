#!/bin/bash
#set -x

function counthours() {
	cat $1 |awk -F"," '{print $2}' | awk -F"-" '{print $4}'| sort |uniq -c |sort -nr
}
