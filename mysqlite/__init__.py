"""
__init__.py
- 해당 디렉터리를 패키지로 인식하게 하는 파일
- 패키지 import 시 초기화를 담당하는 역할
"""
from .database import *
__all__ = ['Database']