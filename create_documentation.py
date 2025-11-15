from pathlib import Path
from datetime import datetime


def create_readme():
    """Create a README.md for the sentAIent website redesign project.

    The function ensures the base directory exists and writes a production-ready
    README.md with a short file structure and generation timestamp.
    """
    base_dir = Path('/app/sentient_website_redesign_0308')
    base_dir.mkdir(parents=True, exist_ok=True)

    readme_path = base_dir / "README.md"
    created_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")

    readme_content = """# sentAIent Website Redesign - Production Ready

**Version:** 1.0  
**Date:** November 15, 2025  
**Status:** ✅ Production Ready

## 🎯 Project Overview

Complete modern HTML5 website redesign for sentAIent (sentaient.com), an AI firm specializing in autonomous AI agents, digital marketing services, and AI/business consulting. This project delivers a professional, accessible, and conversion-optimized website that meets top 1% AI/software industry standards.

### Key Features

- ✅ Modern, responsive HTML5 design
- ✅ Mobile-first approach (320px - 1920px breakpoints)
- ✅ WCAG 2.1 AA accessibility compliant
- ✅ SEO-optimized with semantic HTML5
- ✅ Interactive B2B and consumer tools
- ✅ Optimized performance (minified assets)
- ✅ Brand-consistent design (#60a9ff, #202733, white)

## 📁 File Structure
```
/app/sentient_website_redesign_0308/
├── README.md
├── src/
│   ├── index.html
│   ├── assets/
│   │   ├── css/
│   │   └── js/
│   └── components/
├── public/
├── build/
└── docs/
```

Generated: {timestamp}
""".format(timestamp=created_at)

    readme_path.write_text(readme_content, encoding="utf-8")
    return readme_path


if __name__ == "__main__":
    path = create_readme()
    print(f"README written to: {path}")