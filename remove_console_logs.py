import re
from pathlib import Path

def remove_console_logs(filepath):
    """Remove all console.log statements from JavaScript file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_lines = len(content.split('\n'))
    
    # Remove various console.log patterns
    patterns = [
        r'console\.log\([^)]*\);?\s*\n',
        r'\s*console\.log\([^)]*\);?',
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content)
    
    # Clean up .catch(err => console.log(...))
    content = re.sub(r'\.catch\(err => console\.log\([^)]*\)\)', '.catch(err => {})', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_lines = len(content.split('\n'))
    return original_lines, new_lines

base_dir = Path('/app/sentient_website_redesign_0308')
js_files = [
    base_dir / 'scripts' / 'tools.js',
    base_dir / 'scripts' / 'consumer-tools.js'
]

print("Removing console.log statements from JavaScript files...")
print("=" * 80)

for js_file in js_files:
    if js_file.exists():
        orig, new = remove_console_logs(js_file)
        print(f"\n✅ {js_file.name}")
        print(f"   Original lines: {orig}")
        print(f"   New lines: {new}")
        print(f"   Lines removed: {orig - new}")

print("\n" + "=" * 80)
print("Verification - Searching for remaining console.log statements...")
print("=" * 80)

for js_file in js_files:
    if js_file.exists():
        with open(js_file, 'r') as f:
            content = f.read()
        count = content.count('console.log')
        if count > 0:
            print(f"⚠️  {js_file.name}: {count} console.log statements remaining")
        else:
            print(f"✅ {js_file.name}: All console.log statements removed")

print("\n✅ Console.log cleanup complete!")