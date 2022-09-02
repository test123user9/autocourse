import pytest
import requests

from Homework_20.configuration import AVAILABLE, PENDING, SOLD
from Homework_20.src.enums.global_enums import GlobalErrorMessages


@pytest.mark.parametrize('status, expected_code_result', [(requests.get(AVAILABLE), 200),
                                                          (requests.get(PENDING), 200),
                                                          (requests.get(SOLD), 200)])
def test_get_by_status(status, expected_code_result):
    assert status.status_code == expected_code_result, GlobalErrorMessages.WRONG_STATUS_CODE.value
