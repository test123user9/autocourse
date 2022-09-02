import pytest
import requests

from Homework_20.configuration import PET


@pytest.fixture(scope="session")
def new_pet():
    pet_dict = {
        "id": 1239,
        "name": "some new animal",
        "category": {
            "id": 9321,
            "name": "animal animal"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 3219,
                "name": "tag tag"
            }
          ],
        "status": "pending"
        }
    print('pet created')
    yield pet_dict
    requests.delete(f'{PET}/1239')
    print('pet deleted')

@pytest.fixture(scope="session")
def updated_pet():
    updated_pet_dict = {
        "id": 1239,
        "name": "updated animal",
        "category": {
            "id": 9321,
            "name": "category animal"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 3219,
                "name": "updated tag"
            }
          ],
        "status": "sold"
        }
    print('pet updated')
    return updated_pet_dict






