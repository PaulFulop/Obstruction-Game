import sys
sys.path.append("./src")

class ScoreRepo:
    def __init__(self, file_path:str):
        self.__file_path = file_path
        self.__data = []
        self.__load()

    def update_score(self, flag:bool):
        player = 0 if flag == False else 1
        self.__data[player] += 1
        self.__save()
    
    def __save(self):
        try:
            with open(self.__file_path, "wt") as file:
                file.write(f"{self.__data[0]} {self.__data[1]}")
        except FileNotFoundError:
            return

    def __load(self):
        try:
            with open(self.__file_path, "rt") as file:
                score = file.readline()
                tokens = score.split()
                tokens[0] = int(tokens[0].strip())
                tokens[1] = int(tokens[1].strip())
                self.__data.extend(tokens[:2])
        except FileNotFoundError:
            return
    
    @property
    def data(self):
        return self.__data


# score = ScoreRepo("src/repository/score.txt")