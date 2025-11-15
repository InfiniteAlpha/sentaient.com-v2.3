# Deployment Guide

**Document Version:** 1.0  
**Last Updated:** November 15, 2025

## 📋 Pre-Deployment Checklist

### Files & Assets
- [x] All HTML files use minified CSS/JS references
- [x] Minified assets present in `/styles` and `/scripts`
- [x] No test files included in production package
- [x] File permissions set correctly

### Configuration
- [ ] Update contact form action URLs (if applicable)
- [ ] Configure analytics tracking code (if required)
- [ ] Set correct domain in meta tags and links
- [ ] Verify all internal links use correct paths

## 🖥 Hosting Requirements

### Minimum Server Specifications
- **Web Server:** Apache 2.4+ or Nginx 1.18+
- **Storage:** 5MB minimum (10MB recommended)
- **No database required**
- **No server-side processing needed**

### Recommended Hosting Providers

**Static Hosting (Recommended):**
- **Netlify** - Free tier, automatic CDN
- **Vercel** - Excellent performance, free SSL
- **Cloudflare Pages** - Global CDN, DDoS protection

## 🚀 Deployment Methods

### Method 1: Netlify (Easiest)

1. Create account at https://netlify.com
2. Click "Add new site" > "Deploy manually"
3. Drag and drop `production_package` folder
4. Configure custom domain
5. HTTPS enabled automatically

### Method 2: Traditional cPanel Hosting

1. Access cPanel file manager
2. Navigate to `public_html`
3. Upload all files from `production_package`
4. Set file permissions (644 files, 755 directories)
5. Install SSL certificate (Let's Encrypt)

### .htaccess Configuration:
```apache
# Enable compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript
</IfModule>

# Browser caching
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType text/html "access plus 1 hour"
</IfModule>

# Force HTTPS
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>
```

## ⚙️ Configuration Steps

### Update Asset References

Change HTML files to use minified assets:

**In `<head>` sections:**
```html
<link rel="stylesheet" href="styles/main.min.css">
```

**Before `</body>`:**
```html
<script src="scripts/main.min.js"></script>
<script src="scripts/tools.min.js"></script>
<script src="scripts/consumer-tools.min.js"></script>
```

## ✅ Testing Procedures

### Post-Deployment Checklist
- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Interactive tools function
- [ ] Forms validate properly
- [ ] Mobile menu works
- [ ] HTTPS enabled
- [ ] Run Lighthouse audit (target 90+)

## 📊 Monitoring & Maintenance

### Uptime Monitoring
Recommended: UptimeRobot (free, 5-minute checks)

### Regular Maintenance
- **Weekly:** Check uptime status
- **Monthly:** Review performance metrics
- **Quarterly:** Update browser compatibility testing

## 🔧 Troubleshooting

### Common Issues

**Issue: Styles not loading**
- Check file paths in HTML
- Verify browser console for 404 errors

**Issue: JavaScript not working**
- Check browser console for errors
- Test with unminified versions for debugging

**Issue: Slow page load**
- Enable gzip/brotli compression
- Verify minified assets used

## 🎯 Success Criteria

✅ All pages load correctly  
✅ HTTPS enabled and working  
✅ Lighthouse score 90+ on all metrics  
✅ Responsive design works on all devices  
✅ All interactive features functional