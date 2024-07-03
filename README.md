# Footer Generator

This script reads data from a CSV file ('data.txt') containing information about users and generates personalized footer HTML files based on a template.

## Installation

1. **Clone the repository:**
```bath
git clone https://github.com/manyinc/csv-signatures-generator.git
cd csv-signatures-generator
```

2. **Ensure Python 3.x is installed:**

This script requires Python 3.x. If not installed, download it from [python.org](https://www.python.org/downloads/).

3. **Install dependencies:**

This script uses standard Python libraries (`csv`, `os`). If you don't have them, install using pip:
```bath
pip install csv
```

## Usage

1. **Prepare your data:**

Place your CSV file (`data.txt`) in the root directory of the repository. The CSV should have the following structure:

  fullname;num;mail;name;surname;position
  John Doe;12345;johndoe@example.com;John;Doe;Developer

Each row represents a user with columns 
```bath
'fullname'; 'num'; 'mail'; 'name'; 'surname'; 'position'
```

2. **Run the script:**

Execute the script using Python:

```bath
python main.py
```

3. **Generated files:**

The script will generate HTML files in the `footer` directory. Each file is named based on the user's first initial, last name, and email address.

## Example

Assume `data.txt` contains:
```bath
fullname;num;mail;name;surname;position
John Doe;12345;johndoe@example.com;John;Doe;Developer
```

Running the script will generate a file named `footer/jdoe_example_com (johndoe@example.com).htm` with personalized information filled into the HTML template.

## Notes

- Make sure `template/footer_template.html` exists and contains placeholders `{uname}`, `{num}`, `{mail}`, and `{pos}` for user information.
- Check permissions to write files in the current directory.
- Review generated HTML files to ensure correctness.
