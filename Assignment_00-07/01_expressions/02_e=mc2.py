def main():
    c= 299792458
    mass_in_kg = float(input("Enter kilos of mass: "))
    print("e = m * C^2...")
    print("m= " +str(mass_in_kg)+" kg")
    print("C = " +str(c) + " m/s")
    energy_in_joules=mass_in_kg* c**2
    print(energy_in_joules)
if __name__ =='__main__':
    main()