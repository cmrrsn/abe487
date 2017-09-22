#!/bin/bash

if [[ $# -eq 0 ]]; then 
	printf "Usage: %s FILE [NUM]\n" "$(basename "$0")" 
	exit 1 
else	
	if [[ -f "$1" ]]; then
		if [[ $# -gt 1 ]]; then
			i=0
			while read -r LINE; do
				let i++
				if [[ i -le $2 ]]; then
					echo $LINE
				else
					break
				fi
			done<"$1"
		else 
			i=0
			while read -r LINE; do
				let i++
				if [[ i -le 3 ]]; then
					echo $LINE
				else
					break
				fi
			done<"$1"
		fi		
	else
		printf "\"%s\" is not a file\n" "$(basename "$1")"
		exit 1
	fi
fi
