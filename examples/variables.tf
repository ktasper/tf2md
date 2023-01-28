variable "force_destroy" {
  type        = bool
  description = "Destroy the user even if it has non-Terraform-managed IAM access keys, login profile or MFA devices"
  default     = false
}
variable "kms_arn" {
  type = string
  description = "The kms arn you wish to use for this module"
}

variable "project_name" {
  type = string
  default = "MyGoodProject"
}

variable "ec2_instance_name" {
  description = "value"
  default = string
}

variable "kms_alias_name" {
  description = "value"
}

variable "numOfInstances" {
  type = number
}

variable "numOfRds" {
  default = 20
}

variable "test_list" {
  type = list[str]
  default = ["item1", "item2", "item3"]
  
}

variable "test_map" {
  type = map(string)
  default = {
    "name" = "Karl",
    "Foo" = "bar"
  }
  
}

variable "empty_var" {
  
}

variable "can_be_null" {
  nullable = true
}

variable "is_sensative" {
  sensitive = true
}