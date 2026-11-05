from typing import List
from aims.dvd import DigitalVideoDisc

def search_by_title(items: List[DigitalVideoDisc], keyword: str) -> List[DigitalVideoDisc]:
    # Bản ban đầu phân biệt hoa thường (sẽ hotfix ở Lab 05)
    return [dvd for dvd in items if keyword in dvd.title]
