from pathlib import Path

class BaseParser:
    def __init__(self, origin, destiny, **kwargs):
        if not origin or not destiny:
            raise ValueError("Error: Both origin and destiny paths must be provided. Got origin='{}' and destiny='{}'".format(origin, destiny))
        
        # Convert S3 paths to local paths
        if origin.startswith('s3://'):
            origin = origin.replace('s3://', 's3_simulation/')
        if destiny.startswith('s3://'):
            destiny = destiny.replace('s3://', 's3_simulation/')
            
        self.origin = origin
        self.destiny = destiny
        self.kwargs = kwargs