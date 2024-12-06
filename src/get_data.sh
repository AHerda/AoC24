#!/bin/bash

day=$1

url="https://adventofcode.com/2024/day/$day/input"
cookie_path="cookie/session"

echo "Fetching day: '$day' from url: '$url'"

mkdir -p data

# Obliczanie nazwy katalogu
dir_name=$(printf "data/day$day")

# Pobieranie danych i zapisywanie w odpowiednim katalogu
curl -s -b $(cat $cookie_path) $url >$dir_name

echo "Saved input to $dir_name"
