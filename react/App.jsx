import React, { useState, useEffect } from 'react';
import { fetchAllDigimons, searchDigimonByName } from './api';
import './style.css';

const App = () => {
    const [digimons, setDigimons] = useState([]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [searchTerm, setSearchTerm] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            const allDigimons = await fetchAllDigimons();
            setDigimons(allDigimons);
        };
        fetchData();
    }, []);

    const displayDigimon = () => {
        const digimon = digimons[currentIndex];
        return digimon ? (
            <div>
                <h2>{digimon.name}</h2>
                <p>Nível: {digimon.level}</p>
                <img src={digimon.img} alt={digimon.name} className="digimon-image" />
            </div>
        ) : (
            <p>Nenhum Digimon disponível.</p>
        );
    };

    const handleSearch = () => {
        const index = searchDigimonByName(digimons, searchTerm);
        if (index !== -1) {
            setCurrentIndex(index);
            setErrorMessage('');
        } else {
            setErrorMessage('Digimon não encontrado. Tente outro nome.');
        }
    };

    const handleNext = () => {
        if (currentIndex < digimons.length - 1) setCurrentIndex(currentIndex + 1);
    };

    const handlePrevious = () => {
        if (currentIndex > 0) setCurrentIndex(currentIndex - 1);
    };

    return (
        <div className="container">
            <h1 className="title">DigimonDex</h1>
            <div className="search-container">
                <input
                    type="text"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    placeholder="Digite o nome do Digimon"
                    onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
                />
                <button onClick={handleSearch}>Pesquisar</button>
            </div>
            <div className="result">
                {errorMessage ? <p>{errorMessage}</p> : displayDigimon()}
            </div>
            <div className="navigation">
                <button onClick={handlePrevious} disabled={currentIndex === 0}>
                    Anterior
                </button>
                <button
                    onClick={handleNext}
                    disabled={currentIndex === digimons.length - 1 || digimons.length <= 1}
                >
                    Próximo
                </button>
            </div>
        </div>
    );
};

export default App;
