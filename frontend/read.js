const bigContainer = document.getElementById("big-container");

function getPosts() {
    let fetchRes = fetch("http://127.0.0.1:5000/read",{method: 'GET'});
    fetchRes.then(res =>
        res.json())
        .then(data => {
            console.log(data)
            appendPosts(data)
        })
}

function appendPosts(data){
    let messages = data['messages'];
    if(messages.length != 0){
        for (let i = 0;i<messages.length;i++){
            const div = document.createElement("div")
            const h6 = document.createElement("h6")
            const p = document.createElement("p")
            h6.innerHTML = messages[i][1]
            p.innerHTML = messages[i][2]
            div.appendChild(h6)
            div.appendChild(p)
            div.classList.add("card")
            bigContainer.appendChild(div)
        }
    }
    else{
        const p = document.createElement("p")
        p.innerHTML = "No posts to display yet!"
        p.classList.add("no-messages")
        bigContainer.after(p)
    }
    
}


window.addEventListener("load",()=>{
    getPosts()
})