import os
import json
from pathlib import Path

base_path = Path('/app/sentient_website_redesign_0308')

print("=" * 80)
print("CONSUMER TOOLS IMPLEMENTATION VALIDATION")
print("=" * 80)

validation_results = {
    "files_created": [],
    "files_integrated": [],
    "issues": [],
    "success": True
}

print("\n1. Checking Consumer Tools JavaScript Module...")
consumer_js_path = base_path / 'scripts' / 'consumer-tools.js'
if consumer_js_path.exists():
    with open(consumer_js_path, 'r') as f:
        content = f.read()
        tools = ['AIDemo', 'AssessmentQuiz', 'SavingsCalculator', 'TrialSignup']
        for tool in tools:
            if tool in content:
                print(f"   ✓ {tool} implementation found")
                validation_results["files_created"].append(f"{tool} in consumer-tools.js")
            else:
                print(f"   ✗ {tool} implementation missing")
                validation_results["issues"].append(f"{tool} missing from consumer-tools.js")
                validation_results["success"] = False
        
        print(f"   ✓ File size: {len(content)} characters")
else:
    print("   ✗ consumer-tools.js not found")
    validation_results["issues"].append("consumer-tools.js file not created")
    validation_results["success"] = False

print("\n2. Checking CSS Styling...")
css_path = base_path / 'styles' / 'main.css'
if css_path.exists():
    with open(css_path, 'r') as f:
        content = f.read()
        css_classes = [
            'consumer-tools-section',
            'ai-demo-container',
            'quiz-container',
            'calculator-container',
            'trial-signup-container',
            'share-modal'
        ]
        found_classes = 0
        for css_class in css_classes:
            if css_class in content:
                found_classes += 1
        
        print(f"   ✓ Found {found_classes}/{len(css_classes)} required CSS classes")
        if found_classes == len(css_classes):
            validation_results["files_created"].append("Complete CSS styling")
        else:
            validation_results["issues"].append(f"Only {found_classes}/{len(css_classes)} CSS classes found")
            validation_results["success"] = False
else:
    print("   ✗ main.css not found")
    validation_results["issues"].append("main.css not found")
    validation_results["success"] = False

print("\n3. Checking Homepage Integration...")
index_path = base_path / 'index.html'
if index_path.exists():
    with open(index_path, 'r') as f:
        content = f.read()
        
        if 'consumer-tools.js' in content:
            print("   ✓ consumer-tools.js script included")
            validation_results["files_integrated"].append("consumer-tools.js script tag")
        else:
            print("   ✗ consumer-tools.js script not included")
            validation_results["issues"].append("consumer-tools.js script tag missing")
            validation_results["success"] = False
        
        tool_ids = ['ai-demo-tool', 'assessment-quiz-tool', 'savings-calculator-tool', 'trial-signup-tool']
        found_ids = 0
        for tool_id in tool_ids:
            if tool_id in content:
                found_ids += 1
        
        print(f"   ✓ Found {found_ids}/{len(tool_ids)} tool containers in HTML")
        if found_ids == len(tool_ids):
            validation_results["files_integrated"].append("All tool containers in homepage")
        else:
            validation_results["issues"].append(f"Only {found_ids}/{len(tool_ids)} tool containers found")
            validation_results["success"] = False
        
        if 'interactive-tools' in content:
            print("   ✓ Interactive tools section found")
            validation_results["files_integrated"].append("Interactive tools navigation section")
        else:
            print("   ✗ Interactive tools section missing")
            validation_results["issues"].append("Interactive tools section not found")
else:
    print("   ✗ index.html not found")
    validation_results["issues"].append("index.html not found")
    validation_results["success"] = False

print("\n4. Checking JavaScript Functionality...")
if consumer_js_path.exists():
    with open(consumer_js_path, 'r') as f:
        content = f.read()
        
        features = {
            'Email validation': 'validateEmail',
            'Local storage': 'saveProgress',
            'Analytics logging': 'logEvent',
            'Social sharing': 'shareResult',
            'Form validation': 'serializeForm'
        }
        
        for feature_name, function_name in features.items():
            if function_name in content:
                print(f"   ✓ {feature_name} implemented")
            else:
                print(f"   ✗ {feature_name} missing")
                validation_results["issues"].append(f"{feature_name} not implemented")

print("\n5. Mobile Responsiveness Check...")
if css_path.exists():
    with open(css_path, 'r') as f:
        content = f.read()
        
        if '@media (max-width: 768px)' in content:
            print("   ✓ Mobile breakpoints defined")
            validation_results["files_created"].append("Mobile-responsive CSS")
        else:
            print("   ✗ Mobile breakpoints missing")
            validation_results["issues"].append("Mobile breakpoints not defined")

print("\n" + "=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)
print(f"\nFiles Created: {len(validation_results['files_created'])}")
for item in validation_results['files_created']:
    print(f"  • {item}")

print(f"\nIntegration Points: {len(validation_results['files_integrated'])}")
for item in validation_results['files_integrated']:
    print(f"  • {item}")

if validation_results['issues']:
    print(f"\nIssues Found: {len(validation_results['issues'])}")
    for item in validation_results['issues']:
        print(f"  ⚠ {item}")
else:
    print("\n✓ No issues found!")

print(f"\nOverall Status: {'✓ PASS' if validation_results['success'] else '✗ FAIL'}")
print("=" * 80)

with open(base_path / 'consumer_tools_validation.json', 'w') as f:
    json.dump(validation_results, f, indent=2)
    print(f"\nValidation results saved to: consumer_tools_validation.json")