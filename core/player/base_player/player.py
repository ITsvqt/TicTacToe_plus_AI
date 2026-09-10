from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.board import Board

class Player(ABC):
    
    def __init__(self, name: str, sign: str):
        self._ensure_valid_name(name)
        self._ensure_valid_sign(sign)
        
        self._name = name
        self._sign = sign

    @property
    def name(self):
        return self._name

    @property
    def sign(self):
        return self._sign


    @abstractmethod
    def get_move(self, board: Board) -> tuple[int, int]:
        """
            Returns
                tuple of board cordinates, after normalizing them from 1 based indexes in the user format, to the underlying 0 based index matrix
                    tuple[0] maps to the second dimension of the board's matrix
                    tuple[1] maps to the first dimension of the board's matrix
        """
        
        ...
    
    
    @staticmethod
    def _ensure_valid_name(name:str):
        if not 3 <= len(name) <= 28:
            raise ValueError(f"Illegal name length: [3:28]: {name} ({len(name)})")
        
    @staticmethod
    def _ensure_valid_sign(sign:str):
        if sign == ' ':
            raise ValueError("Invalid player sign: \' \' is the only invalid sign.")
    