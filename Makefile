.PHONY = up
up: 
	docker-compose up -d

.PHONY = build
build:
	docker-compose build

.PHONY = down
down:
	docker-compose down

.PHONY = install
install:
	docker-compose exec api pip install -r requirements.txt

.PHONY = tests
tests:
	docker-compose exec api python -m unittest testApp.py

.PHONY = logs
logs:
	docker-compose logs -f