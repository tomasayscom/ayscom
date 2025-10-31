sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose
sudo service docker start
sudo usermod -aG docker $USER
sudo apt install -y python3 python3-pip python3-venv
sudo apt install -y python3-psycopg2 python3-pandas
sudo apt install -y nano curl wget git unzip
