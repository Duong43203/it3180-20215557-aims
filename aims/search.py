from typing import List
from aims.dvd import DigitalVideoDisc

def search_by_category(items: List[DigitalVideoDisc], category: str) -> List[DigitalVideoDisc]:
    return [dvd for dvd in items if category.lower() in dvd.category.lower()]

def search_by_title(items: List[DigitalVideoDisc], keyword: str) -> List[DigitalVideoDisc]:
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
