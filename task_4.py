class Autobus:
    def __init__(self, number, start, end, time):
        self.start = start
        self.end = end
        self.number = number
        self.time = time

    def info(self):
        return f"Route number: {self.number}\nStarting point: {self.start}\nDestination point: {self.end}\nTravel time: {self.time}\n{'-'*20}" 
    
    def set_number(self, value):
        self.number = value

    def get_number(self):
        return self.number

    def set_start(self, value):
        self.start = value

    def get_start(self):
        return self.start
    
    def set_end(self, value):
        self.end = value

    def get_end(self):
        return self.end
    
    def set_time(self, value):
        self.time = value

    def get_time(self):
        return self.time
    
def create_autopark():
    n = int(input('Enter the number of buses: '))
    buses = []
    for i in range(n):
        num = int(input(f'Enter number of {i+1} bus: '))
        start = input(f'Enter the starting point of {i+1} bus: ')
        end = input(f'Enter the destination point of {i+1} bus: ')
        time = input(f'Enter the travel time of {i+1} bus: ')
        print('-'*20)
        buses.append(Autobus(num, start, end, time))

    with open('buses.txt', 'w') as file:
        for i in range(len(buses)):
            file.write(str(buses[i].info()) + '\n')

def read_file(filename: str) -> list:
    with open(filename, 'r') as file:
        buses = []
        lines = file.readlines()
        i = 4
        while i <= len(lines):
            lines.pop(i)
            i+=4

        words = [line.replace('\n', '').split(sep=' ')[-1] for line in lines]

        while len(words) >= 4:
            buses.append(Autobus(int(words[0]), words[1], words[2], words[3]))
            for i in range(4):
                words.pop(0)

        return buses
    
def show_autopark(buses: list) -> None:
    for bus in buses:
        print(bus.info())

def sort_by_number(buses: list) -> None:
    autopark = {}
    for bus in buses:
        autopark.update({bus.get_number():bus})

    new_autopark = {key: value for key, value in sorted(autopark.items(), key=lambda item: item[0], reverse=True)}
    for key in new_autopark.keys():
        print(new_autopark[key].info())

def search_by_point(city:str, buses: list) -> None:
    for bus in buses:
        if bus.get_start() == city or bus.get_end() == city:
            print(bus.info())

create_autopark()
autopark = read_file('buses.txt')
show_autopark(autopark)
sort_by_number(autopark)
search_by_point('Pinsk', autopark)