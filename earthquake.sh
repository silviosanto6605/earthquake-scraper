pip3 install telegram-send
clear

curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime=$1T00:00:00&endtime=$2T22:22:00&format=text" > terremoti.txt;


echo "Inserisci il luogo da cercare:"

echo Cerco
grep -w -i "$3" terremoti.txt;
grep -w -i "$3" terremoti.txt > terremotifiltrato.txt;

input="terremotifiltrato.txt"
while IFS= read -r line
do
telegram-send "$line"
done < "$input"
2>/dev/null
exit
