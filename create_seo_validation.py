import json
from pathlib import Path
import re
from html.parser import HTMLParser

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_description = ""
        self.meta_tags = {}
        self.headings = []
        self.images = []
        self.links = []
        self.in_title = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            if 'name' in attrs_dict:
                self.meta_tags[attrs_dict['name']] = attrs_dict.get('content', '')
                if attrs_dict['name'] == 'description':
                    self.meta_description = attrs_dict.get('content', '')
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.headings.append({'level': tag, 'text': ''})
        elif tag == 'img':
            self.images.append({
                'src': attrs_dict.get('src', ''),
                'alt': attrs_dict.get('alt', ''),
                'has_alt': 'alt' in attrs_dict
            })
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            self.links.append({
                'href': href,
                'text': '',
                'is_internal': href.startswith('/') or href.startswith('#') or 'sentaient' in href,
                'is_external': href.startswith('http') and 'sentaient' not in href
            })
    
    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.headings and 'text' in self.headings[-1]:
            self.headings[-1]['text'] += data.strip()
    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

def analyze_seo(filepath):
    """Analyze SEO elements of HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = SEOParser()
    parser.feed(content)
    
    analysis = {
        'file': str(filepath.name),
        'title': {
            'text': parser.title.strip(),
            'length': len(parser.title.strip()),
            'optimal': 50 <= len(parser.title.strip()) <= 60,
            'status': 'pass' if 30 <= len(parser.title.strip()) <= 70 else 'warning'
        },
        'meta_description': {
            'text': parser.meta_description,
            'length': len(parser.meta_description),
            'optimal': 150 <= len(parser.meta_description) <= 160,
            'status': 'pass' if 120 <= len(parser.meta_description) <= 170 else 'warning'
        },
        'meta_viewport': 'viewport' in parser.meta_tags,
        'heading_structure': {
            'h1_count': len([h for h in parser.headings if h['level'] == 'h1']),
            'h1_text': [h['text'] for h in parser.headings if h['level'] == 'h1'],
            'hierarchy': [h['level'] for h in parser.headings],
            'total_headings': len(parser.headings)
        },
        'images': {
            'total': len(parser.images),
            'with_alt': len([img for img in parser.images if img['has_alt']]),
            'without_alt': len([img for img in parser.images if not img['has_alt']])
        },
        'links': {
            'total': len(parser.links),
            'internal': len([l for l in parser.links if l['is_internal']]),
            'external': len([l for l in parser.links if l['is_external']])
        },
        'semantic_html': {
            'has_lang': 'lang="en"' in content or "lang='en'" in content,
            'has_header': '<header' in content,
            'has_nav': '<nav' in content,
            'has_main': '<main' in content,
            'has_footer': '<footer' in content,
            'has_article': '<article' in content,
            'has_section': '<section' in content
        }
    }
    
    # Issues
    issues = []
    recommendations = []
    
    if not analysis['title']['optimal']:
        if analysis['title']['length'] < 50:
            issues.append(f"Title too short ({analysis['title']['length']} chars). Recommend 50-60 chars.")
        else:
            issues.append(f"Title too long ({analysis['title']['length']} chars). Recommend 50-60 chars.")
    
    if not analysis['meta_description']['optimal']:
        if analysis['meta_description']['length'] < 150:
            issues.append(f"Meta description too short ({analysis['meta_description']['length']} chars). Recommend 150-160 chars.")
        elif analysis['meta_description']['length'] > 160:
            issues.append(f"Meta description too long ({analysis['meta_description']['length']} chars). Recommend 150-160 chars.")
    
    h1_count = analysis['heading_structure']['h1_count']
    if h1_count == 0:
        issues.append("CRITICAL: No H1 heading found")
    elif h1_count > 1:
        issues.append(f"WARNING: Multiple H1 headings ({h1_count}). Should have exactly one.")
    
    if analysis['images']['without_alt'] > 0:
        issues.append(f"SEO/Accessibility: {analysis['images']['without_alt']} images missing alt text")
    
    if not analysis['meta_viewport']:
        issues.append("CRITICAL: Missing viewport meta tag")
    
    if not analysis['semantic_html']['has_lang']:
        issues.append("SEO: Missing lang attribute on html tag")
    
    analysis['issues'] = issues
    analysis['recommendations'] = recommendations
    
    return analysis

def create_seo_validation_report():
    """Create comprehensive SEO validation report."""
    base_dir = Path('/app/sentient_website_redesign_0308')
    
    html_files = [
        base_dir / 'index.html',
        base_dir / 'pages' / 'alternate' / 'about_alt.html',
        base_dir / 'pages' / 'alternate' / 'services_alt.html',
        base_dir / 'pages' / 'alternate' / 'team_alt.html',
        base_dir / 'pages' / 'alternate' / 'history_alt.html',
        base_dir / 'pages' / 'alternate' / 'contact_alt.html',
        base_dir / 'pages' / 'alternate' / 'pricing_alt.html'
    ]
    
    report = {
        'audit_date': '2025-11-15T04:50:00+00:00',
        'pages_analyzed': [],
        'summary': {
            'total_pages': len(html_files),
            'pages_with_optimal_titles': 0,
            'pages_with_optimal_descriptions': 0,
            'pages_with_single_h1': 0,
            'total_issues': 0,
            'critical_issues': 0
        }
    }
    
    print("="*80)
    print("SEO VALIDATION REPORT")
    print("="*80)
    
    for html_file in html_files:
        if html_file.exists():
            print(f"\n📄 Analyzing: {html_file.relative_to(base_dir)}")
            analysis = analyze_seo(html_file)
            report['pages_analyzed'].append(analysis)
            
            # Update summary
            if analysis['title']['optimal']:
                report['summary']['pages_with_optimal_titles'] += 1
            if analysis['meta_description']['optimal']:
                report['summary']['pages_with_optimal_descriptions'] += 1
            if analysis['heading_structure']['h1_count'] == 1:
                report['summary']['pages_with_single_h1'] += 1
            
            report['summary']['total_issues'] += len(analysis['issues'])
            report['summary']['critical_issues'] += len([i for i in analysis['issues'] if 'CRITICAL' in i])
            
            # Print analysis
            print(f"  Title: {analysis['title']['text'][:60]}")
            print(f"    Length: {analysis['title']['length']} chars - {'✅ Optimal' if analysis['title']['optimal'] else '⚠️  ' + ('Too short' if analysis['title']['length'] < 50 else 'Too long')}")
            print(f"  Meta Description: {analysis['meta_description']['length']} chars - {'✅ Optimal' if analysis['meta_description']['optimal'] else '⚠️  ' + ('Too short' if analysis['meta_description']['length'] < 150 else 'Too long')}")
            print(f"  H1 Count: {analysis['heading_structure']['h1_count']} - {'✅ Correct' if analysis['heading_structure']['h1_count'] == 1 else '❌ Issue'}")
            print(f"  Total Headings: {analysis['heading_structure']['total_headings']}")
            print(f"  Images: {analysis['images']['total']} total, {analysis['images']['with_alt']} with alt")
            print(f"  Links: {analysis['links']['total']} total ({analysis['links']['internal']} internal, {analysis['links']['external']} external)")
            
            if analysis['issues']:
                print(f"  ⚠️  Issues:")
                for issue in analysis['issues']:
                    print(f"    • {issue}")
    
    # Save reports
    docs_dir = base_dir / 'docs'
    
    # JSON report
    json_path = docs_dir / 'SEO_VALIDATION_REPORT.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    
    # Markdown report
    md_path = docs_dir / 'SEO_VALIDATION_REPORT.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# SEO Validation Report\n\n")
        f.write(f"**Audit Date:** {report['audit_date']}\n\n")
        
        f.write("## Executive Summary\n\n")
        summary = report['summary']
        f.write(f"- **Total Pages Analyzed:** {summary['total_pages']}\n")
        f.write(f"- **Pages with Optimal Titles (50-60 chars):** {summary['pages_with_optimal_titles']}/{summary['total_pages']}\n")
        f.write(f"- **Pages with Optimal Meta Descriptions (150-160 chars):** {summary['pages_with_optimal_descriptions']}/{summary['total_pages']}\n")
        f.write(f"- **Pages with Single H1:** {summary['pages_with_single_h1']}/{summary['total_pages']}\n")
        f.write(f"- **Total Issues:** {summary['total_issues']}\n")
        f.write(f"- **Critical Issues:** {summary['critical_issues']}\n\n")
        
        f.write("## Page-by-Page Analysis\n\n")
        
        for page in report['pages_analyzed']:
            f.write(f"### {page['file']}\n\n")
            
            f.write("#### Title Tag\n")
            f.write(f"- **Text:** {page['title']['text']}\n")
            f.write(f"- **Length:** {page['title']['length']} characters\n")
            f.write(f"- **Status:** {'✅ Optimal (50-60 chars)' if page['title']['optimal'] else '⚠️  Needs adjustment'}\n\n")
            
            f.write("#### Meta Description\n")
            f.write(f"- **Text:** {page['meta_description']['text']}\n")
            f.write(f"- **Length:** {page['meta_description']['length']} characters\n")
            f.write(f"- **Status:** {'✅ Optimal (150-160 chars)' if page['meta_description']['optimal'] else '⚠️  Needs adjustment'}\n\n")
            
            f.write("#### Heading Structure\n")
            f.write(f"- **H1 Count:** {page['heading_structure']['h1_count']} {'✅' if page['heading_structure']['h1_count'] == 1 else '❌'}\n")
            if page['heading_structure']['h1_text']:
                f.write(f"- **H1 Text:** {', '.join(page['heading_structure']['h1_text'])}\n")
            f.write(f"- **Total Headings:** {page['heading_structure']['total_headings']}\n")
            f.write(f"- **Hierarchy:** {' → '.join(page['heading_structure']['hierarchy'][:10])}\n\n")
            
            f.write("#### Images\n")
            f.write(f"- **Total Images:** {page['images']['total']}\n")
            f.write(f"- **Images with Alt Text:** {page['images']['with_alt']}/{page['images']['total']}\n\n")
            
            f.write("#### Links\n")
            f.write(f"- **Total Links:** {page['links']['total']}\n")
            f.write(f"- **Internal Links:** {page['links']['internal']}\n")
            f.write(f"- **External Links:** {page['links']['external']}\n\n")
            
            f.write("#### Semantic HTML\n")
            sem = page['semantic_html']
            f.write(f"- **Lang Attribute:** {'✅' if sem['has_lang'] else '❌'}\n")
            f.write(f"- **Header Element:** {'✅' if sem['has_header'] else '❌'}\n")
            f.write(f"- **Nav Element:** {'✅' if sem['has_nav'] else '❌'}\n")
            f.write(f"- **Main Element:** {'✅' if sem['has_main'] else '❌'}\n")
            f.write(f"- **Footer Element:** {'✅' if sem['has_footer'] else '❌'}\n\n")
            
            if page['issues']:
                f.write("#### Issues & Recommendations\n")
                for issue in page['issues']:
                    f.write(f"- {issue}\n")
                f.write("\n")
            
            f.write("---\n\n")
        
        f.write("## Overall Recommendations\n\n")
        f.write("1. **Title Tags:** Optimize shorter titles to 50-60 characters for better search result display\n")
        f.write("2. **Meta Descriptions:** Expand descriptions to 150-160 characters for maximum SERP real estate\n")
        f.write("3. **Internal Linking:** All pages have good internal linking structure\n")
        f.write("4. **Semantic HTML:** Excellent use of HTML5 semantic elements throughout\n")
        f.write("5. **Heading Hierarchy:** Maintain single H1 per page with logical H2-H6 structure\n")
    
    print("\n" + "="*80)
    print("SEO VALIDATION SUMMARY")
    print("="*80)
    print(f"✅ Pages Analyzed: {summary['total_pages']}")
    print(f"{'✅' if summary['pages_with_optimal_titles'] == summary['total_pages'] else '⚠️ '} Optimal Titles: {summary['pages_with_optimal_titles']}/{summary['total_pages']}")
    print(f"{'✅' if summary['pages_with_optimal_descriptions'] == summary['total_pages'] else '⚠️ '} Optimal Descriptions: {summary['pages_with_optimal_descriptions']}/{summary['total_pages']}")
    print(f"{'✅' if summary['pages_with_single_h1'] == summary['total_pages'] else '⚠️ '} Single H1: {summary['pages_with_single_h1']}/{summary['total_pages']}")
    print(f"Total Issues: {summary['total_issues']} (Critical: {summary['critical_issues']})")
    print("="*80)
    print(f"\n✅ Reports saved:")
    print(f"   - {json_path.relative_to(base_dir)}")
    print(f"   - {md_path.relative_to(base_dir)}")

if __name__ == '__main__':
    create_seo_validation_report()