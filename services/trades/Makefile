run-dev:
	uv run python run.py

run-dev-historical:
	cp historical.settings.env settings.env
	uv run python run.py

build:
	docker build -f multistage.Dockerfile -t trades .

run: build
	docker run -it \
		--network redpanda_network \
		-e KAFKA_BROKER_ADDRESS=redpanda:9092 \
		--env-file settings.env \
		trades

# build-multistage:
# 	docker build -f multistage.Dockerfile -t trades:multistage .

# run-multistage: build-multistage
# 	docker run -it \
# 		--network redpanda_network \
# 		-e KAFKA_BROKER_ADDRESS=redpanda:9092 \
# 		trades:multistage

# build-all: build build-multistage