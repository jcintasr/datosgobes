import pandas as pd
import numpy as np
import requests


class OpenDataset:
    def __init__(self, url):
        self.url = url
        self.id = url.split('/')[-1]
        self.metadata = {}
    
        
    def _extract_from_meta(self, meta: dict) -> None:
        self.metadata["id"] = meta["id"]
        self.metadata["about"] = meta["_about"]
        self.metadata["description"] = meta["description"]
        self.metadata["identifier"] = meta["identifier"]
        self.metadata["issued"] = meta["issued"]
        self.metadata["keyword"] = meta["keyword"]
        self.metadata["language"] = meta["language"]
        self.metadata["modified"] = meta["modified"]
        self.metadata["publisher"] = meta["publisher"]
        self.metadata["theme"] = meta["theme"]
        self.metadata["title"] = meta["title"]
        self.metadata["type"] = meta["type"]

        
