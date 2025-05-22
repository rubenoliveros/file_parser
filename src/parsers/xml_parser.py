import pandas as pd
from pathlib import Path
from lxml import etree
import logging
from .base_parser import BaseParser

class XmlToCsvParser(BaseParser):
    def convert(self):
        """Convert XML file to CSV format."""
        try:
            source_path = Path(self.origin)
            dest_path = Path(self.destiny)

            tree = etree.parse(source_path)
            root = tree.getroot()

            data = []
            for element in root.iter():
                if element.text and element.text.strip():
                    data.append({
                        'tag': element.tag,
                        'text': element.text.strip(),
                        'parent': element.getparent().tag if element.getparent() is not None else None
                    })

            df = pd.DataFrame(data)
            output_file = dest_path / f"{source_path.stem}.csv"
            df.to_csv(output_file, index=False)

            logging.info(f"Converted {source_path} to {output_file}")
            return True

        except Exception as e:
            logging.error(f"Failed to convert XML file '{self.origin}'. Reason: {str(e)}")
            return False 