import os
import sys
import pytest
from unittest.mock import MagicMock, call
from mdutils.mdutils import MdUtils

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tf2md.markdown import create_output_file, tf_var_type_cleaner, create_variables_file


def test_create_output_file():
    outputs = [{"name": "output1", "description": "This is output1"},
               {"name": "output2", "description": "This is output2"}]
    output_file = "Outputs"
    create_output_file(outputs, output_file)

    # Check if the markdown file was created
    assert os.path.exists(f"{output_file}.md")

    # Clean up
    os.remove(f"{output_file}.md")


def test_tf_var_type_cleaner():
    # Test a string with all characters to be removed
    input_string = "${string}"
    expected_output = "string"
    assert tf_var_type_cleaner(input_string) == expected_output

    # Test a string with no characters to be removed
    input_string = "string"
    expected_output = "string"
    assert tf_var_type_cleaner(input_string) == expected_output

    # Test an empty string
    input_string = ""
    expected_output = ""
    assert tf_var_type_cleaner(input_string) == expected_output

    # Test a string with multiple instances of characters to be removed
    input_string = "${string} with ${extra} characters"
    expected_output = "string with extra characters"
    assert tf_var_type_cleaner(input_string) == expected_output
