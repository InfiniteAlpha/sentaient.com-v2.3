# Quick Start Guide - sentAIent Website

## Viewing the Website

### Local Preview
Open in browser: `/app/sentient_website_redesign_0308/index.html`

### Python HTTP Server
```bash
cd /app/sentient_website_redesign_0308
python3 -m http.server 8000
```

## File Locations

**Homepage:** `index.html`

**Alternate Pages:**
- About: `pages/alternate/about_alt.html`
- Services: `pages/alternate/services_alt.html`
- Team: `pages/alternate/team_alt.html`
- History: `pages/alternate/history_alt.html`
- Contact: `pages/alternate/contact_alt.html`
- Pricing: `pages/alternate/pricing_alt.html`

**Assets:**
- CSS: `styles/main.css`
- JS: `scripts/main.js`

## Documentation

- Complete Summary: `docs/CYCLE_2_SUMMARY.md`
- Deliverables List: `CYCLE_2_DELIVERABLES.txt`
- Validation Report: `docs/cycle_2_validation.json`

## Brand Colors

- Primary Blue: `#60a9ff`
- Dark Navy: `#202733`
- White: `#ffffff`

## Validation

Run automated checks:
```bash
python validate_pages.py
```

## Status

✅ **Cycle 2 Complete** - All 7 pages validated and ready for review