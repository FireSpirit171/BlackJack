class read_singletone:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super(read_singletone, cls).__new__(cls)
            cls._instance.filename = filename
        return cls._instance

    def read_file(self):       
        with open(self.filename, 'r') as stat_file:
            info_numbers = []
            for line in stat_file.readlines():
                info_numbers.append(line.split(": ")[1])
        games, wons, draws, loses, percant = info_numbers
        good_open = True

        #Преобразование типов и печать об удачном/неудачном открытии
        try:
            games = int(games)
            wons = int(wons)
            draws = int(draws)
            loses = int(loses)
            percant = float(percant)
        except:
            good_open = False

        if good_open:
            return games, wons, draws, loses, percant 
        else:
            print("Ошибка!")

    def update_stat(self, result):
        games, wons, draws, loses, percent = self.read_file()
        games += 1  
        if result == 1:
            wons += 1
        elif result == 0:
            draws += 1
        else: 
            loses += 1
        percent = round((wons/games)*100, 2)
        with open (self.filename, 'w') as stat_file:
            stat_file.write(f"Games: {games}\n")
            stat_file.write(f"Wons: {wons}\n")
            stat_file.write(f"Draws: {draws}\n")
            stat_file.write(f"Loses: {loses}\n")
            stat_file.write(f"Percant: {percent}")