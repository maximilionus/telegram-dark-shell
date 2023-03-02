use std::fs;
use rand::seq::SliceRandom;

const PATH_NAMES_FILE: &str = "./data/names.txt";
const PATH_USED_NAMES_FILE: &str = "./data/used_names.txt";

fn main() {
    println!("Dark Shell - Release Naming Tool");
    println!("This tool will generate the random release name using the samples from '{}', excluding already used names, stated in '{}'\n", PATH_NAMES_FILE, PATH_USED_NAMES_FILE);

    let names_file_contents = fs::read_to_string(&PATH_NAMES_FILE).unwrap();
    let names_vec: Vec<&str> = names_file_contents.lines().collect();
    
    let used_names_contents = fs::read_to_string(&PATH_USED_NAMES_FILE).unwrap();
    let mut used_names_vec: Vec<&str> = used_names_contents.lines().collect();

    if used_names_vec.len() == names_vec.len() {
        println!("No unused names found. Update the database - \"{}\"", PATH_NAMES_FILE);
        return;
    }

    loop {
        let random_name = names_vec.choose(&mut rand::thread_rng()).unwrap();

        if !used_names_vec.contains(random_name) {
            // Add used name to "used_names.txt"
            used_names_vec.push(&random_name);
            fs::write(&PATH_USED_NAMES_FILE, used_names_vec.join("\n")).expect("Can not write the output to used names file");

            // Display the result
            println!("Generated Release Name: \"{}\"", random_name);
            break;
        }
    }
}
