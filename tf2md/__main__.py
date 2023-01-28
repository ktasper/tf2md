import click
from tf2md.markdown import create_output_file, create_variables_file
from tf2md.parser import open_file, parse_hcl, get_tf_file_type

@click.group()
@click.version_option("1.0.0")
def main():
    """Terraform to markdown"""


@main.command()
@click.argument("input_file", type=click.Path(), required=True)
def gen_docs(input_file):
    """
    This generates markdown docs for either variables.tf or outputs.tf
    """
    hcl_dict = open_file(input_file)
    file_type = get_tf_file_type(hcl_dict)
    parsed_dict = parse_hcl(hcl_dict, file_type)
    if file_type == "variable":
        create_variables_file(parsed_dict, file_type)
    else:
        create_output_file(parsed_dict, file_type)
