import requests
from bs4 import BeautifulSoup
import json
import os
import sys
from urllib.parse import urljoin, urlparse
import time
import logging

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

class WebsiteScraper:
    def __init__(self, base_url, output_dir):
        self.base_url = base_url
        self.output_dir = output_dir
        self.visited_urls = set()
        self.content_data = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def is_valid_url(self, url):
        """Check if URL belongs to the same domain"""
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return parsed.netloc == base_parsed.netloc or parsed.netloc == ''
    
    def extract_page_content(self, url):
        """Extract structured content from a page"""
        try:
            logger.info(f"Scraping: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Remove script and style elements
            for element in soup(['script', 'style', 'noscript']):
                element.decompose()
            
            # Extract page data
            page_data = {
                'url': url,
                'title': soup.title.string if soup.title else '',
                'meta_description': '',
                'headings': {},
                'paragraphs': [],
                'links': [],
                'images': [],
                'raw_text': '',
                'html_structure': []
            }
            
            # Meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                page_data['meta_description'] = meta_desc.get('content', '')
            
            # Headings
            for i in range(1, 7):
                headings = soup.find_all(f'h{i}')
                if headings:
                    page_data['headings'][f'h{i}'] = [h.get_text(strip=True) for h in headings]
            
            # Paragraphs
            paragraphs = soup.find_all('p')
            page_data['paragraphs'] = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
            
            # Links
            links = soup.find_all('a', href=True)
            for link in links:
                href = urljoin(url, link['href'])
                link_text = link.get_text(strip=True)
                page_data['links'].append({'href': href, 'text': link_text})
            
            # Images
            images = soup.find_all('img', src=True)
            for img in images:
                src = urljoin(url, img['src'])
                alt = img.get('alt', '')
                page_data['images'].append({'src': src, 'alt': alt})
            
            # Raw text content
            page_data['raw_text'] = soup.get_text(separator='\n', strip=True)
            
            # HTML structure for main content
            main_content = soup.find('main') or soup.find('body')
            if main_content:
                for elem in main_content.find_all(['section', 'div', 'article'], recursive=False):
                    elem_class = ' '.join(elem.get('class', []))
                    elem_id = elem.get('id', '')
                    page_data['html_structure'].append({
                        'tag': elem.name,
                        'class': elem_class,
                        'id': elem_id,
                        'text_preview': elem.get_text(strip=True)[:200]
                    })
            
            return page_data
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            return None
    
    def crawl(self, start_url, max_pages=20):
        """Crawl the website starting from start_url"""
        to_visit = [start_url]
        
        while to_visit and len(self.visited_urls) < max_pages:
            url = to_visit.pop(0)
            
            if url in self.visited_urls:
                continue
            
            if not self.is_valid_url(url):
                continue
            
            # Skip non-HTML resources
            if any(url.lower().endswith(ext) for ext in ['.pdf', '.jpg', '.png', '.gif', '.css', '.js']):
                continue
            
            self.visited_urls.add(url)
            page_data = self.extract_page_content(url)
            
            if page_data:
                # Create safe filename
                path = urlparse(url).path
                filename = path.strip('/').replace('/', '_') or 'homepage'
                self.content_data[filename] = page_data
                
                # Find new links to visit
                for link in page_data['links']:
                    href = link['href']
                    if href not in self.visited_urls and self.is_valid_url(href):
                        # Only follow internal links
                        if href.startswith(self.base_url) or href.startswith('/'):
                            to_visit.append(href)
            
            time.sleep(1)  # Rate limiting
        
        logger.info(f"Crawled {len(self.visited_urls)} pages")
    
    def save_content(self):
        """Save extracted content to JSON files"""
        os.makedirs(self.output_dir, exist_ok=True)
        
        for filename, data in self.content_data.items():
            output_path = os.path.join(self.output_dir, f"{filename}.json")
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Saved: {output_path}")
        
        # Save summary
        summary = {
            'total_pages': len(self.content_data),
            'pages': list(self.content_data.keys()),
            'base_url': self.base_url,
            'extraction_date': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        summary_path = os.path.join(self.output_dir, '_summary.json')
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        logger.info(f"Content extraction complete. {len(self.content_data)} pages saved.")

if __name__ == '__main__':
    base_url = 'https://www.sentaient.com'
    output_dir = '/app/sentient_website_redesign_0308/extracted_content'
    
    scraper = WebsiteScraper(base_url, output_dir)
    scraper.crawl(base_url)
    scraper.save_content()
    
    print("\n=== EXTRACTION SUMMARY ===")
    print(f"Pages extracted: {len(scraper.content_data)}")
    print(f"Output directory: {output_dir}")
    print("\nExtracted pages:")
    for page in scraper.content_data.keys():
        print(f"  - {page}")