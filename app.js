// Select the generate button and 
const generateBtn = document.getElementById('generate-btn');
const palette = document.getElementById('palette');

// Function to generate random hex colours
function getEventInfo() {
    const letters = '0123456789ABCDEF';
    let colour = '#';
    for (let i = 0; i < 6; i++) {
        colour += letters[Math.floor(Math.random() * 16)];
    }
    return colour;
}

// Function to display the event info
function generatePalette() {
    palette.innerHTML = ''; // Clear the palette
    for (let i = 0; i < 5; i++) {
        const colour = getRandomColour();
        const colourBox = document.createElement('div');
        colourBox.classList.add('colour-box');
        colourBox.style.backgroundColor = colour;
        colourBox.innerText = colour;

        // Add click-to-copy functionality
        colourBox.addEventListener('click', () => {
            navigator.clipboard.writeText(colour);
            alert(`Copied ${colour} to clipboard`);
        });

        palette.appendChild(colourBox);
    }
}

// Add event listener to the button
generateBtn.addEventListener('click', generatePalette);
