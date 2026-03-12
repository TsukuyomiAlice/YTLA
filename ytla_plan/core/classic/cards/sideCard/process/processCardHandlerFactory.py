import os
import importlib
import inspect
from ytla_plan import config
from core.classic.cards.sideCard.process.processCardHandler import CardHandler

base_dir = config.BACKEND_FOLDER


class CardHandlerFactory:

    @classmethod
    def register_handler(cls, card_type, card_sub_type, handler):
        """register new card handler"""
        cls._handlers[(card_type, card_sub_type)] = handler

    @classmethod
    def get_handler(cls, card_type, card_sub_type):
        """get card handler"""
        if not cls._handlers:
            cls.load_and_register_handlers()
        handler = cls._handlers.get((card_type, card_sub_type))
        if not handler:
            raise ValueError(f"Unregistered card type: {card_type}/{card_sub_type}")
        return handler

    @classmethod
    def scan_card_handler_files(cls, scan_target_dir: str, handler_files: list[str]) -> list[str]:
        """
        Scan a directory for card handler files
        :param scan_target_dir: Target directory
        :param handler_files: List to collect handler files
        :return handler_files: Updated list of handler files
        """
        for root, dirs, files in os.walk(scan_target_dir):
            if 'process' in dirs:
                process_dir = os.path.join(root, 'process')
                for file in os.listdir(process_dir):
                    if file.startswith('process') and file.endswith('.py'):
                        handler_files.append(os.path.join(process_dir, file))
        return handler_files

    @classmethod
    def find_card_handler_files(cls):
        """
        Recursively scan features directory to find card handler files
        :return handler_files: List of found handler files
        """
        handler_files = []
        features_dir = os.path.join(base_dir, 'features')
        if os.path.exists(features_dir):
            handler_files = cls.scan_card_handler_files(features_dir, handler_files)
        return handler_files

    @classmethod
    def build_import_path(cls, file_path) -> str:
        """
        Build import path based on file path
        :param file_path: The file path to convert
        :return import_path: The import path
        """
        relative_path = os.path.relpath(file_path, base_dir)
        import_path = relative_path.replace(os.path.sep, '.').replace('.py', '')
        return str(import_path)

    @classmethod
    def find_card_handlers_in_module(cls, module):
        """
        Find CardHandler subclasses in the module
        :param module: The module to search
        :return handlers: List of found CardHandler subclasses
        """
        handlers = []
        for name, obj in module.__dict__.items():
            if inspect.isclass(obj) and issubclass(obj, CardHandler) and obj is not CardHandler:
                handlers.append(obj)
        return handlers

    @classmethod
    def load_and_register_handlers(cls):
        """
        Dynamically load and register all card handlers
        """
        handler_files = cls.find_card_handler_files()
        registered_count = 0

        for handler_file in handler_files:
            try:
                import_path = cls.build_import_path(handler_file)
                module = importlib.import_module(import_path)
                handler_classes = cls.find_card_handlers_in_module(module)
                
                for handler_class in handler_classes:
                    handler_name = handler_class.__name__
                    
                    if hasattr(handler_class, 'card_type') and hasattr(handler_class, 'card_sub_type'):
                        cls._handlers[(handler_class.card_type, handler_class.card_sub_type)] = handler_class()
                        registered_count += 1
                        print(f"Registered handler: {handler_name} for {handler_class.card_type}/{handler_class.card_sub_type}")
                    else:
                        print(f"Handler {handler_name} found but missing card_type or card_sub_type class attributes")
                        
            except Exception as e:
                print(f"Error loading handlers from {handler_file}: {str(e)}")
        
        print(f"Total registered card handlers: {registered_count}")

    _handlers = {}
    _sub_type_to_type_mapping = {}

    @classmethod
    def get_card_type_from_sub_type(cls, card_sub_type):
        """
        Get card_type from card_sub_type
        :param card_sub_type: The card sub type
        :return: The corresponding card type, or 'unknown' if not found
        """
        if not cls._handlers:
            cls.load_and_register_handlers()
        
        if not cls._sub_type_to_type_mapping:
            cls._sub_type_to_type_mapping = {}
            for (card_type, sub_type), _ in cls._handlers.items():
                cls._sub_type_to_type_mapping[sub_type] = card_type
        
        return cls._sub_type_to_type_mapping.get(card_sub_type, 'unknown')
