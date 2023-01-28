
Terraform Module variable
=========================


This is a auto generated file by running `tf2md`.
# Required variable

|Name|Description|Type|Nullable|Required?|
| :---: | :---: | :---: | :---: | :---: |
|`force_destroy`|Destroy the user even if it has non-Terraform-managed IAM access keys, login profile or MFA devices|`bool`|False|True|
|`kms_arn`|The kms arn you wish to use for this module|`string`|False|True|
|`kms_alias_name`|value|`None`|False|True|
|`numOfInstances`|None|`number`|False|True|
|`empty_var`|None|`None`|False|True|
|`can_be_null`|None|`None`|True|True|
|`is_sensative`|None|`None`|False|True|
  

# variable

|Name|Description|Type|Nullable|Default|
| :---: | :---: | :---: | :---: | :---: |
|`project_name`|None|`string`|False|MyGoodProject|
|`ec2_instance_name`|value|`None`|False|${string}|
|`numOfRds`|None|`None`|False|20|
|`test_list`|None|`list[str]`|False|['item1', 'item2', 'item3']|
|`test_map`|None|`map(string)`|False|{'name': 'Karl', 'Foo': 'bar'}|
