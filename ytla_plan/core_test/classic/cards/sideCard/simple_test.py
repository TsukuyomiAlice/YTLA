# encoding = utf-8

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=== Testing CardHandlerFactory ===")

from core.classic.cards.sideCard.process.processCardHandlerFactory import CardHandlerFactory

print("\n1. Finding handler files...")
files = CardHandlerFactory.find_card_handler_files()
print(f"Found {len(files)} files:")
for f in files:
    print(f"  - {f}")

print("\n2. Loading handlers...")
CardHandlerFactory.load_and_register_handlers()

print("\n3. Checking registered handlers:")
for key, handler in CardHandlerFactory._handlers.items():
    print(f"  {key}: {handler.__class__.__name__}")

print("\n=== Test complete! ===")
