export async function fetchAllDigimons() {
    try {
        const response = await fetch(`https://digimon-api.vercel.app/api/digimon`);
        if (!response.ok) throw new Error('Erro ao buscar Digimons');
        return await response.json();
    } catch (error) {
        console.error(error.message);
        return [];
    }
}

export function searchDigimonByName(digimons, digimonName) {
    return digimons.findIndex((d) => d.name.toLowerCase() === digimonName.toLowerCase());
}
