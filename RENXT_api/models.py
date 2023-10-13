from typing import List, Dict
from datetime import datetime
from dateutil import parser

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
        self.date_added = parser.parse(date_added)
        self.date_modified = parser.parse(date_modified)
        self.do_not_email = do_not_email
        self.inactive = inactive
        self.primary = primary
        self.type = type

class ConstituentSearch:
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

class AddressList:
    def __init__(self, id: int, address_lines: str, city: str, constituent_id: int, country: str, county: str, date_added: str, date_modified: str, do_not_mail: bool, formatted_address: str, inactive: bool, postal_code: str, preferred: bool, state: str, type: str, lot: str, cart: str, dpc: int, **kwargs) -> None:
        self.id = id
        self.address_lines = address_lines
        self.city = city
        self.constituent_id = constituent_id
        self.country = country
        self.county = county
        self.date_added = date_added
        self.date_modified = date_modified
        self.do_not_mail = do_not_mail
        self.formatted_address = formatted_address
        self.inactive = inactive
        self.postal_code = postal_code
        self.preferred = preferred
        self.state = state
        self.type = type
        self.lot = lot
        self.cart = cart
        self.dpc = dpc
        self.__dict__.update(kwargs)