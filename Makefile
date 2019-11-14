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
	docker-compose exec api pip install -r /opt/app/requirements.txt