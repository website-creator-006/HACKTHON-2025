document.addEventListener("DOMContentLoaded", function () {
        const chatBox = document.getElementById("chat-box");
        const userInput = document.getElementById("user-input");
        const sendButton = document.getElementById("send-btn");
    
        function appendMessage(sender, message) {
            const messageElement = document.createElement("p");
            messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    
        function sendMessage() {
            const message = userInput.value.trim();
            if (message === "") return;
            
            appendMessage("You", message);
            userInput.value = "";
            
            fetch("/chatbot", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => appendMessage("Bot", data.response))
            .catch(error => appendMessage("Bot", "Oops! Something went wrong. Please try again later."));
        }
    
        sendButton.addEventListener("click", sendMessage);
        userInput.addEventListener("keypress", function (event) {
            if (event.key === "Enter") sendMessage();
        });
    });
    