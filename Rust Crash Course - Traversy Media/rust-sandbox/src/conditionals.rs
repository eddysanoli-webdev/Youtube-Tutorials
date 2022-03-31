pub fn run() {

    let age: u8 = 18;
    let check_id: bool = false;
    let knows_person_of_age = true;

    // If-else
    if age >= 21 && check_id || knows_person_of_age {
        println!("Able to drink");
    }
    else if age < 21 && check_id {
        println!("You are not able to drink!");
    }
    else {
        println!("Able to drink, but need to check your ID")
    }

    // Theres no ternary operator in rust, but theres a shorthand if
    let is_of_age = if age >= 21 {true} else {false};
    println!("Is of Age: {}", is_of_age);

}