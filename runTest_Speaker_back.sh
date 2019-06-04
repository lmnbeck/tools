#!/bin/sh
dicPath="./dic/trig.vtdic"
#wavPath="../Test_data/WAVE/SPEAKER0024/SESSION0/"
wavPath="../Test_data/WAVE/SPEAKER0"$1"/SESSION0/"
i=1

if [ "$#" -ne "2" ]; then
	exit 2
fi

for element in $(ls $wavPath); do
	#statements
	if [ "$i" -eq "1" ]; then
		#statements
		echo "    trig--=======>"
	elif [ "$i" -eq "11" ]; then
		#statements
		echo "    func--=======>"
	elif [ "$i" -eq "31" ]; then
		#statements
		echo "    time--=======>"
	elif [ "$i" -eq "64" ]; then
		#statements
		echo "    func--=======>"
	fi
	
	if [ "$i" -le "10" ]; then
		#echo $element
		#statements
		dicPath="./dic/trig.vtdic"
	elif [ "$i" -ge "31" ] && [ "$i" -le "63" ]; then
		#statements
		dicPath="./dic/time.vtdic"
	else
		dicPath="./dic/func.vtdic"
	fi

	./demo.exe $dicPath $wavPath$element $2

	i=$(($i+1))
	#echo $i
done

