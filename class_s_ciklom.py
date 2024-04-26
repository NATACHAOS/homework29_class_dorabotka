class House:

    def __init__(self):
        self.numberOfFloors = 10

    def schet(self):
        print('Текущий этаж равен: ')
        for a in range(0, 10):
            print(a + 1)


my_house = House()

my_house.schet()
