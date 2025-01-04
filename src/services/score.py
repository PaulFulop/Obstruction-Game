# Service for the score repository

import sys
sys.path.append("./src")
from repository.score_repo import ScoreRepo

class ScoreService:
    def __init__(self, file_path:str):
        self.__score_repo = ScoreRepo(file_path)
    
    def list_score(self):
        return self.__score_repo.data
    
    def update_score(self, flag):
        self.__score_repo.update_score(flag)