const prompt = require("prompt-sync")();

// api_key = 1ce11b9b

//const movie_name = prompt("Please enter movie: ");
const movie_name = process.env.MOVIE_NAME || "Inception";

get_info(movie_name);

async function get_info(movie_name) {
let base_url = 'http://www.omdbapi.com/?apikey=1ce11b9b&t='+movie_name;
    try {
        const response = await fetch(base_url);
        if (response.ok) {
            const movie_data = await response.json(); 
            console.log(movie_data.Title);
            console.log(movie_data.Year);
            console.log(movie_data.Director);
        } else {
            throw new Error('Failed to fetch data');
        }
    } catch (error) {
        console.error('Error:', error); 
    }
}