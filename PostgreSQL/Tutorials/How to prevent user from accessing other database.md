# How to prevent users from accessing other database

1. Revoke all users from connecting into a database in Public schema
    ```psql
    REVOKE CONNECT ON DATABASE <database name> FROM PUBLIC;
    ```

2. Grant specific user access/connect to that database
    ```
    GRANT CONNECT ON DATABASE <database name> TO <role name>;
    ```

# Resources
- [Created user can access all databases in PostgreSQL without any grants](https://dba.stackexchange.com/questions/17790/created-user-can-access-all-databases-in-postgresql-without-any-grants)