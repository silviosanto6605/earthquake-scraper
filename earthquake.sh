clear

date=$(date '+%Y-%m-%d')

curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime=$1T00:00:00&endtime=${date}T22:22:00&format=text" > terremoti.txt;

echo Cerco
grep -w -i "$2" terremoti.txt;
grep -w -i "$2" terremoti.txt > terremotifiltrato.txt;
awk -F "|" 'BEGIN{OFS="|"}{print $2,$6,$11,$12,$13}' terremotifiltrato.txt > terremotifiltrato2.txt
input="terremotifiltrato2.txt";
while IFS= read -r line
do
telegram-send "$line";
done < "$input"
2>/dev/null
exit
