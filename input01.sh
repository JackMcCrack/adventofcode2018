#!/bin/bash
FOO=0
for i in `cat input01`
do
	FOO=$(($FOO + $i))
done
echo $FOO
