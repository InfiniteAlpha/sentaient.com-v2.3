# Content Mapping Guide

## Overview
This document maps the original sentAIent website content to the new homepage structure, showing how information was reorganized, simplified, and enhanced.

---

## Original Content Sources

### Primary Source
- **Website**: sentaient.com (React-based SPA)
- **Research Method**: Internet search and documentation review
- **Content Extracted**: Services, team bios, company philosophy, industry applications

### Content Categories
1. Company Overview
2. Service Offerings (6 categories)
3. Team Leadership (2 members)
4. Industry Use Cases (3 industries)
5. Value Propositions
6. Calls-to-Action

---

## New Homepage Section Mapping

### 1. Hero Section
**Original Content**: Homepage hero/tagline
**New Content**:
- **Headline**: "Transform Your Business with AI That Works For You"
- **Subheadline**: "Deploy autonomous AI agents that augment your team, automate routine tasks, and deliver measurable ROI. Human augmentation, not replacement."
- **Source**: Synthesized from company philosophy and value propositions
- **Enhancement**: Clearer value communication, 3-second test optimized

### 2. Trust Signals / Metrics
**Original Content**: Scattered throughout site
**New Content**:
- 40-60% Efficiency Gain
- 24/7 AI Availability
- 3 Industry Specialties
- Measurable ROI
**Source**: Performance metrics from service descriptions
**Enhancement**: Front-loaded credibility, immediate trust building

### 3. Services Overview
**Original Content**: Service pages (separate, detailed)
**New Content**: 6 service cards with summaries

| Service | Original Location | New Location | Changes |
|---------|------------------|--------------|---------|
| Autonomous AI Agents | Services page | Card 1 | Simplified, benefit-focused |
| Generative AI Chatbots | Services page | Card 2 | Emphasized brand voice |
| Digital Marketing | Services page | Card 3 | AI-powered angle highlighted |
| AI Consulting | Services page | Card 4 | Positioned as strategy partner |
| Business Consulting | Services page | Card 5 | Operational excellence focus |
| Software Development | Services page | Card 6 | Custom solutions emphasis |

**Enhancement**: 
- Consistent card format
- Scannable summaries
- Clear CTAs to detail pages

### 4. Industry Use Cases
**Original Content**: Generic industry mentions
**New Content**: Detailed challenge-solution-outcome framework

#### Finance Industry
- **Challenges**: Manual processing, compliance, risk assessment
- **Solutions**: Automation, monitoring, fraud detection
- **Outcomes**: 60-80% time reduction, 24/7 support
- **Source**: Financial services use case examples
- **Enhancement**: Quantified benefits, specific pain points

#### Technology Industry
- **Challenges**: Development cycles, onboarding, support scaling
- **Solutions**: Code review, onboarding AI, chatbots
- **Outcomes**: Faster iterations, reduced time
- **Source**: Tech company applications
- **Enhancement**: Developer-focused language

#### Hospitality Industry
- **Challenges**: Service consistency, booking, training
- **Solutions**: AI concierge, automation, training systems
- **Outcomes**: Enhanced experience, efficiency
- **Source**: Hospitality sector examples
- **Enhancement**: Guest experience focus

### 5. Process Section
**Original Content**: Implementation details scattered
**New Content**: 4-step journey framework
1. **Discovery & Assessment** - Identify opportunities
2. **Strategy & Design** - Custom AI strategy
3. **Implementation** - Seamless deployment
4. **Optimization & Growth** - Continuous improvement

**Source**: Consulting methodology
**Enhancement**: Clear, sequential process visualization

### 6. Team Leadership
**Original Content**: Team bios (separate pages)
**New Content**: Summary cards with profiles

#### Brian Leonard - CEO
- **Original**: Full biography page
- **New**: Card with key expertise highlights
- **Focus**: AI strategy, autonomous agents, business transformation
- **Enhancement**: Digestible summary, link to full profile

#### Greg Francis - Corporate Solutions
- **Original**: Full biography page
- **New**: Card with operational excellence focus
- **Focus**: Complex concept translation, implementation
- **Enhancement**: Value proposition clear upfront

