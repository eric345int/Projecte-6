
import re

def es_email_valid(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def es_telefon_valid(telefon):
    return telefon.isdigit() and len(telefon) in [9, 10]
