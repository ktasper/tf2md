output "user_name" {
  value       = local.username
  description = "Normalized IAM user name"
}

output "user_arn" {
  value       = join("", aws_iam_user.default.*.arn)
  description = "The ARN assigned by AWS for this user"
}

output "user_unique_id" {
  value       = join("", aws_iam_user.default.*.unique_id)
  description = "The unique ID assigned by AWS"
}

output "super_secret_password" {
  value       = join("", aws_iam_user.default.*.unique_id)
  description = "The super secret password"
  sensitive = true
}