# Many-to-many relationship
- Many-to-many relationships are used when any number entities of one entity type is associated with any number of entities of the same or another entity type. For example, a Post can have many associated Tags, and each Tag can in turn be associated with any number of Posts.

#### Example

```c#
public class Post
{
    public int Id { get; set; }
    public List<Tag> Tags { get; } = [];
}

public class Tag
{
    public int Id { get; set; }
    public List<Post> Posts { get; } = [];
}
```

### References
- [Many-to-many relationships](https://learn.microsoft.com/en-us/ef/core/modeling/relationships/many-to-many)