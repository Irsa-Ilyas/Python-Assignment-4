def main():
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    print("🌍 Welcome to the Planet Weight Converter!")
    print("Planets you can choose from:")
    for planet in planet_gravity:
        print(f"➡️ {planet}")
    try:
        earth_weight = float(input("\nEnter your weight on Earth (in kg): "))
        planet = input("Enter a planet name: ").capitalize()
        if planet in planet_gravity:
            planet_weight = round(earth_weight * planet_gravity[planet], 2)
            print(f"🌌 Your weight on {planet} would be: {planet_weight} kg")
        else:
            print("❌ Invalid planet name. Please enter a valid one from the list above.")
    except ValueError:
        print("⚠️ Please enter a valid number for weight.")
if __name__ == "__main__":
    main()
