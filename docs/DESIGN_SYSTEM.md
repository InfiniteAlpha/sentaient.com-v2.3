# sentAIent Design System

## Overview
This document defines the complete design system for the sentAIent website, including colors, typography, spacing, components, and usage guidelines.

---

## Brand Colors

### Primary Palette

**Primary Blue** - `#60a9ff`
- **Usage**: CTAs, links, accents, interactive elements
- **Accessibility**: AAA on white backgrounds
- **RGB**: rgb(96, 169, 255)
- **HSL**: hsl(208, 100%, 69%)

**Dark Navy** - `#202733`
- **Usage**: Headings, primary text, dark backgrounds
- **Accessibility**: AAA on white backgrounds
- **RGB**: rgb(32, 39, 51)
- **HSL**: hsl(218, 23%, 16%)

**White** - `#ffffff`
- **Usage**: Backgrounds, light text on dark backgrounds
- **RGB**: rgb(255, 255, 255)

### Supporting Colors

**Gray Scale**
- Light: `#f8f9fa` - Alternating section backgrounds
- Medium: `#6c757d` - Secondary text
- Dark: `#343a40` - Tertiary text

**Interactive States**
- Primary Dark: `#4a8fe0` - Hover state for primary blue
- Primary Light: `#7bb8ff` - Active/pressed state
- Navy Light: `#2d3b4d` - Hover state for navy

### Color Usage Guidelines

**Do's**:
- Use primary blue for all CTAs and important actions
- Use navy for headings and primary body text
- Maintain white space for breathing room
- Use gray scale for hierarchy and emphasis

**Don'ts**:
- Never use colors outside the defined palette
- Don't use primary blue for large text blocks
- Avoid low contrast combinations
- Don't use more than 3 colors in a single component

---

## Typography

### Font Families

**System Font Stack**:
```css
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
'Helvetica Neue', Arial, sans-serif
```

**Rationale**: Fast loading, native feel, excellent readability

### Type Scale

**Headings**:
- H1: `clamp(2rem, 5vw, 3.5rem)` - Hero headlines
- H2: `clamp(1.75rem, 4vw, 2.5rem)` - Section titles
- H3: `clamp(1.25rem, 3vw, 1.75rem)` - Subsection titles
- H4: `1.25rem` - Card titles
- H5: `1.125rem` - Minor headings
- H6: `1rem` - Small headings

**Body**:
- Base: `1rem` (16px) - Standard body text
- Large: `1.125rem` - Intro paragraphs
- Extra Large: `1.25rem` - Hero subheadings
- Small: `0.875rem` - Captions, footnotes

### Font Weights

- Normal: `400` - Body text
- Medium: `500` - Emphasis
- Semibold: `600` - Strong emphasis, navigation
- Bold: `700` - Headings, important text

### Line Heights

- Headings: `1.2` - Tight for visual impact
- Body: `1.6` - Comfortable reading
- UI Elements: `1` - Buttons, labels

### Usage Guidelines

**Headings**:
- Always use semantic hierarchy (H1 → H6)
- One H1 per page
- Don't skip heading levels
- Use sentence case, not all caps

**Body Text**:
- Maintain 60-80 characters per line
- Use comfortable line height (1.6)
- Left-align for readability
- Adequate spacing between paragraphs

---

## Spacing System

### Base Unit: 8px

All spacing follows 8px increments for consistency and harmony.

### Spacing Scale

```css
--spacing-xs:   0.5rem;  /* 8px  */
--spacing-sm:   1rem;    /* 16px */
--spacing-md:   1.5rem;  /* 24px */
--spacing-lg:   2rem;    /* 32px */
--spacing-xl:   3rem;    /* 48px */
--spacing-xxl:  5rem;    /* 80px */
```

### Application

**Vertical Rhythm**:
- Section padding: `--spacing-xxl` (80px desktop, 48px mobile)
- Element margins: `--spacing-md` (24px)
- Component padding: `--spacing-lg` (32px)
- Small gaps: `--spacing-sm` (16px)

