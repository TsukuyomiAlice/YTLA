from features.timer.process.processCardsTimer import TimerCardHandler
from features.relax.process.processCardsRelax import RelaxCardHandler
from features.sample.process.processCardsSample import SampleCardHandler


class CardHandlerFactory:

    @classmethod
    def register_handler(cls, card_type, card_sub_type, handler):
        """register new card handler"""
        cls._handlers[(card_type, card_sub_type)] = handler

    @classmethod
    def get_handler(cls, card_type, card_sub_type):
        """get card handler"""
        handler = cls._handlers.get((card_type, card_sub_type))
        if not handler:
            raise ValueError(f"Unregistered card type: {card_type}/{card_sub_type}")
        return handler

    _handlers = {
        ('timer', 'alarm'): TimerCardHandler('alarm'),
        ('timer', 'countdown'): TimerCardHandler('countdown'),
        ('timer', 'count'): TimerCardHandler('count'),
        ('sample', 'sample1'): SampleCardHandler('sample1'),
        ('sample', 'sample2'): SampleCardHandler('sample2'),
        ('sample', 'sample3'): SampleCardHandler('sample3'),
        ('relax', 'wordle'): RelaxCardHandler('wordle')
    }
