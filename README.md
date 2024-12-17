# Lambda Function: Validação de CPF

Esta aplicação implementa uma função Lambda em Python para validar CPFs. O objetivo é verificar se um CPF fornecido é válido conforme as regras brasileiras antes de prosseguir com um fluxo de negócios.

## 🚀 Funcionalidades

- Validação de formato do CPF (11 dígitos numéricos).
- Rejeita CPFs com todos os dígitos iguais (ex.: `11111111111`).
- Validação dos dígitos verificadores do CPF.

## 📂 Estrutura do Projeto

```
.
├── src
│   ├── lambda_function.py  # Função principal da Lambda
│   ├── utils.py            # Funções auxiliares, como a validação de CPF
│   └── __init__.py         # Indica que src é um módulo Python
├── tests
│   ├── test_lambda.py      # Testes unitários
│   └── __init__.py         # Indica que tests é um módulo Python
├── terraform
│   ├── main.tf             # Definição dos recursos AWS (Lambda, API Gateway)
│   ├── variables.tf        # Variáveis Terraform
│   ├── outputs.tf          # Saídas Terraform
│   └── terraform.tfvars    # Valores das variáveis (opcional)
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── function.zip            # Código compactado para deploy (gerado automaticamente)
```

## 🛠️ Requisitos

- Python 3.9+
- AWS CLI configurado
- Terraform 1.5+
- Dependências do Python (instaláveis via `requirements.txt`)

## 🚀 Deploy

### Pré-requisitos

1. Configure o AWS CLI com as credenciais e região apropriadas:
   ```bash
   aws configure
   ```

2. Instale as dependências do Python:
   ```bash
   pip install -r requirements.txt
   ```

3. Gere o pacote `function.zip`:
   ```bash
   zip -r function.zip src
   ```

### Deploy com Terraform

1. Inicialize o Terraform no diretório `terraform`:
   ```bash
   terraform init
   ```

2. Aplique a infraestrutura:
   ```bash
   terraform apply
   ```

3. Após a execução, o Terraform fornecerá a URL do endpoint da API Gateway.

## 📦 Exemplos de Uso

### Requisição

**Endpoint:** `POST /validate`  
**Body:**
```json
{
  "cpf": "12345678909"
}
```

### Respostas

**CPF Válido:**
```json
{
  "message": "CPF válido.",
  "cpf": "12345678909"
}
```

**CPF Inválido:**
```json
{
  "message": "CPF inválido. Deve conter 11 dígitos válidos."
}
```

## ✅ Testes

Para rodar os testes, execute:
```bash
pytest
```

Os testes incluem:
- Validação de CPFs corretos e incorretos.
- Cenários de erro, como entrada inválida.

## 📖 Referências

- [Formato do CPF - Receita Federal](https://www.gov.br/receitafederal)
- [Documentação AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)