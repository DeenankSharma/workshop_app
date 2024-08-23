const post_btn = document.getElementById("post_btn");
const message = document.getElementById("message");
const username = document.getElementById("username");


post_btn.addEventListener("click", (event) => {
    event.preventDefault()
    postData(username.value,message.value)
})


function postData(username, message) {
    let data = { "username": username, "message": message };
    fetch("http://127.0.0.1:5000/add", 

        {   method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data) }).then(response => {
                // Check if the request was successful
                if (!response.ok) {
                  throw new Error('Network response was not ok');
                }
                // Parse the response as JSON
                return response.json();
              })
              .then(data => {
                // Handle the JSON data
                console.log(data);
              })
              .catch(error => {
                // Handle any errors that occurred during the fetch
                console.error('Fetch error:', error);
              });
}