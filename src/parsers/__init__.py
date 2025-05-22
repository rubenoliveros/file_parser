"""
Parser implementations for different file types.
"""

from .base_parser import BaseParser
from .zip_parser import ZipFileParser
from .xml_parser import XmlToCsvParser

def get_parser(parser_type, origin, destiny, **kwargs):
    if parser_type == 'unzip':
        return ZipFileParser(origin, destiny)
    elif parser_type == 'xml_to_csv':
        return XmlToCsvParser(origin, destiny)
    else:
        raise ValueError(f"Unsupported parser type: {parser_type}")

__all__ = ['BaseParser', 'ZipFileParser', 'XmlToCsvParser', 'get_parser'] 