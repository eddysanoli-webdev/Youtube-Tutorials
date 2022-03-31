// Enums: Types which have a few definite values

// We have a game with a movement controller
// This are the variants for the movement
enum Movement {
    Up, 
    Down,
    Left,
    Right
}

// Movement function
fn move_avatar(m: Movement) {
    match m {
        Movement::Up => println!("Avatar moving up"),
        Movement::Down => println!("Avatar moving down"),
        Movement::Left => println!("Avatar moving left"),
        Movement::Right => println!("Avatar moving right")
    }
}

pub fn run() {

    // This will return 3 "variant is never constructed" warnings
    // as "down", "left" and "right" are never used
    let avatar = Movement::Up;
    move_avatar(avatar);

}