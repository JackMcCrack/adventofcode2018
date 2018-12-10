#!/bin/bash
FOO=0
for i in `cat input01`
do
	echo $FOO >>output01-1.txt
	FOO=$(($FOO + $i))
	if [ `grep -c -x \'$FOO\' output01-1.txt` -eq 1 ]
	then
		echo -n "$FOO "
	fi
done
#echo $FOO
