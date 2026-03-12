# encoding = utf-8
"""
Test script for CardHandlerFactory dynamic loading
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.classic.cards.sideCard.process.processCardHandlerFactory import CardHandlerFactory

def test_factory():
    print("=" * 60)
    print("Testing CardHandlerFactory dynamic loading")
    print("=" * 60)
    
    # Step 1: Test finding handler files
    print("\n[1] Finding card handler files...")
    handler_files = CardHandlerFactory.find_card_handler_files()
    print(f"Found {len(handler_files)} handler files:")
    for f in handler_files:
        print(f"  - {f}")
    
    # Step 2: Load and register handlers
    print("\n[2] Loading and registering handlers...")
    CardHandlerFactory.load_and_register_handlers()
    
    # Step 3: Test getting handlers
    print("\n[3] Testing handler retrieval...")
    test_cases = [
        ('timer', 'alarm'),
        ('timer', 'countdown'), 
        ('timer', 'count'),
        ('sample', 'sample1'),
        ('sample', 'sample2'),
        ('sample', 'sample3'),
        ('relax', 'wordle')
    ]
    
    for card_type, card_sub_type in test_cases:
        try:
            handler = CardHandlerFactory.get_handler(card_type, card_sub_type)
            print(f"  ✓ Success: Got handler for {card_type}/{card_sub_type}: {handler.__class__.__name__}")
        except Exception as e:
            print(f"  ✗ Failed: Could not get handler for {card_type}/{card_sub_type}: {str(e)}")
    
    print("\n" + "=" * 60)
    print("Test complete!")
    print("=" * 60)

if __name__ == "__main__":
    test_factory()
