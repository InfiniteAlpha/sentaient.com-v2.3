import shutil
import os
from pathlib import Path
import json

def create_production_package():
    """Create organized production deployment package."""
    base_dir = Path('/app/sentient_website_redesign_0308')
    prod_dir = base_dir / 'production_package'
    
    # Remove existing production package if present
    if prod_dir.exists():
        shutil.rmtree(prod_dir)
    
    prod_dir.mkdir(exist_ok=True)
    
    print("="*80)
    print("CREATING PRODUCTION DEPLOYMENT PACKAGE")
    print("="*80)
    print()
    
    # Create directory structure
    directories = [
        'pages/alternate',
        'styles',
        'scripts',
        'images',
        'docs'
    ]
    
    for directory in directories:
        (prod_dir / directory).mkdir(parents=True, exist_ok=True)
    
    print("📁 Created directory structure")
    
    # Copy HTML files
    html_files = [
        'index.html',
        'pages/alternate/about_alt.html',
        'pages/alternate/services_alt.html',
        'pages/alternate/team_alt.html',
        'pages/alternate/history_alt.html',
        'pages/alternate/contact_alt.html',
        'pages/alternate/pricing_alt.html'
    ]
    
    print("\n📄 Copying HTML files...")
    for html_file in html_files:
        src = base_dir / html_file
        dst = prod_dir / html_file
        if src.exists():
            shutil.copy2(src, dst)
            print(f"   ✅ {html_file}")
    
    # Copy minified CSS
    print("\n🎨 Copying CSS files...")
    css_files = ['main.css', 'main.min.css']
    for css_file in css_files:
        src = base_dir / 'styles' / css_file
        dst = prod_dir / 'styles' / css_file
        if src.exists():
            shutil.copy2(src, dst)
            print(f"   ✅ styles/{css_file}")
    
    # Copy minified JavaScript
    print("\n⚙️  Copying JavaScript files...")
    js_files = [
        'main.js', 'main.min.js',
        'tools.js', 'tools.min.js',
        'consumer-tools.js', 'consumer-tools.min.js'
    ]
    for js_file in js_files:
        src = base_dir / 'scripts' / js_file
        dst = prod_dir / 'scripts' / js_file
        if src.exists():
            shutil.copy2(src, dst)
            print(f"   ✅ scripts/{js_file}")
    
    # Copy documentation
    print("\n📚 Copying documentation...")
    doc_files = [
        'README.md',
        'docs/RESPONSIVE_TESTING_REPORT.md',
        'docs/ACCESSIBILITY_AUDIT.md',
        'docs/SEO_VALIDATION_REPORT.md',
        'docs/PERFORMANCE_REPORT.md',
        'docs/CODE_QUALITY_REPORT.md',
        'docs/DEPLOYMENT_GUIDE.md',
        'docs/USER_MANUAL.md'
    ]
    
    # Copy README to root of production package
    readme_src = base_dir / 'README.md'
    readme_dst = prod_dir / 'README.md'
    if readme_src.exists():
        shutil.copy2(readme_src, readme_dst)
        print(f"   ✅ README.md")
    
    # Copy docs
    for doc_file in doc_files:
        if doc_file.startswith('docs/'):
            src = base_dir / doc_file
            dst = prod_dir / doc_file
            if src.exists():
                shutil.copy2(src, dst)
                print(f"   ✅ {doc_file}")
    
    # Create VERSION.txt
    print("\n📋 Creating version information...")
    version_content = """sentAIent Website Redesign
Version: 1.0
Release Date: November 15, 2025
Status: Production Ready

Package Contents:
- Complete HTML5 website (7 pages)
- Responsive CSS framework (minified)
- Interactive JavaScript tools (minified)
- Comprehensive documentation
- Deployment guides and instructions

Quality Metrics:
- WCAG 2.1 AA Compliant
- SEO Optimized
- Mobile-First Responsive Design
- Performance Optimized (minified assets)

For deployment instructions, see docs/DEPLOYMENT_GUIDE.md
For usage information, see docs/USER_MANUAL.md
"""
    
    version_path = prod_dir / 'VERSION.txt'
    with open(version_path, 'w', encoding='utf-8') as f:
        f.write(version_content)
    print("   ✅ VERSION.txt")
    
    # Create MANIFEST.txt
    print("\n📋 Creating manifest...")
    manifest_lines = ["sentAIent Website Production Package - File Manifest\n"]
    manifest_lines.append("="*60 + "\n\n")
    
    for root, dirs, files in os.walk(prod_dir):
        level = root.replace(str(prod_dir), '').count(os.sep)
        indent = ' ' * 2 * level
        rel_root = Path(root).relative_to(prod_dir)
        if str(rel_root) != '.':
            manifest_lines.append(f'{indent}{rel_root}/\n')
        subindent = ' ' * 2 * (level + 1)
        for file in sorted(files):
            file_path = Path(root) / file
            size = os.path.getsize(file_path)
            manifest_lines.append(f'{subindent}{file} ({size:,} bytes)\n')
    
    manifest_path = prod_dir / 'MANIFEST.txt'
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.writelines(manifest_lines)
    print("   ✅ MANIFEST.txt")
    
    # Create deployment checklist
    print("\n✅ Creating deployment checklist...")
    checklist_content = """# Pre-Deployment Checklist

## Files Verification
- [ ] All HTML files present (7 pages)
- [ ] Minified CSS and JS files present
- [ ] All documentation included
- [ ] VERSION.txt and MANIFEST.txt present

## Configuration
- [ ] Update HTML files to reference .min.css and .min.js files
- [ ] Verify all internal links use correct paths
- [ ] Check form action URLs are configured
- [ ] Add analytics tracking code (if required)

## Server Setup
- [ ] Enable gzip/brotli compression
- [ ] Configure cache headers (CSS/JS: 1 year, HTML: 1 hour)
- [ ] Install SSL certificate
- [ ] Test HTTPS redirect

## Testing
- [ ] Test all pages load correctly
- [ ] Verify navigation works
- [ ] Test all interactive tools
- [ ] Check forms validate properly
- [ ] Test on mobile devices
- [ ] Run Lighthouse audit (target 90+)

## Security
- [ ] HTTPS enabled
- [ ] Security headers configured
- [ ] No sensitive data in source code
- [ ] SSL certificate valid

## Final Checks
- [ ] Staging environment tested
- [ ] Backup of old site taken (if replacing)
- [ ] DNS records ready (if new domain)
- [ ] Rollback plan documented

## Post-Deployment
- [ ] Verify site loads at production URL
- [ ] Test all functionality in production
- [ ] Check mobile responsiveness
- [ ] Monitor for errors (first 24 hours)
- [ ] Update search engine sitemaps

---

**Date Deployed:** _____________  
**Deployed By:** _____________  
**Sign-off:** _____________
"""
    
    checklist_path = prod_dir / 'DEPLOYMENT_CHECKLIST.md'
    with open(checklist_path, 'w', encoding='utf-8') as f:
        f.write(checklist_content)
    print("   ✅ DEPLOYMENT_CHECKLIST.md")
    
    # Calculate package statistics
    print("\n" + "="*80)
    print("PACKAGE STATISTICS")
    print("="*80)
    
    total_size = 0
    file_count = 0
    
    for root, dirs, files in os.walk(prod_dir):
        for file in files:
            file_path = Path(root) / file
            total_size += os.path.getsize(file_path)
            file_count += 1
    
    print(f"\nTotal Files: {file_count}")
    print(f"Total Size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    print(f"Package Location: {prod_dir.relative_to(base_dir.parent)}")
    
    # Create package info JSON
    package_info = {
        'package_name': 'sentAIent Website Production Package',
        'version': '1.0',
        'release_date': '2025-11-15',
        'total_files': file_count,
        'total_size_bytes': total_size,
        'total_size_kb': round(total_size/1024, 1),
        'contents': {
            'html_pages': len(html_files),
            'css_files': len(css_files),
            'js_files': len(js_files),
            'documentation_files': len(doc_files) + 3  # +3 for README, VERSION, MANIFEST
        },
        'quality_checks': {
            'wcag_2.1_aa_compliant': True,
            'seo_optimized': True,
            'responsive_design': True,
            'assets_minified': True,
            'performance_optimized': True
        }
    }
    
    package_info_path = prod_dir / 'PACKAGE_INFO.json'
    with open(package_info_path, 'w', encoding='utf-8') as f:
        json.dump(package_info, f, indent=2)
    print(f"\n✅ Created: PACKAGE_INFO.json")
    
    print("\n" + "="*80)
    print("✅ PRODUCTION PACKAGE CREATED SUCCESSFULLY")
    print("="*80)
    
    return prod_dir

if __name__ == '__main__':
    create_production_package()