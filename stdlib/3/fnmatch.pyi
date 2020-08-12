# Stubs for fnmatch

# Based on http://docs.python.org/3.2/library/fnmatch.html and
# python-lib/fnmatch.py

from typing import AnyStr, Iterable, List

def fnmatch(name: AnyStr, pat: AnyStr) -> bool: ...
def fnmatchcase(name: AnyStr, pat: AnyStr) -> bool: ...
def filter(names: Iterable[AnyStr], pat: AnyStr) -> List[AnyStr]: ...
def translate(pat: str) -> str: ...
