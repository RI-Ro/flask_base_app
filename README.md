# flask_base_app

# Шаблон простого приложения на flask 

# Установите flask, flask-restful, flask-cors
pip3 install flask-cors flask-restful flask

#  Скачайте код из примера для развертывания шаблона приложения на flask

export FLASK_APP=runserver.py
export FLASK_DEBUG=True
# Создаем в базе данных sqlite таблицу users
flask db init
flask db migrate -m "Users models for test"
flask db upgrade
# Запускам наш код
flask run
# И переходим в браузере http://127.0.0.1:5000/ 
