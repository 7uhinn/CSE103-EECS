class House:
    def displayHouse(self):
        print("Property Name: ", self.area)
        print("Property Type: ", 'House')
        print("Property Lease: ", self.lease, "\n")


class Apartment:
    def displayApartment(self):
        print("Property Name: ", self.area)
        print("Property Type: ", 'Apartment')
        print("Property Lease: ", self.lease, "\n")


class Purchase(House, Apartment):
    def __init__(self, area):
        self.area = area
        self.lease = 'Purchase'


class Rent(House, Apartment):
    def __init__(self, area):
        self.area = area
        self.lease = 'Rent'


rh = []
ra = []
ph = []
pa = []

print("\nProperty Application")
print("----------------------------------------------")

f1 = f2 = 1

while(f1):
    print("\n0: Enlist a new property listing")
    print("1: Print all property listings")
    print("Any other key: Exit")

    i = int(input('\nEnter your choice: '))

    if(i == 0):
        print("\nEnlist a new property listing")
        print("----------------------------------------------")

        while(f2):
            print("\n0: Apartment")
            print("1: House")
            print("Any other key: Exit to main menu")

            j = int(input('\nEnter your choice: '))

            if(j == 0):
                print("\n0: For Rent")
                print("1: For Purchase")

                k = int(input('\nEnter your choice: '))

                if(k == 0):
                    name = input('\nEnter the name of the property: ')

                    ra.append(Rent(name))

                    print('\nProperty listing added successfully!\n')
                    print("----------------------------------------------")

                elif(k == 1):
                    name = input('\nEnter the name of the property: ')

                    pa.append(Purchase(name))

                    print('\nProperty listing added successfully!\n')
                    print("----------------------------------------------")

            elif(j == 1):
                print("\n0: For Rent")
                print("1: For Purchase")

                k = int(input('\nEnter your choice: '))

                if(k == 0):
                    name = input('\nEnter the name of the property: ')

                    rh.append(Rent(name))

                    print('\nProperty listing added successfully!\n')
                    print("----------------------------------------------")

                elif(k == 1):
                    name = input('\nEnter the name of the property: ')

                    ph.append(Purchase(name))

                    print('\nProperty listing added successfully!\n')
                    print("----------------------------------------------")

            else:
                break

    elif(i==1):
        print("\nAll Properties")
        print("----------------------------------------------")

        print('\nRented Apartments')
        print('-----------------')

        for raidx in range(len(ra)):
            ra[raidx].displayApartment()

        print('\nRented Houses')
        print('-------------')

        for rhidx in range(len(rh)):
            rh[rhidx].displayHouse()

        print('\nPurchase Apartments')
        print('-------------------')

        for paidx in range(len(pa)):
            pa[paidx].displayApartment()

        print('\nPurchase Houses')
        print('---------------')

        for phidx in range(len(ph)):
            ph[phidx].displayHouse()

        print("----------------------------------------------")
    
    else:
        print("----------------------------------------------")
        print("THANK YOU")
        print("----------------------------------------------")
        break

                
