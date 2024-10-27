const votes = document.querySelectorAll("select.vote")

votes.forEach(vote => {
    vote.addEventListener("click", (e => {
        e.preventDefault()
        const selected_index = e.target.selectedIndex
        const selected_item = e.target.options[selected_index]
        const data = new URLSearchParams();
        data.append('question_id', e.target.getAttribute('id'));
        data.append('option_id', selected_item.value);
        fetch("/poll/result",{
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: data
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error(error));
    }));
});