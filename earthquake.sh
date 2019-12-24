echo "Inserisci la data iniziale"
read starttime

echo "Inserisci la data finale"
read endtime

curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime=${starttime}T00:00:00&endtime=${endtime}T22:22:00&format=text" > terremoti.txt;


echo "Inserisci il luogo da cercare:"
read place 
echo Cerco
grep -w -i "$place" terremoti.txt;
grep -w -i "$place" terremoti.txt > terremotifiltrato.txt;

input="terremotifiltrato.txt"
while IFS= read -r line
do
echo "$line"
telegram-send "$line"
done < "$input"
exit