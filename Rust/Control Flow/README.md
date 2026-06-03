# Control Flow

### `if` expression

```rust
if 5 > 0 {
    println!("True");
}
else {
    println!("False");
} 
```

### `loop`

```rust
loop {
    println!("forever!");
}
```

### `while`

```rust
let mut number = 3;

while number != 0 {
    println!("{number}!");
    number -= 1;
}
```

### `for`

```rust
let a = [10, 20, 30, 40, 50];

for element in a {
    println!("the value is: {element}");
}
```




## References
- [Control Flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
