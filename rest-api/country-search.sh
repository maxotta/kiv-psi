#!/bin/sh

while read -p 'Country: ' COUNTRY; do
    echo '\n'
    curl https://restcountries.eu/rest/v2/name/$COUNTRY
    echo '\n'
done
