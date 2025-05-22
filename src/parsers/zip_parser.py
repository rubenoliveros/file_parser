import zipfile
from pathlib import Path
import logging
from .base_parser import BaseParser

class ZipFileParser(BaseParser):
    def extract(self):
        """Extract contents of a ZIP file to the destination directory."""
        try:
            source_path = Path(self.origin)
            dest_path = Path(self.destiny)

            if not source_path.exists():
                logging.error(f"File not found: {source_path}")
                return False

            dest_path.mkdir(parents=True, exist_ok=True)

            with zipfile.ZipFile(source_path, 'r') as zip_ref:
                zip_ref.extractall(dest_path)
            
            logging.info(f"Extracted {source_path} to {dest_path}")
            return True

        except Exception as e:
            logging.error(f"Failed to extract ZIP file '{self.origin}'. Reason: {str(e)}")
            return False 