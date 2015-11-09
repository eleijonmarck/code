#!/bin/bash

main() 
{
    AggregatorPath="/home/ubuntu/agregator/data"
    File=$(find_highest_file_number ${AggregatorPath})

    while true
    do 
	echo "Input user:"
	read User
	echo "${User}" > ${AggregatorPath}/${File}
	File=$((1+File))
	$(check_processing) 
	
    done
}
	
find_highest_file_number() 
{
  echo 0
} 

is_file_in_processing()
{
 file_name=$1 
 before_processing=$(file_exists ${file_name}) 
 is_processing=$(file_exists "${file_name}.processing")
 return true
}

is_file_producing_db()
{
 return $(file_exists "${file_name}.db");
 }

is_file_producing_report()
{

 return true

 }
file_exists()
{
 return true
 } 
main
