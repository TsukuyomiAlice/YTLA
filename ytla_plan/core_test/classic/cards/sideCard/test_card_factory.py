# Test script for CardHandlerFactory
from core.classic.cards.sideCard.process.processCardHandlerFactory import CardHandlerFactory

print("Testing CardHandlerFactory...")
print("=" * 60)

# Test 1: Initial state
print("\n1. Initial state:")
handlers = CardHandlerFactory._handlers
print(f"   Initial handlers count: {len(handlers)}")

# Test 2: Load handlers
print("\n2. Loading handlers...")
CardHandlerFactory.load_and_register_handlers()
handlers = CardHandlerFactory._handlers
print(f"   After load handlers count: {len(handlers)}")

# Test 3: List all handlers
print("\n3. Registered handlers:")
for k, v in handlers.items():
    print(f"   {k}: {type(v).__name__}")

# Test 4: Get specific handlers
print("\n4. Testing get_handler:")
test_cases = [
    ('timer', 'alarm'),
    ('timer', 'countdown'),
    ('timer', 'count'),
    ('sample', 'sample1'),
    ('sample', 'sample2'),
    ('sample', 'sample3'),
    ('relax', 'wordle'),
]

for card_type, card_sub_type in test_cases:
    try:
        handler = CardHandlerFactory.get_handler(card_type, card_sub_type)
        print(f"   ✓ Success: {card_type}/{card_sub_type} -> {type(handler).__name__}")
    except Exception as e:
        print(f"   ✗ Failed: {card_type}/{card_sub_type} -> {str(e)}")

print("\n" + "=" * 60)
print("Test completed!")
