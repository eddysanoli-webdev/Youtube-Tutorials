// NOTES:
// - Variables hold primitive data or references to data
// - Variables are inmutable by default (they cannot be re-assigned)
// - Rust is a block-scoped language (Variables inside a
//   function are local to said function).

pub fn run() {

    // Add mutable keyword to allow reassignment
    let name = "Brad";
    let mut age = 37;
    println!("My name is {}, age {}", name, age);

    // Change the age
    age = 38;
    println!("My name is {}, age {}", name, age);

    // Constants need an explicit type
    // (Constants are not really used)
    const ID: i32 = 1;
    println!("ID: {}", ID);

    // Assign multiple variables
    let ( my_name, my_age ) = ("Eddy", 25);
    println!("{} is {}", my_name, my_age);
}