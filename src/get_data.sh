#!/bin/bash

day=$1

url="https://adventofcode.com/2024/day/$day/input"
cookie_path="cookie/session"

echo "Fetching day: '$day' from url: '$url'"

# Obliczanie nazwy katalogu
dir_name=$(printf "data/zad%02d-%02d" $((day * 2 - 1)) $((day * 2)))

# Pobieranie danych i zapisywanie w odpowiednim katalogu
curl -s -b $(cat $cookie_path) $url > $dir_name

echo "Saved input to $dir_name"
