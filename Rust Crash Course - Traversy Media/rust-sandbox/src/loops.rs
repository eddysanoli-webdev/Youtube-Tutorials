// Loops: Used to iterate until a condition is met

pub fn run() {

    let mut count = 0;

    // Infinite loop
    // Will continue forever until it encounters a "break" statement
    loop {
        count += 1;

        if count == 20 {
            println!("Finished on Number: {}", count);
            break;
        }
    }

    // Reset the count
    count = 0;

    // While Loop (FizzBuzz)
    while count <= 100 {
        if count % 15 == 0 { println!("FizzBuzz"); }
        else if count % 3 == 0 { println!("Fizz"); }
        else if count % 5 == 0 { println!("Buzz"); }
        else { println!("{}", count); }

        count += 1;
    }

    // For range
    // Numbers from 0 to 99
    for x in 0..100 {
        if x % 50 == 0 { println!("Found 50 Multiple! {}", x); }
    }

}