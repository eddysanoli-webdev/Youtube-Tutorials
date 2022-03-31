use std::mem;

// Arrays: Fixed list where elements are the same data type
pub fn run() {

    // Array of 5 int32 numbers 
    let mut numbers: [i32; 5] = [1, 2, 3, 4, 5];

    // Re-assign value
    numbers[2] = 20;

    // Print the whole array with the debug trait
    println!("{:?}", numbers);

    // Get single value
    println!("Single Value: {}", numbers[0]);

    // Array length
    println!("Array Length: {}", numbers.len());

    // Get memory used in bytes
    // NOTE: We pass the function a reference to the memory address, not the variable itself
    // NOTE: Arrays are stack allocated (Data thats declared as variables within a function)
    println!("Array occupies {} bytes", mem::size_of_val(&numbers));

    // Get the first two elements of the array
    // (We need to "borrow" the value of "number" by using &, that way we will prevent
    // errors during compilation)
    let slice: &[i32] = &numbers[0..2];
    println!("Slice: {:?}", slice);


}