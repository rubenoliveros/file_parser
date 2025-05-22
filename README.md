# File Parser

A Python application that processes files based on job definitions. It supports multiple file transformations including:
- Extracting ZIP files
- Converting XML files to CSV format

[![Python](https://img.shields.io/badge/Python-100%25-blue)](https://github.com/rubenoliveros/file_parser)

> **Note**: This project simulates S3 paths locally. Any path starting with `s3://` will be automatically converted to a local path by replacing `s3://` with `s3_simulation/`. For example, `s3://alejo-parsers/file.zip` becomes `s3_simulation/alejo-parsers/file.zip`.

> **Note**: The job definition file path is hardcoded as `job_definition.json` in `main.py`. Make sure to place your job definition file in the project root directory.

## Project Structure

```
.
├── src/
│   ├── parsers/
│   │   ├── base_parser.py      # Base parser class
│   │   ├── zip_parser.py       # ZIP file extraction
│   │   └── xml_parser.py       # XML to CSV conversion
│   ├── config.py               # Configuration and logging setup
│   └── main.py                 # Main application entry point
├── logs/                       # Log files directory
│   └── file_parser.log         # Application logs
├── s3_simulation/              # Local directory for S3 path simulation
└── job_definition.json         # Job configuration file
```

## Requirements

- Python 3.x
- Required packages:
  - pandas
  - lxml

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rubenoliveros/file_parser.git
cd file_parser
```

2. Install dependencies:
```bash
pip install pandas lxml
```

## Usage

1. Create a job definition file (`job_definition.json`) with your transformations:
```json
{
    "transformations": [
        {
            "object": {
                "parser": "unzip",
                "origin": "s3://alejo-parsers/workspace1/sources/rutafuente1/miarchivo1.zip",
                "destiny": "s3://alejo-parsers/workspace1/sources/rutafuente2/",
                "classname": "ZipFileParser"
            },
            "kwargs": {
                "scripts_path": "scripts/",
                "scripts_bucket": "alejo-scripts"
            }
        },
        {
            "object": {
                "parser": "xml_to_csv",
                "origin": "s3://alejo-parsers/workspace1/sources/rutafuente1/miarchivo2.xml",
                "destiny": "s3://alejo-parsers/workspace1/sources/rutafuente2/",
                "classname": "XmlToCsvParser"
            },
            "kwargs": {
                "scripts_path": "scripts/",
                "scripts_bucket": "alejo-scripts"
            }
        }
    ]
}
```

2. Place your input files in the corresponding local directories under `s3_simulation/`. For example:
   - `s3_simulation/alejo-parsers/workspace1/sources/rutafuente1/miarchivo1.zip`
   - `s3_simulation/alejo-parsers/workspace1/sources/rutafuente1/miarchivo2.xml`

3. Run the application:
```bash
python3 src/main.py
```

## Supported Parsers

1. **ZIP Parser** (`unzip`)
   - Extracts contents of a ZIP file to a destination directory
   - Example: `"parser": "unzip"`

2. **XML to CSV Parser** (`xml_to_csv`)
   - Converts XML files to CSV format
   - Extracts tag names, text content, and parent tags
   - Example: `"parser": "xml_to_csv"`

## Logging

The application logs all operations to:
- Console output
- `logs/file_parser.log`

Log entries include:
- Timestamp
- Log level (INFO/ERROR)
- Operation details

## Error Handling

The application handles various error cases:
- Missing job definition file
- Invalid JSON format
- Unsupported parser types
- File not found errors
- Processing errors

All errors are logged with detailed messages for debugging.

## Contributing

Feel free to submit issues and enhancement requests! 