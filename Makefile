server:
	@echo "Server is listening"
	python ./messenger/server/server.py

server:
	@echo "Server is listening"
	python ./messenger/client/client.py

migrate_up:
	@echo "Migrate up"
	migrate -path migrations -database "postgres://postgres:2505@localhost:5432/postgres?sslmode=disable" up

migrate_drop:
	@echo "Migrate drop"
	migrate -path migrations -database "postgres://postgres:2505@localhost:5432/postgres?sslmode=disable" drop