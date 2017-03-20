#!/bin/bash

# Example: ./getopts.sh -b world -a hello one two three
# Output: A=hello B=world 1=one 2=two 3=three 4=

while getopts "a:b:" opt; do
  case "$opt" in
  "a") A="$OPTARG";;
  "b") B="$OPTARG";;
  esac
done
shift $(( OPTIND - 1 ))

echo "A=$A B=$B 1=$1 2=$2 3=$3 4=$4"