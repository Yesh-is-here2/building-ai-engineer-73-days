Run (requires Docker Desktop):

cd phase1_core_ml/06_postgres_connection_test
docker compose up -d
# apply SQL (copy container id if needed)
docker ps
# then:
# docker exec -i <CONTAINER_ID> psql -U yesh -d phase1db < setup.sql
python main.py
docker compose down
