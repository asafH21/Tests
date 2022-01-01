import requests
import pytest

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=ec902fcf704d3d56691d9c63c2aafa15'
MOCKS = dict({"CUR1": 5, "CUR2": 8, "CUR3": 12, "CUR4": 16, "CUR5": 16})


def isDevOrProd(mock=None):
    result = []
    if mock is None:
        jasonResponse = requests.get(url).json()
        dict = jasonResponse['rates']
        for d in dict:
            if dict[d] < 10:
                result.append(d)

    else:
        dict = mock
        for d in dict:
            if dict[d] < 10:
                result.append(d)
    return result


