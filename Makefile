.PHONY = install
install: 
	docker-compose exec api pip install -r requirements.txt