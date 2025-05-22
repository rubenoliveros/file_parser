import logging
import os
from pathlib import Path
from parsers import ZipFileParser, XmlToCsvParser

# Environment configuration
MODE = os.getenv('PARSER_MODE', 'online')  # Default to online mode
LOCAL_BASE_PATH = Path('data')  # Base path for local mode

# Configure logging
def setup_logging():
    """Setup basic logging configuration."""
    # Get the absolute path to the project root
    project_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Create logs directory if it doesn't exist
    log_dir = project_root / 'logs'
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    log_file = log_dir / 'file_parser.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),  # Console handler
            logging.FileHandler(str(log_file))  # File handler
        ]
    )
    logging.info("Logging initialized")

def get_path(path: str) -> str:
    """
    Convert path based on current mode.
    In local mode, converts S3 paths to local paths.
    In online mode, keeps S3 paths as is.
    """
    if MODE == 'local':
        if path.startswith('s3://'):
            # Convert s3://bucket/path to local path
            relative_path = path[5:]  # Remove s3://
            return str(LOCAL_BASE_PATH / relative_path)
    return path

# Parser registry
PARSER_REGISTRY = {
    'unzip': 'ZipFileParser',
    'xml_to_csv': 'XmlToCsvParser'
}

def get_parser(parser_type, **kwargs):
    """Get the appropriate parser class based on the parser type."""
    parser_class = PARSER_REGISTRY.get(parser_type)
    if not parser_class:
        raise ValueError(f"Unknown parser type: {parser_type}")
    
    # Convert paths based on mode
    if 'origin' in kwargs:
        kwargs['origin'] = get_path(kwargs['origin'])
    if 'destiny' in kwargs:
        kwargs['destiny'] = get_path(kwargs['destiny'])
    
    return parser_class(**kwargs) 