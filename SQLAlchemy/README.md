# SQLAlchemy
- SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

### ORM Quick Start
1. Declare models
2. Create an Engine
3. Create tables

#### Example:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column,
                            Session)

# declare models
class Base(DeclarativeBase):
    pass

class IncomeStatement(Base):
    __tablename__ = 'income_statement'

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int]
    company_name: Mapped[str]
    gross_revenue: Mapped[float]
    net_income: Mapped[float]

# create database engine
database = 'sqlite:///sample.db'
engine = create_engine(database, echo=True)

# create tables
Base.metadata.create_all(engine)

# insert record
with Session(engine) as session:
    dnl = IncomeStatement(year=2016,
                          company_name='DNL',
                          gross_revenue=22232396304,
                          net_income=2629682992)
    session.add(dnl)
    session.commit()
```  

### References
- [SQLAlchemy - The Database Toolkit for Python](https://www.sqlalchemy.org/)
- [ORM Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)