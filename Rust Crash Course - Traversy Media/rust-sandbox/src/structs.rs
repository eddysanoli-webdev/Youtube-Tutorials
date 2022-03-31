
// Structs: Used to create custom data types (Similar to an object in javascript)

// Traditional Struct
// Create struct for RGB colors
struct Color {
    red: u8,
    green: u8,
    blue: u8
}

// Tuple struct
struct ColorCMY(u8, u8, u8);

// ===================
// Struct Methods

// Struct Declaration
struct Person {
    first_name: String,
    last_name: String
}

// Struct Methods
impl Person {

    // Construct a person
    fn new(first: &str, last: &str) -> Person {
        Person {
            first_name: first.to_string(),
            last_name: last.to_string()
        }
    }

    // Get full name
    // Return a formatted string with the full name. Works very similar to println!()
    // NOTE: Self works very similar to self in python and "this" in javascript
    fn full_name(&self) -> String {
        format!("{} {}", self.first_name, self.last_name)
    }

    // Set last name
    // We get a reference to "self" but its a mutatable version of it
    fn set_last_name(&mut self, last: &str) {
        self.last_name = last.to_string();
    }

    // Name to tuple
    fn name_to_tuple(self) -> (String, String) {
        (self.first_name, self.last_name)
    }
}

// =================
// Main Loop
pub fn run() {

    // Create a color instance
    let mut c = Color {
        red: 255,
        green: 0,
        blue: 0
    };

    // Change the "green" property
    c.green = 200;

    // Get properties using dot indexing
    println!("Color: R {} G {} B {}", c.red, c.green, c.blue);

    // Use and modify the tuple struct
    let mut c2 = ColorCMY(0, 100, 200);
    c2.0 = 50;
    println!("Color: C {} M {} Y {}", c2.0, c2.1, c2.2);

    // Create a new person and change its last name
    let mut person = Person::new("Eddy", "Sanoli");
    person.set_last_name("Santizo");
    println!("Person: {}", person.full_name());
    println!("Name Tuple: {:?}", person.name_to_tuple());

}