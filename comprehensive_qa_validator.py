import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.issues = []
        self.meta_tags = {}
        self.headings = []
        self.images = []
        self.links = []
        self.aria_labels = []
        
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs_dict = dict(attrs)
        
        if tag == 'meta':
            if 'name' in attrs_dict:
                self.meta_tags[attrs_dict['name']] = attrs_dict.get('content', '')
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.headings.append(tag)
        elif tag == 'img':
            self.images.append({
                'src': attrs_dict.get('src', ''),
                'alt': attrs_dict.get('alt', ''),
                'has_alt': 'alt' in attrs_dict
            })
        elif tag == 'a':
            self.links.append({
                'href': attrs_dict.get('href', ''),
                'aria_label': attrs_dict.get('aria-label', ''),
                'has_aria': 'aria-label' in attrs_dict
            })
        
        if any(attr[0].startswith('aria-') for attr in attrs):
            self.aria_labels.append({
                'tag': tag,
                'attrs': [attr for attr in attrs if attr[0].startswith('aria-')]
            })

def analyze_html_file(filepath):
    """Analyze HTML file for structure, SEO, and accessibility."""
    results = {
        'filepath': str(filepath),
        'filename': filepath.name,
        'seo': {},
        'accessibility': {},
        'structure': {},
        'issues': []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        validator = HTMLValidator()
        validator.feed(content)
        
        # SEO Analysis
        results['seo']['has_title'] = '<title>' in content
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            results['seo']['title'] = title
            results['seo']['title_length'] = len(title)
            results['seo']['title_optimal'] = 50 <= len(title) <= 60
        
        results['seo']['meta_description'] = validator.meta_tags.get('description', '')
        desc_len = len(results['seo']['meta_description'])
        results['seo']['description_length'] = desc_len
        results['seo']['description_optimal'] = 150 <= desc_len <= 160
        
        results['seo']['has_viewport'] = 'viewport' in validator.meta_tags
        
        # Heading hierarchy
        h1_count = validator.headings.count('h1')
        results['structure']['h1_count'] = h1_count
        results['structure']['heading_hierarchy'] = validator.headings[:10]
        
        if h1_count == 0:
            results['issues'].append('CRITICAL: No H1 heading found')
        elif h1_count > 1:
            results['issues'].append(f'WARNING: Multiple H1 headings ({h1_count})')
        
        # Accessibility - Images
        images_without_alt = [img for img in validator.images if not img['has_alt']]
        results['accessibility']['total_images'] = len(validator.images)
        results['accessibility']['images_with_alt'] = len([img for img in validator.images if img['has_alt']])
        results['accessibility']['images_without_alt'] = len(images_without_alt)
        
        if images_without_alt:
            results['issues'].append(f'ACCESSIBILITY: {len(images_without_alt)} images missing alt text')
        
        # Accessibility - ARIA
        results['accessibility']['aria_labels_count'] = len(validator.aria_labels)
        results['accessibility']['has_lang'] = 'lang="en"' in content or 'lang=\'en\'' in content
        
        if not results['accessibility']['has_lang']:
            results['issues'].append('ACCESSIBILITY: Missing lang attribute on html tag')
        
        # Links
        results['structure']['total_links'] = len(validator.links)
        empty_links = [link for link in validator.links if not link['href'] or link['href'] == '#']
        if empty_links:
            results['issues'].append(f'WARNING: {len(empty_links)} empty or placeholder links')
        
        # Semantic HTML
        has_header = '<header' in content
        has_nav = '<nav' in content
        has_main = '<main' in content
        has_footer = '<footer' in content
        
        results['structure']['semantic_html'] = {
            'has_header': has_header,
            'has_nav': has_nav,
            'has_main': has_main,
            'has_footer': has_footer
        }
        
        missing_semantic = []
        if not has_header:
            missing_semantic.append('header')
        if not has_nav:
            missing_semantic.append('nav')
        if not has_main:
            missing_semantic.append('main')
        if not has_footer:
            missing_semantic.append('footer')
        
        if missing_semantic:
            results['issues'].append(f'SEMANTIC: Missing semantic tags: {", ".join(missing_semantic)}')
        
    except Exception as e:
        results['issues'].append(f'ERROR: {str(e)}')
    
    return results

def analyze_css_file(filepath):
    """Analyze CSS for responsive design and performance."""
    results = {
        'filepath': str(filepath),
        'size_bytes': 0,
        'lines': 0,
        'media_queries': [],
        'color_usage': {},
        'issues': []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        results['size_bytes'] = len(content.encode('utf-8'))
        results['lines'] = len(content.split('\n'))
        
        # Media queries
        media_queries = re.findall(r'@media[^{]+', content)
        results['media_queries'] = [mq.strip() for mq in media_queries]
        results['media_query_count'] = len(media_queries)
        
        # Check for responsive breakpoints
        has_mobile = any('max-width' in mq and ('768px' in mq or '767px' in mq) for mq in media_queries)
        has_tablet = any('max-width' in mq and '1024px' in mq for mq in media_queries)
        
        results['responsive_breakpoints'] = {
            'has_mobile': has_mobile,
            'has_tablet': has_tablet
        }
        
        # Brand colors
        brand_colors = {
            '#60a9ff': content.count('#60a9ff'),
            '#202733': content.count('#202733'),
            '#ffffff': content.count('#ffffff')
        }
        results['color_usage'] = brand_colors
        
        if brand_colors['#60a9ff'] == 0 and brand_colors['#202733'] == 0:
            results['issues'].append('WARNING: Brand colors not found in CSS')
        
    except Exception as e:
        results['issues'].append(f'ERROR: {str(e)}')
    
    return results

def analyze_js_file(filepath):
    """Analyze JavaScript file."""
    results = {
        'filepath': str(filepath),
        'size_bytes': 0,
        'lines': 0,
        'has_console_logs': False,
        'issues': []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        results['size_bytes'] = len(content.encode('utf-8'))
        results['lines'] = len(content.split('\n'))
        
        # Check for console.log statements
        console_logs = re.findall(r'console\.log\(', content)
        results['has_console_logs'] = len(console_logs) > 0
        results['console_log_count'] = len(console_logs)
        
        if results['has_console_logs']:
            results['issues'].append(f'WARNING: {len(console_logs)} console.log statements found (should be removed for production)')
        
        # Check for event listeners
        has_event_listeners = 'addEventListener' in content
        results['has_event_listeners'] = has_event_listeners
        
    except Exception as e:
        results['issues'].append(f'ERROR: {str(e)}')
    
    return results

def main():
    base_dir = Path('/app/sentient_website_redesign_0308')
    
    report = {
        'timestamp': '2025-11-15T04:46:45+00:00',
        'html_files': [],
        'css_files': [],
        'js_files': [],
        'summary': {
            'total_issues': 0,
            'critical_issues': 0,
            'warnings': 0
        }
    }
    
    # Analyze HTML files
    html_files = list(base_dir.glob('**/*.html'))
    html_files = [f for f in html_files if 'test_' not in f.name]
    
    print(f"\n{'='*80}")
    print(f"COMPREHENSIVE QA VALIDATION REPORT")
    print(f"{'='*80}\n")
    
    print(f"📄 HTML FILES ANALYSIS ({len(html_files)} files)")
    print("-" * 80)
    
    for html_file in html_files:
        print(f"\n📝 Analyzing: {html_file.relative_to(base_dir)}")
        analysis = analyze_html_file(html_file)
        report['html_files'].append(analysis)
        
        # SEO
        print(f"  SEO:")
        print(f"    • Title: {analysis['seo'].get('title', 'MISSING')[:60]}")
        print(f"    • Title Length: {analysis['seo'].get('title_length', 0)} chars (Optimal: 50-60)")
        print(f"    • Meta Description: {analysis['seo'].get('description_length', 0)} chars (Optimal: 150-160)")
        
        # Accessibility
        print(f"  Accessibility:")
        print(f"    • Images with alt text: {analysis['accessibility']['images_with_alt']}/{analysis['accessibility']['total_images']}")
        print(f"    • ARIA labels: {analysis['accessibility']['aria_labels_count']}")
        print(f"    • Lang attribute: {'✓' if analysis['accessibility']['has_lang'] else '✗'}")
        
        # Structure
        print(f"  Structure:")
        print(f"    • H1 count: {analysis['structure']['h1_count']}")
        semantic = analysis['structure']['semantic_html']
        print(f"    • Semantic HTML: header={semantic['has_header']}, nav={semantic['has_nav']}, main={semantic['has_main']}, footer={semantic['has_footer']}")
        
        # Issues
        if analysis['issues']:
            print(f"  ⚠️  Issues:")
            for issue in analysis['issues']:
                print(f"    • {issue}")
                if 'CRITICAL' in issue:
                    report['summary']['critical_issues'] += 1
                elif 'WARNING' in issue:
                    report['summary']['warnings'] += 1
                report['summary']['total_issues'] += 1
    
    # Analyze CSS files
    css_files = list(base_dir.glob('**/*.css'))
    print(f"\n\n🎨 CSS FILES ANALYSIS ({len(css_files)} files)")
    print("-" * 80)
    
    for css_file in css_files:
        print(f"\n📝 Analyzing: {css_file.relative_to(base_dir)}")
        analysis = analyze_css_file(css_file)
        report['css_files'].append(analysis)
        
        print(f"  • Size: {analysis['size_bytes']:,} bytes ({analysis['size_bytes']/1024:.1f} KB)")
        print(f"  • Lines: {analysis['lines']:,}")
        print(f"  • Media queries: {analysis['media_query_count']}")
        print(f"  • Responsive: Mobile={analysis['responsive_breakpoints']['has_mobile']}, Tablet={analysis['responsive_breakpoints']['has_tablet']}")
        print(f"  • Brand colors: #60a9ff={analysis['color_usage']['#60a9ff']}, #202733={analysis['color_usage']['#202733']}")
        
        if analysis['issues']:
            for issue in analysis['issues']:
                print(f"  ⚠️  {issue}")
                report['summary']['total_issues'] += 1
                report['summary']['warnings'] += 1
    
    # Analyze JS files
    js_files = list(base_dir.glob('scripts/*.js'))
    print(f"\n\n⚙️  JAVASCRIPT FILES ANALYSIS ({len(js_files)} files)")
    print("-" * 80)
    
    for js_file in js_files:
        print(f"\n📝 Analyzing: {js_file.relative_to(base_dir)}")
        analysis = analyze_js_file(js_file)
        report['js_files'].append(analysis)
        
        print(f"  • Size: {analysis['size_bytes']:,} bytes ({analysis['size_bytes']/1024:.1f} KB)")
        print(f"  • Lines: {analysis['lines']:,}")
        print(f"  • Console logs: {analysis['console_log_count']}")
        
        if analysis['issues']:
            for issue in analysis['issues']:
                print(f"  ⚠️  {issue}")
                report['summary']['total_issues'] += 1
                report['summary']['warnings'] += 1
    
    # Summary
    print(f"\n\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total Issues: {report['summary']['total_issues']}")
    print(f"  • Critical: {report['summary']['critical_issues']}")
    print(f"  • Warnings: {report['summary']['warnings']}")
    
    # Save report
    report_path = base_dir / 'docs' / 'QA_VALIDATION_REPORT.json'
    report_path.parent.mkdir(exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Detailed report saved to: {report_path.relative_to(base_dir)}")
    
    return report

if __name__ == '__main__':
    main()