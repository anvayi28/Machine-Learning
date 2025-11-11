async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="message user"><b>You:</b> ${message}</div>`;
  input.value = "";

 const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });
  const data = await response.json();

  chatBox.innerHTML += `<div class="message bot"><b>Bot:</b> ${data.response}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
