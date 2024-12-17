import json
from src.utils import validate_cpf

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        cpf = body.get("cpf")

        if not cpf or not validate_cpf(cpf):
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "CPF inválido. Deve conter 11 dígitos válidos."}),
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "CPF válido.", "cpf": cpf}),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Erro interno.", "error": str(e)}),
        }
