pip3 install telegram-send
clear

curl "http://webservices.ingv.it/fdsnws/event/1/query?starttime=${$1}T00:00:00&endtime=${$2}T22:22:00&format=text" > terremoti.txt;


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