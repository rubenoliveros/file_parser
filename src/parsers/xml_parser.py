import pandas as pd
from pathlib import Path
from lxml import etree
from datetime import datetime
import logging
from .base_parser import BaseParser

class XmlToCsvParser(BaseParser):
    def parse(self):
        """Convert XML file to CSV format with name, email, street, city, country headers."""
        try:
            if not Path(self.origin).exists():
                logging.error(f"Source file {self.origin} does not exist")
                return False

            # Create destiny directory if it doesn't exist
            Path(self.destiny).mkdir(parents=True, exist_ok=True)

            # Parse XML file
            tree = etree.parse(self.origin)
            root = tree.getroot()

            # Extract data
            data = []
            for record in root.findall('.//record'):
                record_data = {
                    'name': record.findtext('name', ''),
                    'email': record.findtext('email', ''),
                    'street': record.findtext('address/street', ''),
                    'city': record.findtext('address/city', ''),
                    'country': record.findtext('address/country', '')
                }
                data.append(record_data)

            columns = ['name', 'email', 'street', 'city', 'country']
            df = pd.DataFrame(data, columns=columns)
            output_path = Path(self.destiny) / f"{Path(self.origin).stem}.csv"
            df.to_csv(output_path, index=False)
            logging.info(f"Successfully converted {self.origin} to {output_path}")
            return True

        except Exception as e:
            logging.error(f"Error processing XML file: {str(e)}")
            return False 