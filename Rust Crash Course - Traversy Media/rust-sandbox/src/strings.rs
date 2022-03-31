// Two Types of String:
// - Primitive: Inmutable fixed-length string somewhere in memory
// - String: Growable, heap-allocated data structure (Heap memory is where modifyable data
//   is stored). Use when you want to modify the string data.

pub fn run() {

    // Primitive string
    let hello = "Hello";

    // Growable string
    let mut hello2 = String::from("Hello ");

    // Get length
    println!("Length: {}", hello2.len());

    // Push a single character at the end of the string
    hello2.push('W');

    // Push a multi-char string
    hello2.push_str("orld!");

    // Get capacity: The number of bytes that a string can store
    println!("Capacity: {}", hello2.capacity());

    // Check if string is empty
    println!("Is Empty: {}", hello2.is_empty());

    // Contains
    println!("Contains 'World' {}", hello2.contains("World"));

    // Replace
    println!("Replace: {}", hello2.replace("World", "There"));

    // Split the string by its whitespace, and print each word in a new line
    for word in hello2.split_whitespace() {
        println!("{}", word);
    }

    // Create a string with a certain capacity
    let mut s = String::with_capacity(10);
    s.push('a');
    s.push('b');

    // Assertion testing
    // Check if the length of "s" is 2, and its capacity is 10. 
    // If it passes, nothing happens. On the flipside, when it fails it displays an error.
    assert_eq!(2, s.len());
    assert_eq!(10, s.capacity());

    // Print the final string
    println!("{}", hello2);

}