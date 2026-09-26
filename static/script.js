const inputField = document.getElementById("url-input");
const submitButton = document.getElementById("url-button");

submitButton.addEventListener("click", async function() {
    const data = { url: inputField.value };

    try {
        const response = await fetch('/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        console.log("Success: ", result);
        document.getElementById('shorten-url').innerText = "Shorten URL: " + window.location.origin + "/" + result.short_code;
    } catch (error) {
        console.error("Error sending JSON: ", error);
    }
});