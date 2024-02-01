import numpy as np
import pandas as pd

# Load the CSV data into a pandas DataFrame
pokemon_data = pd.read_csv('pokemon.csv')

# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(pokemon_data.head())

# Filter the DataFrame to show only 'Grass' type Pokemon
grass_pokemon = pokemon_data[pokemon_data['Type 1'] == 'Grass']



# Display the first 5 rows of Grass type Pokemon
print("\nFirst 5 rows of Grass type Pokemon:")
print(grass_pokemon.head())

# Print all the legendary Pokemon
legendary_pokemon = pokemon_data[pokemon_data['Legendary'] == True]
print("\nLegendary Pokemon:")
print(legendary_pokemon)


# Filter and display only Generation 1 Pokémon
gen1_pokemon = pokemon_data[pokemon_data['Generation'] == 1]
print("\nGeneration 1 Pokemon:")
print(gen1_pokemon)

# Calculate the total number of legendary Pokemon
total_legendaries = legendary_pokemon.shape[0]
print(f"\nTotal number of legendary Pokemon: {total_legendaries}")

# Calculate the average Attack and Defense of Pokemon
attack_array = pokemon_data['Attack'].to_numpy()
defense_array = pokemon_data['Defense'].to_numpy()

average_attack = np.mean(attack_array)
average_defense = np.mean(defense_array)

print(f'Average Attack of every Pokemon: {average_attack:.2f}')
print(f'Average Defense of every Pokemon: {average_defense:.2f}')

# Find the Pokemon with the highest HP
max_hp_pokemon = pokemon_data.loc[pokemon_data['HP'].idxmax()]
print("\nPokemon with the highest HP:", max_hp_pokemon['Name'])
print(max_hp_pokemon)

# Find the Top 5 Pokemon by Total stats
sorted_pokemon = pokemon_data.sort_values(by='Total', ascending=False)
print("\nTop 5 Pokemon by Total stats:")
for index, row in sorted_pokemon.head(5).iterrows():
    # Print the row
    print(row['Name'], row['Total'])

# Display All Pokemon Types
unique_types = pokemon_data['Type 1'].unique()
print("\nPokemon types:")
print(unique_types)

