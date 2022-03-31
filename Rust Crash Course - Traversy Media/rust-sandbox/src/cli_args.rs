use std::env;

pub fn run() {

    // Retrieve the arguments passed through the CLI (cargo run arg1 arg2 ...)
    // The first element element of the vector will always be the target executable
    // for the "cargo run" command. The following elements are rest of the arguments
    let args: Vec<String> = env::args().collect();

    // Get the second element (first argument)
    let command = args[1].clone();
    println!("Command: {:?}", command);

    // Print depending on the command
    if command == "uwu" {
        println!("Hewow Wowld");
    }
    else if command == "status" {
        println!("Not uwu");
    }
    else {
        println!("Unrecognized command");
    }

}