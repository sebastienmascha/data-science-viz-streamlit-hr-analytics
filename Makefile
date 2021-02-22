build:
	docker-compose -f docker-compose.dev.yaml build
up:
	docker-compose -f docker-compose.dev.yaml up -d
restart:
	make build
	make up

down:
	docker-compose -f docker-compose.dev.yaml down

deploy:
	docker-compose -f docker-compose.prod.yaml build
	docker-compose -f docker-compose.prod.yaml up -d
