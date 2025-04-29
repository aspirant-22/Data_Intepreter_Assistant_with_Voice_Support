function startVoiceInput() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const speechText = event.results[0][0].transcript;
        document.getElementById("userText").textContent = speechText;

        fetch('/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: speechText })
        })
        .then(res => res.json())
        .then(data => {
            const response = data.response;
            document.getElementById("botResponse").textContent = response;
            speak(response);
        });
    };
}

function speak(text) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);
    synth.speak(utterance);
}
