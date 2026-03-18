# Troubleshooting


### ERROR:  duplicate key value violates unique constraint "table_name_pkey"

The max ID in your table and the newly added ID does not match. It needs to be in sync


Check the `last_value` field

```bash
select * from table_name_id_seq;
 last_value | log_cnt | is_called
------------+---------+-----------
         13 |      32 | t
```

Check the max ID of your table

```
select max(id) from homepage_contribution;
 max
-----
  15
```

If the `last_value` is left behind, this value needs to be reset by running the SQL below:

```sql
SELECT setval('table_name_id_seq', (SELECT MAX(id) FROM table_name)+1);
```

This will increase the value of last_value by 1 so that the next record will use this ID.
