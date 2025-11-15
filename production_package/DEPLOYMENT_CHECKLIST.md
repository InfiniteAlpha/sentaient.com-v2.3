# Pre-Deployment Checklist

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
