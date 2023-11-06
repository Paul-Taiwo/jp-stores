#!/bin/bash

echo -n "Starting "

python manage.py migrate

fixtures=$(ls seeds/)
while IFS= read -r fixture; do
    echo -n "Seeding "
    echo $fixture
    python manage.py loaddata seeds/$fixture
done <<< "$fixtures"