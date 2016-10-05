rm -r app.db db_repository
python db_create.py
python add_data_test.py
echo "Database reloaded"