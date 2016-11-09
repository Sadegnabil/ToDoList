virtualenv -p python3 venv
source venv/bin/activate
./install_flask.sh
./create_database.sh
python run.py