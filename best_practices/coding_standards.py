```python
# Importing required libraries
import pep8
from flake8.api import legacy as flake8

def followCodingStandards(file_path):
    """
    Function to check if the code follows PEP8 coding standards
    """
    # Create a StyleGuide instance
    pep8style = pep8.StyleGuide()

    # Run the check on the file
    result = pep8style.check_files([file_path])

    # Print the result
    print(result.total_errors, "PEP8 errors/warnings found")

def checkComplexity(file_path):
    """
    Function to check the complexity of the code
    """
    # Create a Flake8 instance
    flake8_style_guide = flake8.get_style_guide(ignore=['E501'])

    # Run the check on the file
    report = flake8_style_guide.check_files([file_path])

    # Print the result
    print(report.total_errors, "Flake8 errors/warnings found")

# Example usage
followCodingStandards('backend/openai_integration.py')
checkComplexity('backend/openai_integration.py')
```
This Python script checks if the code in the specified file follows PEP8 coding standards and checks the complexity of the code using Flake8. The functions `followCodingStandards` and `checkComplexity` take a file path as an argument and print the number of PEP8 and Flake8 errors/warnings found in the file respectively.