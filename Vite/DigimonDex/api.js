let digimons = [];
let currentIndex = 0;

export async function fetchAllDigimons() {
    try {
        const response = await fetch(`https://digimon-api.vercel.app/api/digimon`);
        if (!response.ok) throw new Error('Erro ao buscar Digimons');
        digimons = await response.json();
    } catch (error) {
        console.error(error.message);
        digimons = [];
    }
}

export function searchDigimon(digimonName) {
    const searchResultIndex = digimons.findIndex(d => d.name.toLowerCase().includes(digimonName.toLowerCase()));

    if (searchResultIndex !== -1) {
        currentIndex = searchResultIndex;
        displayDigimon();
        updateNavigation();
    } else {
        document.getElementById('result').innerHTML = `<p>Digimon não encontrado</p>`;
        digimons = [];
        updateNavigation();
    }
}

export function displayDigimon() {
    const digimon = digimons[currentIndex];
    const resultDiv = document.getElementById('result');

    resultDiv.innerHTML = `
        <h2>${digimon.name}</h2>
        <p>Nível: ${digimon.level}</p>
        <img src="${digimon.img}" alt="${digimon.name}" class="digimon-image">
    `;
}

export function previousDigimon() {
    if (currentIndex > 0) {
        currentIndex--;
        displayDigimon();
        updateNavigation();
    }
}

export function nextDigimon() {
    if (currentIndex < digimons.length - 1) {
        currentIndex++;
        displayDigimon();
        updateNavigation();
    }
}

export function updateNavigation() {
    document.getElementById('prevButton').disabled = currentIndex === 0;
    document.getElementById('nextButton').disabled = currentIndex === digimons.length - 1 || digimons.length <= 1;
}
