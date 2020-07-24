run:
	docker-compose up -d

run-bash:
	docker-compose run webserver bash

run-test:
	docker-compose exec webserver .local/bin/pytest