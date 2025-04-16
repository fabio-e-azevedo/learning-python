# Defina uma interface (abstração) para o cliente HTTP

from abc import ABC, abstractmethod
from typing import Any

class IClienteHTTP(ABC):
    @abstractmethod
    def get(self, url: str) -> Any:
        pass


# Crie a implementação real com requests

import requests

class ClienteHTTPRequests(IClienteHTTP):
    def get(self, url: str) -> Any:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


# A função que processa os dados recebe o cliente como dependência

from typing import List, Dict

def get_filtered_data(http_client: IClienteHTTP, url: str, fields: List[str]) -> List[Dict[str, Any]]:
    data = http_client.get(url)
    return [{field: item.get(field) for field in fields} for item in data]


# url = "https://jsonplaceholder.typicode.com/users"
# desired_fields = ["id", "email"]
# client = ClienteHTTPRequests()
# result = get_filtered_data(client, url, desired_fields)
# print(result)
# for item in result:
#     print(item)



# Testando com Mock (sem acessar a API real)
# Pode criar uma classe mockada para testes

class ClienteHTTPMock(IClienteHTTP):
    def get(self, url: str):
        return [
            {"id": 1, "email": "a@x.com", "name": "Fulano"},
            {"id": 2, "email": "b@x.com", "name": "Ciclano"},
        ]

client = ClienteHTTPMock()
result = get_filtered_data(client, "http://fake", ["id", "email"])
print(result)
