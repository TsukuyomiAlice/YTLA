from abc import ABC, abstractmethod


class CardHandler(ABC):
    @abstractmethod
    def handle(self, data: dict, mode: str, card_id: int = 0) -> bool:
        """To add or update a card"""
        pass

    @abstractmethod
    def parse_detail(self, detail: dict) -> dict:
        """To parse card detail data according to the card subtype"""
        pass

    @abstractmethod
    def soft_update(self, card_id: int, action: str) -> dict:
        """To soft update a card according to the card subtype and the action"""
        pass

    @staticmethod
    def get_default_name(self) -> str:
        """To get default card name"""
        return "defaultCard"
