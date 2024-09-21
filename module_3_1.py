
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(str):
    count_calls()
    return (len(str), str.upper(), str.lower())

def is_contains(str, list):
    count_calls()
    for s in list:
        if str.lower() == s.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)