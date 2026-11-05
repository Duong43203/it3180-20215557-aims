from typing import List
from aims.dvd import DigitalVideoDisc

def search_by_title(items: List[DigitalVideoDisc], keyword: str) -> List[DigitalVideoDisc]:
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
