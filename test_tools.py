import os
import json

def test_file_existence():
    """Test that all required files exist"""
    base_path = "/app/sentient_website_redesign_0308"
    
    required_files = [
        "scripts/tools.js",
        "index.html",
        "pages/alternate/pricing_alt.html",
        "pages/alternate/contact_alt.html",
        "styles/main.css"
    ]
    
    print("Testing file existence...")
    all_exist = True
    for file_path in required_files:
        full_path = os.path.join(base_path, file_path)
        exists = os.path.exists(full_path)
        status = "✓" if exists else "✗"
        print(f"  {status} {file_path}")
        if not exists:
            all_exist = False
    
    return all_exist

def test_html_integration():
    """Test that tools are properly integrated into HTML"""
    base_path = "/app/sentient_website_redesign_0308"
    
    tests = {
        "index.html": [
            "roi-calculator",
            "service-selector",
            "consultation-modal",
            "scripts/tools.js"
        ],
        "pages/alternate/pricing_alt.html": [
            "pricing-calculator",
            "scripts/tools.js"
        ],
        "pages/alternate/contact_alt.html": [
            "consultation-form",
            "scripts/tools.js"
        ]
    }
    
    print("\nTesting HTML integration...")
    all_passed = True
    
    for file_name, required_ids in tests.items():
        file_path = os.path.join(base_path, file_name)
        with open(file_path, 'r') as f:
            content = f.read()
        
        print(f"\n  {file_name}:")
        for required_id in required_ids:
            found = required_id in content
            status = "✓" if found else "✗"
            print(f"    {status} Contains '{required_id}'")
            if not found:
                all_passed = False
    
    return all_passed

def test_javascript_structure():
    """Test JavaScript file structure"""
    js_path = "/app/sentient_website_redesign_0308/scripts/tools.js"
    
    print("\nTesting JavaScript structure...")
    
    with open(js_path, 'r') as f:
        js_content = f.read()
    
    required_methods = [
        "initializeROICalculator",
        "initializePricingCalculator",
        "initializeConsultationForm",
        "initializeServiceSelector",
        "calculateROI",
        "calculatePricing",
        "submitConsultation",
        "findServices",
        "validateROIInput",
        "validateConsultationField",
        "getServiceRecommendations"
    ]
    
    all_present = True
    for method in required_methods:
        found = method in js_content
        status = "✓" if found else "✗"
        print(f"  {status} Method: {method}")
        if not found:
            all_present = False
    
    return all_present

def test_css_styling():
    """Test that tool styles are present"""
    css_path = "/app/sentient_website_redesign_0308/styles/main.css"
    
    print("\nTesting CSS styling...")
    
    with open(css_path, 'r') as f:
        css_content = f.read()
    
    required_classes = [
        ".tools-section",
        ".tool-container",
        ".tool-form",
        ".tool-results",
        ".roi-metrics",
        ".pricing-results-content",
        ".consultation-modal",
        ".modal-content",
        ".error-message",
        ".spinner"
    ]
    
    all_present = True
    for class_name in required_classes:
        found = class_name in css_content
        status = "✓" if found else "✗"
        print(f"  {status} Class: {class_name}")
        if not found:
            all_present = False
    
    return all_present

def test_responsive_design():
    """Test responsive design media queries"""
    css_path = "/app/sentient_website_redesign_0308/styles/main.css"
    
    print("\nTesting responsive design...")
    
    with open(css_path, 'r') as f:
        css_content = f.read()
    
    breakpoints = [
        "@media (max-width: 768px)",
        "@media (hover: none)"
    ]
    
    all_present = True
    for breakpoint in breakpoints:
        found = breakpoint in css_content
        status = "✓" if found else "✗"
        print(f"  {status} Breakpoint: {breakpoint}")
        if not found:
            all_present = False
    
    return all_present

def test_form_validation_elements():
    """Test that validation elements are in place"""
    base_path = "/app/sentient_website_redesign_0308"
    
    print("\nTesting form validation elements...")
    
    files_to_check = [
        "index.html",
        "pages/alternate/pricing_alt.html",
        "pages/alternate/contact_alt.html"
    ]
    
    all_valid = True
    for file_name in files_to_check:
        file_path = os.path.join(base_path, file_name)
        with open(file_path, 'r') as f:
            content = f.read()
        
        has_error_message = 'class="error-message"' in content
        has_required = 'required' in content
        
        status = "✓" if (has_error_message and has_required) else "✗"
        print(f"  {status} {file_name}: Validation elements present")
        
        if not (has_error_message and has_required):
            all_valid = False
    
    return all_valid

def generate_summary():
    """Generate test summary"""
    print("\n" + "="*60)
    print("INTERACTIVE TOOLS TEST SUMMARY")
    print("="*60)
    
    results = {
        "File Existence": test_file_existence(),
        "HTML Integration": test_html_integration(),
        "JavaScript Structure": test_javascript_structure(),
        "CSS Styling": test_css_styling(),
        "Responsive Design": test_responsive_design(),
        "Form Validation": test_form_validation_elements()
    }
    
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    
    all_passed = True
    for test_name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"  {symbol} {test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("="*60)
    
    return all_passed

if __name__ == "__main__":
    success = generate_summary()
    exit(0 if success else 1)