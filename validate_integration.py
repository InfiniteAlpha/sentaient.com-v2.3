import os
from pathlib import Path

base_path = Path('/app/sentient_website_redesign_0308')

print("=" * 80)
print("CONSUMER TOOLS INTEGRATION VALIDATION")
print("=" * 80)

index_path = base_path / 'index.html'
with open(index_path, 'r') as f:
    html_content = f.read()

print("\n✓ Checking Homepage Integration...")

tool_ids = ['ai-demo-tool', 'assessment-quiz-tool', 'savings-calculator-tool', 'trial-signup-tool']
found_tools = []
missing_tools = []

for tool_id in tool_ids:
    if f'id="{tool_id}"' in html_content:
        found_tools.append(tool_id)
        print(f"  ✓ {tool_id} container found")
    else:
        missing_tools.append(tool_id)
        print(f"  ✗ {tool_id} container missing")

if 'consumer-tools.js' in html_content:
    print("  ✓ consumer-tools.js script tag found")
else:
    print("  ✗ consumer-tools.js script tag missing")

if 'interactive-tools' in html_content:
    print("  ✓ interactive-tools section found")
else:
    print("  ✗ interactive-tools section missing")

print(f"\n{'='*80}")
print("SUMMARY")
print(f"{'='*80}")
print(f"Tools integrated: {len(found_tools)}/{len(tool_ids)}")
print(f"Missing tools: {len(missing_tools)}")

if missing_tools:
    print(f"\nMissing: {', '.join(missing_tools)}")

consumer_js_path = base_path / 'scripts' / 'consumer-tools.js'
if consumer_js_path.exists():
    print(f"\n✓ consumer-tools.js exists ({consumer_js_path.stat().st_size} bytes)")
else:
    print("\n✗ consumer-tools.js file missing")

test_page_path = base_path / 'test_tools_page.html'
if test_page_path.exists():
    print(f"✓ test_tools_page.html exists for standalone testing")
else:
    print("✗ test_tools_page.html missing")

print(f"\n{'='*80}")
if len(found_tools) == len(tool_ids) and 'consumer-tools.js' in html_content:
    print("✓✓✓ INTEGRATION COMPLETE ✓✓✓")
else:
    print("⚠ INTEGRATION INCOMPLETE - See issues above")
print(f"{'='*80}")