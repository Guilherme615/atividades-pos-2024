import './style.css';
import { fetchAllDigimons, searchDigimon, previousDigimon, nextDigimon } from './api.js';

window.onload = () => {
    fetchAllDigimons().then(() => {
        document.getElementById('searchButton').addEventListener('click', () => {
            const digimonName = document.getElementById('digimonName').value.trim();
            searchDigimon(digimonName);
        });

        document.getElementById('prevButton').addEventListener('click', previousDigimon);
        document.getElementById('nextButton').addEventListener('click', nextDigimon);

        document.getElementById('digimonName').addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                const digimonName = document.getElementById('digimonName').value.trim();
                searchDigimon(digimonName);
            }
        });
    });
};
