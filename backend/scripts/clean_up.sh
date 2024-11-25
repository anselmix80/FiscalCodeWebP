#!/bin/bash

echo "    _______________ _________    __    __________  ____  ______"
echo "   / ____/  _/ ___// ____/   |  / /   / ____/ __ \/ __ \/ ____/"
echo "  / /_   / / \__ \/ /   / /| | / /   / /   / / / / / / / __/   "
echo " / __/ _/ / ___/ / /___/ ___ |/ /___/ /___/ /_/ / /_/ / /___   "
echo "/_/   /___//____/\____/_/  |_/_____/\____/\____/_____/_____/   "

# Remove migrations
rm -rf ../api/migrations
rm -rf ../weather/migrations

# Remove static
rm -rf ../static

# Remove logs
rm -f ../logs/*.log
rm -f ../logs/*.log.*

# Remove cache
rm -rf ../api/__pycache__
rm -rf ../weather/__pycache__
rm -rf ../calc/__pycache__
rm -rf ../fiscal_code/__pycache__
rm -rf ../../cmd/__pycache__
rm -rf __pycache__

# Remove commons files and NoSQL
rm -f ../commons.csv
rm -f ../../cmd/commons.csv
rm -f ../output.csv
rm -f ../../cmd/output.csv
rm -f ../db.sqlite3

# Remove venv
rm -rf ../../venv

# Remove Npm
rm -rf ../../frontend/node_modules