### 7. ROI Calculator
**Original Content**: Not present
**New Content**: Interactive tool
- **Inputs**: Employees, hourly cost, routine task hours
- **Output**: Estimated annual savings
- **Formula**: 50% efficiency gain assumption
- **Enhancement**: Engagement tool, lead qualification

### 8. Dual CTA Section
**Original Content**: Generic contact forms
**New Content**: Segmented CTAs

**B2B Path**:
- Headline: "Ready to Transform Your Business?"
- CTA: "Schedule Consultation"
- Target: Business decision-makers

**Consumer Path**:
- Headline: "Experience AI-Powered Apps"
- CTA: "Explore Apps"
- Target: General consumers

**Enhancement**: Clear audience segmentation, appropriate messaging

---

## Content Reorganization Principles

### 1. Inverted Pyramid
- Most important information first
- Supporting details follow
- Background/context at end

### 2. Simplified Language
**Before**: "Leverage autonomous digital employees for enterprise-grade business process automation"
**After**: "Deploy autonomous AI agents that automate business roles and augment human teams"

**Changes**:
- Removed jargon ("enterprise-grade")
- Clearer verbs ("deploy" vs "leverage")
- Benefit-focused ("augment teams")

### 3. Quantified Benefits
Added specific metrics throughout:
- 40-60% efficiency gains
- 60-80% processing time reduction
- 24/7 availability
- Measurable ROI

### 4. Audience Segmentation
Clear paths for:
- B2B prospects (consultation path)
- Consumer users (app path)
- Industry-specific visitors (use case tabs)

---

## Content Database Structure

### File: `extracted_content/structured_content.json`

```json
{
  "company_overview": { /* Company info */ },
  "services": { 
    "autonomous_ai_agents": { /* Service details */ },
    /* 5 more services */
  },
  "team": {
    "brian_leonard": { /* Bio and expertise */ },
    "greg_francis": { /* Bio and expertise */ }
  },
  "use_cases_by_industry": { /* 3 industries */ },
  "value_propositions": { /* B2B and consumer */ },
  "calls_to_action": { /* All CTA variations */ }
}
```

**Purpose**: Single source of truth for all content
**Usage**: Reference for subpage creation, updates, consistency

---

## Missing Content (To Be Created)

### High Priority
1. **Customer Testimonials**: Client success stories
2. **Case Studies**: Detailed project examples
3. **Pricing Information**: Service packages
4. **Company History**: Timeline or narrative

### Medium Priority
5. **Blog/Resources**: Thought leadership content
6. **FAQ Section**: Common questions
7. **White Papers**: In-depth guides
8. **Webinar/Demo Videos**: Visual content

### Low Priority
9. **Press/Media**: Company news
10. **Careers**: Job listings
11. **Partners**: Integration partners
12. **Legal Pages**: Privacy, terms

---

## Content Maintenance Guidelines

### Updating Services
1. Edit `structured_content.json`
2. Update homepage card if needed
3. Create/update detail page
4. Test all links

### Adding Team Members
1. Add to `structured_content.json`
2. Add card to homepage
3. Create profile page
4. Add photo asset

### Modifying Value Propositions
1. Update hero section headline
2. Adjust trust signal metrics
3. Update dual CTA messaging
4. Test 3-second clarity

---

## Content Style Guidelines

### Voice & Tone
- **Professional** yet **approachable**
- **Confident** not **arrogant**
- **Clear** over **clever**
- **Human-centric** always

### Writing Guidelines
- Use active voice
- Keep sentences under 20 words
- One idea per sentence
- Avoid jargon when possible
- Define technical terms
- Use "you" and "your"
- Focus on benefits, not features

### Formatting
- Short paragraphs (2-3 sentences)
- Bullet points for lists
- Bold for emphasis
- Headers for scanning
- White space for breathing room

---

**Document Version**: 1.0
**Last Updated**: 2025-11-15
**Status**: Complete