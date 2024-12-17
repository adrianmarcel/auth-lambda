output "lambda_arn" {
  description = "ARN da Lambda Function"
  value       = aws_lambda_function.validate_cpf.arn
}

output "api_gateway_url" {
  description = "URL do API Gateway"
  value       = aws_api_gateway_deployment.api_deployment.invoke_url
}
