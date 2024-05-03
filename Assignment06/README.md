# University Managment
<a href='https://pydeploy-course.onrender.com/docs'>Demo</a>

## Install the dependencies:
```shell
pip install --no-cache-dir --upgrade -r requirements.txt
```
## Config Database database.py (Postgesql):
```shell
SQLALCHEMY_DATABASE_URL = "postgresql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]"
```
## Start the application:
```shell
uvicorn server:app --host 127.0.0.4 --reload
```


## Dependencies
* fastapi
* uvicorn
* pydantic
* sqlalchemy
* psycopg2

![alt text](<Screenshot (104).png>)