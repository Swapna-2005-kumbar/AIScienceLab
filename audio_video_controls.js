document.addEventListener("DOMContentLoaded", () => {
    const audioButton = document.querySelector(".btn-audio");
    const videoButton = document.querySelector(".btn-video");
    const aiOutput = document.querySelector(".ai-output");

    // Function to display output
    const displayOutput = (message) => {
        aiOutput.innerHTML = `<div class='ai-response-box'>${message}</div>`;
        aiOutput.classList.add("visible");
    };

    // Generate Audio
    audioButton.addEventListener("click", async () => {
        displayOutput("Generating audio... Please wait.");

        try {
            const response = await fetch("/generate-audio", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: "Hello, this is a generated audio example." })
            });

            if (response.ok) {
                const data = await response.json();
                displayOutput(`<audio controls><source src="${data.audioUrl}" type="audio/mpeg">Your browser does not support the audio element.</audio>`);
            } else {
                displayOutput("Failed to generate audio. Please try again.");
            }
        } catch (error) {
            displayOutput("An error occurred while generating audio.");
        }
    });

    // Generate Video
    videoButton.addEventListener("click", async () => {
        displayOutput("Generating video... Please wait.");

        try {
            const response = await fetch("/generate-video", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: "Hello, this is a generated video example." })
            });

            if (response.ok) {
                const data = await response.json();
                displayOutput(`<video controls><source src="${data.videoUrl}" type="video/mp4">Your browser does not support the video element.</video>`);
            } else {
                displayOutput("Failed to generate video. Please try again.");
            }
        } catch (error) {
            displayOutput("An error occurred while generating video.");
        }
    });
});