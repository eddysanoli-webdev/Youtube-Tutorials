// Public function to make it accesible from outside
pub fn run() {

    // Print to console
    println!("Hello from the print.rs file");

    // Basic Formatting: Print with string literal
    println!("Number: {}", 1);

    // Positional Arguments
    // We tell each "{}", which of the following parameters we want there
    println!("{0} is from {1} and {0} likes to {2}", "Eddy", "Guatemala", "code");

    // Named arguments
    println!("{name} likes to play {activity}", name="John", activity="deez nutz");

    // Placeholder traits
    // Prints the binary, hex and octal for the number given
    println!("Binary: {0:b} / Hex: {0:x} / Octal: {0:o}", 10);

    // Placeholder for debug trait
    // Be able to print tuples and arrays
    println!("{:?}", (12, true, "Hello"));
}