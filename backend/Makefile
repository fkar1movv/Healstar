start_mysql:
	docker run --name healstar_db \
	-v db_data:/var/lib/mysql \
	-e MYSQL_DATABASE=healstar \
	-e MYSQL_ROOT_PASSWORD=russ \
	-p 3306:3306 \
	-d mysql:8.2

docker_build:
	docker build -t healstar_back .

docker_run:
	docker run --name healstar_web \
	-v "/Users/rustam/Personal/healstar":/app \
	--rm \
	-p 9001:8000 \
	--env-file .env \
	-d healstar_back
