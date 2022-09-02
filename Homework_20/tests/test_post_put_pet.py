import pytest
import requests

from Homework_20.configuration import PET
from Homework_20.src.enums.global_enums import GlobalErrorMessages


def test_adding_new_pet(new_pet):
    new_pet = requests.post(PET, json=new_pet)
    assert new_pet.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

@pytest.mark.parametrize('param_name, expected_param_value', [('id', 1239),
                                                              ('name', 'some new animal'),
                                                              ('category', {'id': 9321, 'name': 'animal animal'}),
                                                              ('photoUrls', ['string']),
                                                              ('tags', [{'id': 3219, 'name': 'tag tag'}]),
                                                              ('status', 'pending')
                                                              ])
def test_compare_pet_params_values(param_name, expected_param_value, new_pet, headers):
    new_pet = requests.post(PET, json=new_pet, headers=headers)
    assert new_pet.json()[param_name] == expected_param_value, GlobalErrorMessages.WRONG_PARAM_VALUE

@pytest.mark.parametrize('param_name, expected_param_value', [('id', 1239),
                                                              ('name', 'updated animal'),
                                                              ('category', {'id': 9321, 'name': 'category animal'}),
                                                              ('photoUrls', ['string']),
                                                              ('tags', [{'id': 3219, 'name': 'updated tag'}]),
                                                              ('status', 'sold')
                                                              ])
def test_updating_pet(new_pet, updated_pet, param_name, expected_param_value, headers):
    new_pet = requests.post(PET, json=new_pet, headers=headers)
    assert new_pet.json()['id'] == 1239, GlobalErrorMessages.WRONG_PARAM_VALUE
    updated_pet = requests.put(PET, json=updated_pet)
    assert updated_pet.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert updated_pet.json()[param_name] == expected_param_value, GlobalErrorMessages.WRONG_PARAM_VALUE

