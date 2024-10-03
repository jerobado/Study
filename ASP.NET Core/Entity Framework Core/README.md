# Entity Framework (EF) Core
_Entity Framework (EF) Core_ is a lightweight, extensible, open source and cross-platform version of the popular Entity Framework data access technology.

## Benefits
- can serve as an object-relational mapper (ORM) that enables developers to work with a database using .NET objects.
- eliminates the need to write SQL code

# Tutorials

### How to add EF Core to your application?
1. Prepare the following requirements:
    - Domain class
    - Database context
    - Application configuration
    - Packages (.NET 8)
2. Add the required packages via NuGet package manager:
    - Microsoft.EntityFrameworkCore.SqlServer
    - Microsoft.EntityFrameworkCore.Tools
    - Microsoft.EntityFrameworkCore.Design
3. Create the DbContext class
4. Add the database connection string in `appsettings.json` file
5. Add your DbContext in the `Programs.cs`

### Example

_SampleContext.cs_
```C#
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace Intro;

public class BloggingContext : DbContext
{
    public DbSet<Blog> Blogs { get; set; }
    public DbSet<Post> Posts { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer(
            @"Server=(localdb)\mssqllocaldb;Database=Blogging;Trusted_Connection=True;ConnectRetryCount=0");
    }
}

public class Blog
{
    public int BlogId { get; set; }
    public string Url { get; set; }
    public int Rating { get; set; }
    public List<Post> Posts { get; set; }
}

public class Post
{
    public int PostId { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }

    public int BlogId { get; set; }
    public Blog Blog { get; set; }
}
```

### How to migrate your database?
1. Use `add-migration <migration name>` to generate migration code
2. Use `update-database` to execute SQL code to database

**Reminders**
- Use the `update-database` command when transferring your project from your local machine to another

## References
- [Razor Pages with Entity Framework Core in ASP.NET Core - Tutorial 1 of 8](https://learn.microsoft.com/en-us/aspnet/core/data/ef-rp/intro?view=aspnetcore-8.0&tabs=visual-studio-code)
