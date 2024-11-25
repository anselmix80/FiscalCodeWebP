#!/bin/bash
# figlet -f slant -c "FISCALCODE"

echo "    _______________ _________    __    __________  ____  ______"
echo "   / ____/  _/ ___// ____/   |  / /   / ____/ __ \/ __ \/ ____/"
echo "  / /_   / / \__ \/ /   / /| | / /   / /   / / / / / / / __/   "
echo " / __/ _/ / ___/ / /___/ ___ |/ /___/ /___/ /_/ / /_/ / /___   "
echo "/_/   /___//____/\____/_/  |_/_____/\____/\____/_____/_____/   "

docker compose down --volumes --remove-orphans --rmi all
docker system prune -a -f
docker compose up --build -d