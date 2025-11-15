import json
import os

# Load structured content
with open('/app/sentient_website_redesign_0308/extracted_content/structured_content.json', 'r') as f:
    content = json.load(f)

report = """# sentAIent Website Content Analysis Report

## Executive Summary
Analysis of sentAIent.com reveals a React-based SPA focused on AI agents and digital solutions. The company positions itself as a human-centric AI provider with expertise in autonomous agents, chatbots, and business transformation.

## Current Site Structure Analysis

### Company Identity
- **Name**: sentAIent (note the unique capitalization)
- **Core Philosophy**: Human augmentation, not replacement
- **Market Position**: Top 1% AI/software industry standards
- **Ethical Foundation**: Transparency, fairness, privacy, accountability

### Service Portfolio (6 Core Offerings)
1. **Autonomous AI Agents** - Digital employees for process automation
2. **Generative AI Chatbots** - 24/7 customer engagement with brand voice
3. **Digital Marketing Services** - AI-powered marketing solutions
4. **AI & Automation Consulting** - Strategy and implementation guidance
5. **Business Consulting** - Operational excellence transformation
6. **Custom Software Development** - Tailored application solutions

### Target Markets
**Primary (B2B):**
- Small to mid-sized businesses
- Industries: Finance, Technology, Hospitality
- Decision-makers: Technical and non-technical business owners

**Secondary (B2C):**
- General consumers seeking AI applications
- Viral-potential app users

### Team Leadership
**Brian Leonard** - CEO, AI Strategy & Innovation
- Focus: Autonomous agent development, AI implementation strategy
- Expertise: Business transformation through AI, product vision

**Greg Francis** - Corporate Solutions, Operational Excellence
- Focus: Translating complex AI concepts to practical implementation
- Expertise: Corporate solution deployment, process optimization

## Content Themes & Messaging

### Primary Value Propositions
1. **Efficiency**: 40-60% improvement through intelligent automation
2. **Scalability**: Growth without proportional cost increases
3. **ROI Focus**: Measurable impact with clear metrics
4. **Human-Centric**: AI augments rather than replaces teams

### Industry-Specific Use Cases

**Finance:**
- Document processing automation (60-80% time reduction)
- Compliance monitoring and reporting
- Fraud detection and risk assessment
- 24/7 customer account support

**Technology:**
- Product development acceleration
- Technical support automation
- Onboarding assistance
- Competitive intelligence

**Hospitality:**
- AI concierge services
- Booking management automation
- Staff training systems
- Personalized marketing

## Design & UX Observations

### Brand Colors (Strict Requirements)
- Primary Blue: #60a9ff
- Dark Navy: #202733
- Background: White (#ffffff)

### Current Technology Stack
- React-based single page application
- Client-side rendering (CSR)
- Modern JavaScript framework

## Content Gaps & Opportunities

### Strengths
- Clear service differentiation
- Strong ethical positioning
- Industry-specific examples
- Leadership expertise highlighted

### Improvements Needed
1. **Immediate Value Communication**: Need 3-second clarity on homepage
2. **Simplified Messaging**: Make AI accessible to non-technical audiences
3. **Visual Hierarchy**: Better guide users to key actions
4. **Interactive Tools**: Add ROI calculators, service selectors
5. **Social Proof**: Include testimonials, case studies, metrics
6. **Consumer Path**: Clear separation of B2B and B2C journeys

## Recommendations for New Homepage

### Section Priority Order
1. **Hero** - Immediate value proposition (3-second test)
2. **Trust Signals** - Brief metrics/social proof
3. **Services Overview** - 6 core offerings with icons
4. **Use Cases** - Industry-specific scenarios
5. **How It Works** - Simple 3-4 step process
6. **Team Excellence** - Leadership credibility
7. **Interactive Tools** - ROI calculator or assessment
8. **Dual CTAs** - B2B consultation + Consumer app access

### Content Strategy
- **Headline**: Focus on transformation, not technology
- **Subheadings**: Quantify benefits (efficiency %, time saved)
- **Body Copy**: Accessible language, avoid jargon overload
- **CTAs**: Action-oriented, value-focused

### Information Architecture
"""