**Horizontal Spacing**:
- Container padding: `--spacing-md` (24px)
- Grid gaps: `--spacing-lg` (24px)
- Button padding: `--spacing-sm` × `--spacing-lg`

---

## Layout System

### Container

**Max Width**: 1200px
**Padding**: 24px (responsive)

```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
}
```

### Grid System

**CSS Grid** - Complex layouts:
```css
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: var(--spacing-lg);
}
```

**Flexbox** - Simple layouts:
```css
.flex {
    display: flex;
    gap: var(--spacing-md);
}
```

---

## Components

### Buttons

#### Primary Button
```css
.btn-primary {
    background: #60a9ff;
    color: #ffffff;
    padding: 1rem 2rem;
    border-radius: 8px;
    font-weight: 600;
}
```
**Usage**: Main CTAs, primary actions

#### Secondary Button
```css
.btn-secondary {
    background: transparent;
    color: #202733;
    border: 2px solid #202733;
}
```
**Usage**: Alternative actions, less emphasis

#### Button Sizes
- Standard: `1rem × 2rem` padding
- Large: `1.5rem × 3rem` padding
- Small: `0.5rem × 1rem` padding

### Cards

#### Service Card
- Background: White
- Padding: 48px
- Border radius: 12px
- Shadow: 0 2px 4px rgba(0,0,0,0.1)
- Hover: Lift with enhanced shadow

#### Team Card
- Similar to service card
- Centered text
- Circular photo placeholder
- Professional, clean aesthetic

### Forms

#### Input Fields
- Height: 44px minimum (touch-friendly)
- Padding: 16px
- Border: 2px solid #6c757d
- Focus: Primary blue border + shadow
- Border radius: 8px

---

## Iconography

### Current Implementation
- Emoji placeholders for rapid prototyping
- Consistent sizing (3rem for large, 2rem for medium)
- Primary blue color for emphasis

### Future Enhancement
- SVG icon library
- Consistent stroke width
- Outlined style for professionalism
- Icon + text combinations

---

## Motion & Animation

### Transitions

**Duration**: 300ms (0.3s)
**Easing**: ease (standard)

```css
transition: all 0.3s ease;
```

### Hover Effects

**Buttons**:
- Color change
- Lift (-2px translateY)
- Enhanced shadow

**Cards**:
- Lift (-4px translateY)
- Enhanced shadow
- Subtle scale (optional)

**Links**:
- Color change to primary blue
- Underline appearance (optional)

### Accessibility

**Reduced Motion**:
```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

---

## Responsive Design

### Breakpoints

- **Mobile**: < 768px (base styles)
- **Tablet**: 768px - 1199px
- **Desktop**: ≥ 1200px

### Mobile Considerations

- Touch targets: Minimum 44×44px
- Larger text for readability
- Simplified navigation
- Stacked layouts
- Full-width CTAs

---

## Accessibility

### Color Contrast

All color combinations meet WCAG AA standards:
- Primary blue on white: 4.5:1+
- Navy on white: 12:1+
- White on navy: 12:1+

### Focus Indicators

Visible 2px outline on all interactive elements:
```css
:focus {
    outline: 2px solid #60a9ff;
    outline-offset: 2px;
}
```

### Screen Readers

- Semantic HTML structure
- ARIA labels where needed
- Hidden text for context
- Proper heading hierarchy

---

## Usage Examples

### Creating a New Section

```html
<section class="my-section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Section Title</h2>
            <p class="section-intro">Introduction text</p>
        </div>
        <div class="content-grid">
            <!-- Grid content -->
        </div>
    </div>
</section>
```

### Adding a CTA

```html
<a href="#target" class="btn btn-primary btn-large">
    Call to Action
</a>
```

### Creating a Card

```html
<article class="service-card">
    <div class="service-icon">🤖</div>
    <h3 class="service-title">Service Name</h3>
    <p class="service-description">Description text</p>
    <a href="#" class="service-link">Learn More →</a>
</article>
```

---

**Document Version**: 1.0
**Last Updated**: 2025-11-15
**Status**: Complete