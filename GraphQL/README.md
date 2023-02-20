# GraphQL
- a query language for your API
- provide clients that power to ask for exactly what they need and nothing more
- get all the data your app needs in a single request
- better alternative to REST

### Flow
Client (query) > GraphQL Server > Database

# Types

#### `Scalar`
- Int
- Float
- String
- Boolean
- ID
- Enums

For example:
```graphql
type Author {
    id: ID
    firstName: String
    lastName: String
    rating: Float
    numOfCourses: Int
}

enum languages {
    ENGLISH
    JAPANESE
    GERMAN
}
```

### `Query` and `Mutation`
- Query
- Mutations

For example:
```graphql
type Query {
    author_details: [Author]
}

type Mutation {
    addAuthor(firstName: String, lastName: String): Author
}
```

### Non-Nullable
- Use `!` character after the type to declare it as non-nullable type

For example:
```graphql
type Author {
    id: ID!
    firstName: String
    lastName: String
    rating: Float
    numOfCourses: Int
    courses: [String!]
}
```

# Queries
- GraphQL query is all about asking for specific fields on objects

### `Fields`
```graphql
{
  viewer {
    login
    company
    createdAt
    email
    id
  }
}
```

### `Arguments`
- you can pass arguments to fields
- every field and nested object can get its own set of arguments, this gets rid of multiple API fetches


# Resources
- [GraphQL: The Big Picture](https://app.pluralsight.com/library/courses/graphql-big-picture/table-of-contents)