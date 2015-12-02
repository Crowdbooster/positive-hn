runservers:
	echo "Killing any leftover server processes"
	ps aux | grep -iE '[p]ython manage.py runserver|webpack --watch' | awk '{print $$2}' | xargs kill
	echo "Running webpack --progress --colors --watch & python manage.py runserver"
	webpack --progress --colors --watch & python manage.py runserver
