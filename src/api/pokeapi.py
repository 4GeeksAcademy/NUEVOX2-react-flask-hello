@app.route('/search_pokemon', methods=['GET'])
@login_required
def search_pokemon():
    name = request.args.get('name')
    response = requests.get(
        f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
    if response.status_code == 200:
        data = response.json()
        # extraer info relevante
        pokemon_data = {
            "name": data['name'],
            "types": [t['type']['name'] for t in data['types']],
            "image": data['sprites']['front_default']
        }
        return render_template('pokemon_detail.html', pokemon=pokemon_data)
    else:
        flash('Pokémon no encontrado', 'danger')
        return redirect(url_for('pokedex'))
