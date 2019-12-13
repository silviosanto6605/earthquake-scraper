#!usr/bin/bash

echo "Inserisci il luogo da cercare:"
read place 

echo Cerco
if
  grep -i "$place" terremoti.txt;
then
  exit

else
  echo "Il luogo specificato non è disponibile, prova a ricercare."
  exit
fi