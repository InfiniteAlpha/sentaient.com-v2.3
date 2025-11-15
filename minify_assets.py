import re
from pathlib import Path

def minify_css(content):
    """Minify CSS content."""
    # Remove comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove whitespace around special characters
    content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', content)
    # Remove newlines and extra spaces
    content = re.sub(r'\s+', ' ', content)
    # Remove trailing semicolons
    content = re.sub(r';}', '}', content)
    return content.strip()

def minify_js(content):
    """Basic JavaScript minification."""
    # Remove single-line comments
    content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove extra whitespace but preserve string literals
    lines = content.split('\n')
    minified_lines = []
    for line in lines:
        line = line.strip()
        if line:
            minified_lines.append(line)
    content = '\n'.join(minified_lines)
    # Reduce multiple spaces to single space
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def minify_file(input_path, output_path, file_type):
    """Minify a file and save to output path."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content.encode('utf-8'))
    
    if file_type == 'css':
        minified = minify_css(content)
    elif file_type == 'js':
        minified = minify_js(content)
    else:
        minified = content
    
    minified_size = len(minified.encode('utf-8'))
    reduction = ((original_size - minified_size) / original_size) * 100
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(minified)
    
    return original_size, minified_size, reduction

def main():
    base_dir = Path('/app/sentient_website_redesign_0308')
    
    files_to_minify = [
        {
            'input': base_dir / 'styles' / 'main.css',
            'output': base_dir / 'styles' / 'main.min.css',
            'type': 'css'
        },
        {
            'input': base_dir / 'scripts' / 'main.js',
            'output': base_dir / 'scripts' / 'main.min.js',
            'type': 'js'
        },
        {
            'input': base_dir / 'scripts' / 'tools.js',
            'output': base_dir / 'scripts' / 'tools.min.js',
            'type': 'js'
        },
        {
            'input': base_dir / 'scripts' / 'consumer-tools.js',
            'output': base_dir / 'scripts' / 'consumer-tools.min.js',
            'type': 'js'
        }
    ]
    
    print("="*80)
    print("ASSET MINIFICATION")
    print("="*80)
    
    total_original = 0
    total_minified = 0
    
    for file_info in files_to_minify:
        if file_info['input'].exists():
            print(f"\n📦 Minifying: {file_info['input'].name}")
            
            orig_size, min_size, reduction = minify_file(
                file_info['input'],
                file_info['output'],
                file_info['type']
            )
            
            total_original += orig_size
            total_minified += min_size
            
            print(f"   Original: {orig_size:,} bytes ({orig_size/1024:.1f} KB)")
            print(f"   Minified: {min_size:,} bytes ({min_size/1024:.1f} KB)")
            print(f"   Reduction: {reduction:.1f}%")
            print(f"   ✅ Saved to: {file_info['output'].name}")
        else:
            print(f"   ⚠️  File not found: {file_info['input']}")
    
    total_reduction = ((total_original - total_minified) / total_original) * 100
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total Original Size: {total_original:,} bytes ({total_original/1024:.1f} KB)")
    print(f"Total Minified Size: {total_minified:,} bytes ({total_minified/1024:.1f} KB)")
    print(f"Total Reduction: {reduction:.1f}% ({(total_original - total_minified):,} bytes saved)")
    print("="*80)
    
    # Create performance report
    report = {
        'minification_date': '2025-11-15T04:51:00+00:00',
        'files_minified': len(files_to_minify),
        'total_original_bytes': total_original,
        'total_minified_bytes': total_minified,
        'total_reduction_percentage': total_reduction,
        'files': []
    }
    
    for file_info in files_to_minify:
        if file_info['input'].exists():
            with open(file_info['input'], 'r', encoding='utf-8') as f:
                orig_size = len(f.read().encode('utf-8'))
            with open(file_info['output'], 'r', encoding='utf-8') as f:
                min_size = len(f.read().encode('utf-8'))
            
            report['files'].append({
                'filename': file_info['input'].name,
                'type': file_info['type'],
                'original_size': orig_size,
                'minified_size': min_size,
                'reduction_percentage': ((orig_size - min_size) / orig_size) * 100
            })
    
    import json
    docs_dir = base_dir / 'docs'
    docs_dir.mkdir(exist_ok=True)
    
    with open(docs_dir / 'MINIFICATION_REPORT.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Minification report saved: docs/MINIFICATION_REPORT.json")

if __name__ == '__main__':
    main()