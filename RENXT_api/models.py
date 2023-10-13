from typing import List, Dict
from datetime import datetime

class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class Email:
    def __init__(self, id: str, address: str, constituent_id: str, date_added: str,
                 date_modified: str, do_not_email: bool, inactive: bool, primary: bool, type: str):
        self.id = id
        self.address = address
        self.constituent_id = constituent_id
        self.date_added = datetime.fromisoformat(date_added)
        self.date_modified = datetime.fromisoformat(date_modified)
        self.do_not_email = do_not_email
        self.inactive = inactive
        self.primary = primary
        self.type = type

class Constituent_Search:
    def __init__(self, id: str, address: str, deceased: bool, email: str, fundraiser_status: str, inactive: bool, lookup_id: str, name: str):
        self.id = id
        self.address = address
        self.deceased = deceased
        self.email = email
        self.fundraiser_status = fundraiser_status
        self.inactive = inactive
        self.inactive = inactive
        self.lookup_id = lookup_id
        self.name = name


