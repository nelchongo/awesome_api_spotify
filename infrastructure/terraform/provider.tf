provider "aws" {
  profile = "default"
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket = "fs-infrastructure-bucket"
    key    = "awesome_api_spotify/state"
    region = "us-east-1"
  }
}