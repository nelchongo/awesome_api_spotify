resource "aws_secretsmanager_secret" "client_credentials" {
  count = 1
  name  = "dev/awesome_api_spotify/client_credentials"
}

resource "aws_secretsmanager_secret" "client_token" {
  count = 1
  name  = "dev/awesome_api_spotify/client_token"
}