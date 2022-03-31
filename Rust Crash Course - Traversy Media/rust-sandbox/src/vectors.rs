use std::mem;

// Vectors: Resizable arrays
pub fn run() {

    // Vector of 5 initial values
    let mut numbers: Vec<i32> = vec![1, 2, 3, 4, 5];

    // Re-assign value
    numbers[2] = 20;

    // Add on to the vector
    numbers.push(5);
    numbers.push(6);

    // Pop off the last value
    numbers.pop();

    // Print the whole array with the debug trait
    println!("{:?}", numbers);

    // Get single value
    println!("Single Value: {}", numbers[0]);

    // Vector length
    println!("Vector Length: {}", numbers.len());

    // Get memory used in bytes
    // NOTE: We borrow the value of the vector to prevent errors
    // NOTE: Arrays are stack allocated (Data thats declared as variables within a function)
    println!("Vector occupies {} bytes", mem::size_of_val(&numbers));

    // Get the first two elements of the vector
    // (We need to "borrow" the value of "number" by using &, that way we will prevent
    // errors during compilation)
    let slice: &[i32] = &numbers[0..2];
    println!("Slice: {:?}", slice);

    // Loop through vector values
    for x in numbers.iter() {
        println!("Number: {}", x);
    }

    // Loop and mutate values
    // Multiply each value by 2. Also valid for arrays
    for x in numbers.iter_mut() {
        *x *= 2;
    }
    println!("Mutated Vector: {:?}", numbers);
}