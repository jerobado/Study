# SQLite
- SQLite is an open-source, zero-configuration, self-contained, stand-alone, transaction relational database engine designed to be embedded into an application.


### SQLite CLI commands

### Create a database
```
sqlite3 <database-name>
```

### Create a table
```
sqlite> create table if not exist <table-name> (
    column1 integer not null primary key,
    column2 text not null,
    column3 text,
    column4 integer
);
```

### Insert records to a table
```
sqlit3> insert into <table-name> (column1, column2, column3)
values ('required', 'text', 1);
```


### Open an existing database
```
sqlite> .open <database-name>.db
```



### References
- [SQLite Tutorial - An Easy Way to Master SQLite Fast](https://www.sqlitetutorial.net/)

