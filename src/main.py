import json
import logging
from config import setup_logging
from parsers import get_parser

def load_job_definition(file_path):
    """Load and parse the job definition file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Job definition file not found at '{file_path}'")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in job definition file. Line {e.lineno}, Column {e.colno}: {str(e)}")

def process_transformations(job_definition):
    """Process all transformations defined in the job definition."""
    success = True
    for transformation in job_definition.get('transformations', []):
        try:
            obj = transformation['object']
            kwargs = transformation.get('kwargs', {})
            parser = get_parser(
                parser_type=obj['parser'],
                origin=obj['origin'],
                destiny=obj['destiny'],
                **kwargs
            )
            
            # Call the appropriate method based on parser type
            if obj['parser'] == 'unzip':
                if not parser.extract():
                    success = False
            elif obj['parser'] == 'xml_to_csv':
                if not parser.convert():
                    success = False
            else:
                success = False
                logging.error(f"Unsupported parser type: {obj['parser']}")
                
        except Exception as e:
            success = False
            logging.error(str(e))
    return success

def main():
    """Main entry point for the application."""
    setup_logging()
    try:
        job_definition = load_job_definition('job_definition.json')
        success = process_transformations(job_definition)
        if not success:
            exit(1)
    except Exception as e:
        logging.error(str(e))
        exit(1)

if __name__ == '__main__':
    main() 