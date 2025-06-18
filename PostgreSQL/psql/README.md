# psql
- `psql` is a terminal-based front-end to PostgreSQL.
- It enables you to type in queries interactively, issue them to PostgreSQL, and see the query results.

# Usage

### Connect to database
```
psql -d postgres
```

This will connect to the PostgreSQL database using the current user targeting a specific database.

### Create a database
```
CREATE DATABASE database_name WITH OWNER user;
```



### References
- [PostgreSQL: Documentation: 17: psql](https://www.postgresql.org/docs/current/app-psql.html)
