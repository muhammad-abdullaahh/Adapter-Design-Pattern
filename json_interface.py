from abc import ABC, abstractmethod

class JsonData(ABC):

    @abstractmethod
    def get_json_data(self):
        pass