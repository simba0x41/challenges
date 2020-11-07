#!/bin/bash

myname=$(whoami)

#cd /var/spool/$myname
#echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo $i
        #echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        #if [ "${owner}" = "bandit23" ]; then
         #   timeout -s 9 60 ./$i
        #fi
        #rm -f ./$i
    fi
done
