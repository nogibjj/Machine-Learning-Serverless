import pytest
import json
import requests


# write a test
def test_invoke():
    r = requests.post(
        "https://tad45q3z45.execute-api.us-east-1.amazonaws.com/PROD/ml-serverless-resources",
        data=json.dumps(
            {
                "data": "13.49,22.3,86.91,561.0,0.08752,0.07697999999999999,0.047510000000000004,0.033839999999999995,0.1809,0.057179999999999995,0.2338,1.3530000000000002,1.735,20.2,0.004455,0.013819999999999999,0.02095,0.01184,0.01641,0.001956,15.15,31.82,99.0,698.8,0.1162,0.1711,0.2282,0.1282,0.2871,0.06917000000000001"
            }
        ),
    )
    assert len(r.content) < 10


def test_incorrect_invoke():
    r = requests.post(
        "https://tad45q3z45.execute-api.us-east-1.amazonaws.com/PROD/ml-serverless-resources",
        data=json.dumps({"data": "bad input data"}),
    )

    assert len(r.content) > 10


def test_incorrect_key():
    r = requests.post(
        "https://tad45q3z45.execute-api.us-east-1.amazonaws.com/PROD/ml-serverless-resources",
        data=json.dumps(
            {
                "incorrect_key": "13.49,22.3,86.91,561.0,0.08752,0.07697999999999999,0.047510000000000004,0.033839999999999995,0.1809,0.057179999999999995,0.2338,1.3530000000000002,1.735,20.2,0.004455,0.013819999999999999,0.02095,0.01184,0.01641,0.001956,15.15,31.82,99.0,698.8,0.1162,0.1711,0.2282,0.1282,0.2871,0.06917000000000001"
            }
        ),
    )
    assert len(r.content) > 10


def test_incorrect_endpoint():
    r = requests.post(
        "https://tad45q3z45.execute-api.us-east-1.amazonaws.com/PROD/",
        data=json.dumps(
            {
                "data": "13.49,22.3,86.91,561.0,0.08752,0.07697999999999999,0.047510000000000004,0.033839999999999995,0.1809,0.057179999999999995,0.2338,1.3530000000000002,1.735,20.2,0.004455,0.013819999999999999,0.02095,0.01184,0.01641,0.001956,15.15,31.82,99.0,698.8,0.1162,0.1711,0.2282,0.1282,0.2871,0.06917000000000001"
            }
        ),
    )
    assert len(r.content) > 10
