#!usr/bin/bash

echo "Inserisci il luogo da cercare:"
read place 

echo Cerco
grep -i $place terremoti.txt
exit