# encoding = utf-8
"""
Test script for card type inference refactoring
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ytla_plan'))

from core.classic.cards.sideCard.process.processCards import _infer_card_type
from core.classic.cards.sideCard.process.processCardHandlerFactory import CardHandlerFactory

def test_inference():
    print("=" * 60)
    print("Testing Card Type Inference Refactoring")
    print("=" * 60)
    
    # Test cases matching the original hard-coded mapping
    test_cases = [
        ('alarm', 'timer'),
        ('countdown', 'timer'),
        ('count', 'timer'),
        ('sample1', 'sample'),
        ('sample2', 'sample'),
        ('sample3', 'sample'),
        ('wordle', 'relax'),
        ('unknown_sub_type', 'unknown')
    ]
    
    print("\n[1] Testing _infer_card_type function...")
    all_passed = True
    
    for card_sub_type, expected_type in test_cases:
        result = _infer_card_type(card_sub_type)
        if result == expected_type:
            print(f"  ✓ PASS: _infer_card_type('{card_sub_type}') → '{result}'")
        else:
            print(f"  ✗ FAIL: _infer_card_type('{card_sub_type}') → '{result}', expected '{expected_type}'")
            all_passed = False
    
    print("\n[2] Testing CardHandlerFactory.get_card_type_from_sub_type directly...")
    
    for card_sub_type, expected_type in test_cases:
        result = CardHandlerFactory.get_card_type_from_sub_type(card_sub_type)
        if result == expected_type:
            print(f"  ✓ PASS: get_card_type_from_sub_type('{card_sub_type}') → '{result}'")
        else:
            print(f"  ✗ FAIL: get_card_type_from_sub_type('{card_sub_type}') → '{result}', expected '{expected_type}'")
            all_passed = False
    
    print("\n[3] Checking registered handlers in factory...")
    print(f"  Total registered handlers: {len(CardHandlerFactory._handlers)}")
    for (card_type, sub_type), handler in CardHandlerFactory._handlers.items():
        print(f"  - {card_type}/{sub_type}: {handler.__class__.__name__}")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ All tests passed! Refactoring successful!")
    else:
        print("❌ Some tests failed!")
    print("=" * 60)
    
    return all_passed

if __name__ == "__main__":
    success = test_inference()
    sys.exit(0 if success else 1)
