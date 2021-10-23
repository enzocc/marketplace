## Database

To run a database migration:

```bash
docker exec -it api alembic revision --autogenerate -m "my very important migration!"
```
this will create a new file in `alembic/versions` (use `git status` to see which). Adjust it as necessary and when ready
test the upgrade and/or downgrade with
```bash
docker exec -it portal2_hestia_1 alembic upgrade +1
docker exec -it portal2_hestia_1 alembic downgrade +1
```
these migrations are autoapplied when you `crane lift`.
