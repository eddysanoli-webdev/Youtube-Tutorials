
// Tuples: Grouped together values of different types. Max elements: 12

pub fn run() {

    // Person tuple with types: (Primitive String, Primitive String, 8 bit integer)
    let person: (&str, &str, i8) = ("Eddy", "Guatemala", 25);

    println!("{} is from {} and is {}", person.0, person.1, person.2);

}