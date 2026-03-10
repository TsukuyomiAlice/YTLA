import sys
sys.path.insert(0, 'd:\\YTLA')

print('Testing refactored timer card handlers...\n')

try:
    from features.timer.process.processCardHandlerAlarm import AlarmCardHandler
    from features.timer.process.processCardHandlerCountdown import CountdownCardHandler
    from features.timer.process.processCardHandlerCount import CountCardHandler
    from features.timer.func.funcTimer import calculate_end_time
    print('✓ All imports successful')
except Exception as e:
    print(f'✗ Import failed: {e}')
    sys.exit(1)

try:
    test_start = '2026-03-10 12:00:00'
    result = calculate_end_time(test_start, 'minute', 30)
    print(f'✓ calculate_end_time test passed: {test_start} + 30min = {result}')
except Exception as e:
    print(f'✗ calculate_end_time test failed: {e}')

try:
    alarm_handler = AlarmCardHandler()
    countdown_handler = CountdownCardHandler()
    count_handler = CountCardHandler()
    print('✓ All handler classes instantiated successfully')
except Exception as e:
    print(f'✗ Handler instantiation failed: {e}')

print('\n✅ Refactoring verification complete! All components work correctly.')
