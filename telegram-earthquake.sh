#!/bin/bash
date=$(date '+%Y-%m-%d')

if [ "$3" = "-v" ] || [ "$3" = "--verbose" ]; then   #verbose output
    curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime=$1T00:00:01&endtime=${date}T23:59:59&format=text" > terremoti.txt;
    echo Cerco
    grep -w -i -q "$2" terremoti.txt;
    grep -w -i "$2" terremoti.txt > terremotifiltrato.txt;
    input="terremotifiltrato.txt";
    while IFS= read -r line
    do
    echo $line
    telegram-send "$line"                             
    done < "$input"
    2>/dev/null
    exit


elif [ "$3" = "-e" ] || [ "$3" = "--endtime" ]; then   #customized end time
    curl -s "http://webservices.ingv.it/fdsnws/event/1/query?starttime=$1T00:00:01&endtime=$4T23:59:59&format=text" > terremoti.txt;
    echo Cerco
    grep -w -i -q "$2" terremoti.txt;
    grep -w -i "$2" terremoti.txt > terremotifiltrato.txt;
    awk -F "|" 'BEGIN{OFS="|"}{print $2,$10,$11,$12,$13}' terremotifiltrato.txt > terremotifiltrato2.txt;
    input="terremotifiltrato2.txt";
    while IFS= read -r line
    do
    echo $line
    telegram-send "$line"                          
    done < "$input"
    2>/dev/null
    exit



elif [ "$2" = "-a" ] || [ "$2" = "--all" ]; then   #list all earthquakes
    curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime=$1T00:00:01&endtime=${date}T23:59:59&format=text" > terremoti.txt;
    awk -F "|" 'BEGIN{OFS="|"}{print $2,$10,$11,$12,$13}' terremoti.txt > terremotifiltrato2.txt;
    input="terremotifiltrato2.txt";
    while IFS= read -r line
    do
    echo $line
    telegram-send "$line"                                       
    done < "$input"
    2>/dev/null
    exit

else
    curl -s "http://webservices.ingv.it/fdsnws/event/1/query?starttime=$1T00:00:01&endtime=${date}T23:59:59&format=text" > terremoti.txt;
    echo Cerco
    grep -w -i -q "$2" terremoti.txt;
    grep -w -i "$2" terremoti.txt > terremotifiltrato.txt;
    awk -F "|" 'BEGIN{OFS="|"}{print $2,$10,$11,$12,$13}' terremotifiltrato.txt > terremotifiltrato2.txt;
    input="terremotifiltrato2.txt";
    while IFS= read -r line
    do
    echo $line
    telegram-send "$line"
    done < "$input"
    2>/dev/null
    exit

fi