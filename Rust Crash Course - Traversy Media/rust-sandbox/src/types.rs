
// NOTE:
// 
// Primitive Types:
// - Unsigned Int: u8, u16, u32, u64, u128 (No sign. Number is the number of bits in memory)
// - Signed Int: i8, i16, i32, i64, i128 (Positives and negatives)
// - Floats: f32, f64
// - Boolean: true, false (Lowercase)
// - Characters: One character (Strings dont really exist in rust)
// - Tuples: Lists
// - Arrays: Fixed length (Vectors can change their dimensions)
// 
// Rust is statically typed, meaning that it must know the types of all the variables
// at compile time. However, the compiler can almost always infer what type we want to use
// based on the value and how its being used.

pub fn run() {

    // Default: i32
    let x = 1;

    // Default: f64
    let y = 2.5;

    // Add explicit type
    let z: i64 = 12321432523452;

    // Find max size
    // (Here we use the standard library)
    println!("Max i32: {}", std::i32::MAX);
    println!("Max f64: {}", std::f64::MAX);
}