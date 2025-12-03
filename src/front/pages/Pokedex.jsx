import { useEffect, useState } from "react";
/*import axios from "axios";*/
import PokemonCard from "../components/PokemonCard";

export default function Pokedex() {
    const [pokemons, setPokemons] = useState([]);

    useEffect(() => {
        axios.get("https://pokeapi.co/api/v2/pokemon?limit=50")
            .then(async res => {
                const results = await Promise.all(
                    res.data.results.map(async p => {
                        const info = await axios.get(p.url);
                        return {
                            name: p.name,
                            image: info.data.sprites.front_default
                        };
                    })
                );
                setPokemons(results);
            });
    }, []);

    return (
        <div className="container mt-4 d-flex flex-wrap">
            {pokemons.map((pkm, i) => <PokemonCard key={i} pokemon={pkm} />)}
        </div>
    );
}
