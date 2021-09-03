# Entity Framework (EF) Core
_Entity Framework (EF) Core_ is a lightweight, extensible, open source and cross-platform version of the popular Entity Framework data access technology.

## Benefits
- can serve as an object-relational mapper (O/RM) that enables developers to work with a database using .NET objects.
- eliminates the need to write SQL code

# Tutorials

### How to add EF Core to your application?
1. Prepare the following requirements:
    - Domain class
    - Database context
    - Application configuration
    - Packages (.NET Core 3/5)
2. Add the required packages via NuGet package manager:
    - Microsoft.EntityFrameworkCore.SqlServer
    - Microsoft.EntityFrameworkCore.Tools   
3. Create the DbContext class
4. Add the database connection string in `appsettings.json` file
5. Add your DbContext in the `ConfigureServices` method in `Startup.cs`

### How to migrate your database?
1. Use `add-migration <migration name>` to generate migration code
2. Use `update-database` to execute SQL code to database

**Reminders**
- Use the `update-database` command when transferring your project from your local machine to another
