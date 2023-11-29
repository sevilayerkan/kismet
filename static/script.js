document.addEventListener('DOMContentLoaded', function () {
    const getFortuneButton = document.getElementById('getFortuneButton');
    const fortuneResult = document.getElementById('fortuneResult');

    getFortuneButton.addEventListener('click', function () {
        fetch('/api/fortune', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: 'What is my fortune?',
            }),
        })
        .then(response => response.json())
        .then(data => {
            fortuneResult.innerText = 'Your Fortune: ' + data.fortune;
        })
        .catch(error => {
            console.error('Error fetching fortune:', error);
            fortuneResult.innerText = 'Error fetching fortune.';
        });
    });
});
