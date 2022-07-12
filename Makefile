tests:
	pytest test/ -v -s

linters:
	isort src/
	isort test/
	isort app.py
	isort celery_worker.py
	isort settings.py
	black src/ --line-length=100
	black test/ --line-length=100
	isort app.py --line-length=100
	isort celery_worker.py --line-length=100
	isort settings.py --line-length=100


tasks:
	celery -A celery_worker.celery worker --loglevel=info

beat:
	celery -A celery_worker.celery beat --loglevel=info

make-migrations:
	alembic revision --autogenerate

migration:
	alembic upgrade head
