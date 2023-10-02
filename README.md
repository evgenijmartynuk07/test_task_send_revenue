# test_task_send_revenue


```shell
git clone https://github.com/evgenijmartynuk07/test_task_send_revenue.git
cd test_task_send_revenue

python -m venv venv
source venv/bin/activate

create .env based on .env.sample

python manage.py migrate

python manage.py loaddata spend.json
python manage.py loaddata revenue.json

python manage.py runserver

http://127.0.0.1:8000/api/doc/swagger/
```