import json
import src.lambda_function as lambda_function

def test_validate_cpf():
    assert lambda_function.validate_cpf("12345678909")
    assert lambda_function.validate_cpf("11144477735")

    assert not lambda_function.validate_cpf("12345678900")
    assert not lambda_function.validate_cpf("11111111111")
    assert not lambda_function.validate_cpf("abc12345678")
    assert not lambda_function.validate_cpf("123")

def test_lambda_handler_valid_cpf():
    event = {"body": json.dumps({"cpf": "12345678909"})}
    response = lambda_function.lambda_handler(event, None)

    assert response["statusCode"] == 200
    assert json.loads(response["body"])["message"] == "CPF válido."

def test_lambda_handler_invalid_cpf():
    event = {"body": json.dumps({"cpf": "123"})}
    response = lambda_function.lambda_handler(event, None)

    assert response["statusCode"] == 400
    assert json.loads(response["body"])["message"] == "CPF inválido. Deve conter 11 dígitos válidos."
