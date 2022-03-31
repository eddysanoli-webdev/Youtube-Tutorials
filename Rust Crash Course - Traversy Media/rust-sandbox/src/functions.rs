
// Functions: Used to store blocks of code for re-use
pub fn run() {

    greeting("Hey", "Becky");

    // We bind the return value of the function to a variable
    let get_sum = add(5,5);
    println!("Sum: {}", get_sum);

    // Closure
    // Similar to a lambda function. It also allows us to use variables from outsite
    // the local scope of the function (unlike a regular function)
    let n3: i32 = 10;
    let add_nums = |n1: i32, n2: i32| n1 + n2 + n3;
    println!("Closure Sum: {}", add_nums(3,3));
}

fn greeting(greet: &str, name: &str) {
    println!("{} {}, want sum fuk?", greet, name);
}

// If we dont use a semicolon, the line without the semicolon
// is interpreted as the value that we want to return
fn add(n1: i32, n2: i32) -> i32 {
    n1 + n2
}