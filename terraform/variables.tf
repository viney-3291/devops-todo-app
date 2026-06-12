variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "app_name" {
  description = "Application name"
  default     = "devops-todo-app"
}

variable "db_username" {
  description = "Database username"
  default     = "postgres"
}

variable "db_password" {
  description = "Database password"
  default     = "postgres123"
}

variable "ecr_image_uri" {
  description = "ECR image URI"
  default     = "865749917919.dkr.ecr.us-east-1.amazonaws.com/devops-todo-app:latest"
}