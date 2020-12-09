#!/bin/bash
input="100screen_names.txt"

while IFS= read -r line
do 
	count= grep -c "$line" "tweets.json"
	echo "$line"
	echo "$count"
done < "$input"
