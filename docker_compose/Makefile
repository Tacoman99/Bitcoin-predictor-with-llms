start_redpanda:
	docker compose -f redpanda.yml up -d

stop_redpanda:
	docker compose -f redpanda.yml down
	
add-one-partition-to-trades-topic:
	docker compose -f redpanda.yml exec redpanda rpk topic add-partitions trades --num 1
