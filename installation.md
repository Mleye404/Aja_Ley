python3 -m venv .venv #linux
.\venv\Scripts\Activate.ps1 #windows
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_ajaley
python manage.py createsuperuser
python manage.py runserver
