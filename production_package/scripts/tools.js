class InteractiveTools {
    constructor() {
        this.initializeROICalculator();
        this.initializePricingCalculator();
        this.initializeConsultationForm();
        this.initializeServiceSelector();
    }

    initializeROICalculator() {
        const form = document.getElementById('roi-calculator-form');
        if (!form) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.calculateROI();
        });

        const inputs = form.querySelectorAll('input');
        inputs.forEach(input => {
            input.addEventListener('input', () => this.validateROIInput(input));
        });
    }

    validateROIInput(input) {
        const value = parseFloat(input.value);
        const errorSpan = input.parentElement.querySelector('.error-message');
        
        if (input.value === '') {
            if (errorSpan) errorSpan.textContent = '';
            input.classList.remove('error', 'valid');
            return false;
        }

        if (isNaN(value) || value < 0) {
            if (errorSpan) errorSpan.textContent = 'Please enter a valid positive number';
            input.classList.add('error');
            input.classList.remove('valid');
            return false;
        }

        if (errorSpan) errorSpan.textContent = '';
        input.classList.remove('error');
        input.classList.add('valid');
        return true;
    }

    calculateROI() {
        const currentCosts = parseFloat(document.getElementById('current-costs').value);
        const projectedSavings = parseFloat(document.getElementById('projected-savings').value);
        const implementationCost = parseFloat(document.getElementById('implementation-cost').value);
        const timeline = parseFloat(document.getElementById('implementation-timeline').value);

        if (isNaN(currentCosts) || isNaN(projectedSavings) || isNaN(implementationCost) || isNaN(timeline)) {
            this.showMessage('roi-results', 'Please fill in all fields with valid numbers', 'error');
            return;
        }

        const annualSavings = projectedSavings * 12;
        const roi = ((annualSavings - implementationCost) / implementationCost) * 100;
        const paybackMonths = implementationCost / projectedSavings;
        const threeYearValue = (annualSavings * 3) - implementationCost;

        const resultsDiv = document.getElementById('roi-results');
        resultsDiv.innerHTML = `
            <div class="roi-results-content">
                <h3>Your ROI Analysis</h3>
                <div class="roi-metrics">
                    <div class="metric">
                        <span class="metric-label">Annual Savings</span>
                        <span class="metric-value">$${annualSavings.toLocaleString()}</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">ROI (Year 1)</span>
                        <span class="metric-value ${roi > 0 ? 'positive' : 'negative'}">${roi.toFixed(1)}%</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">Payback Period</span>
                        <span class="metric-value">${paybackMonths.toFixed(1)} months</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">3-Year Value</span>
                        <span class="metric-value">$${threeYearValue.toLocaleString()}</span>
                    </div>
                </div>
                <div class="roi-recommendation">
                    ${roi > 100 ? '<p class="recommendation-text positive">Excellent ROI! This investment could deliver significant returns.</p>' : 
                      roi > 50 ? '<p class="recommendation-text positive">Strong ROI potential for your business.</p>' : 
                      roi > 0 ? '<p class="recommendation-text neutral">Positive ROI with steady long-term value.</p>' : 
                      '<p class="recommendation-text negative">Consider optimizing scope to improve ROI.</p>'}
                </div>
                <button class="btn btn-primary" onclick="document.getElementById('consultation-modal').style.display='flex'">
                    Schedule Consultation
                </button>
            </div>
        `;
        resultsDiv.classList.add('visible');
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    initializePricingCalculator() {
        const form = document.getElementById('pricing-calculator-form');
        if (!form) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.calculatePricing();
        });

        const serviceSelect = document.getElementById('service-type');
        if (serviceSelect) {
            serviceSelect.addEventListener('change', () => this.updatePricingOptions());
        }
    }

    updatePricingOptions() {
        const serviceType = document.getElementById('service-type').value;
        const scopeSelect = document.getElementById('project-scope');
        
        const scopeOptions = {
            'ai-agents': ['Basic Automation (1-2 processes)', 'Standard Implementation (3-5 processes)', 'Enterprise Solution (6+ processes)', 'Custom Development'],
            'digital-marketing': ['Starter Package', 'Growth Package', 'Enterprise Package', 'Custom Strategy'],
            'ai-consulting': ['Single Session', 'Monthly Retainer', 'Quarterly Program', 'Annual Partnership'],
            'business-consulting': ['Strategy Session', 'Implementation Support', 'Ongoing Advisory', 'Transformation Program'],
            'custom-software': ['MVP Development', 'Full Application', 'Enterprise Platform', 'Custom Solution']
        };

        if (scopeSelect && scopeOptions[serviceType]) {
            scopeSelect.innerHTML = '<option value="">Select project scope...</option>' +
                scopeOptions[serviceType].map(opt => `<option value="${opt}">${opt}</option>`).join('');
        }
    }

    calculatePricing() {
        const serviceType = document.getElementById('service-type').value;
        const projectScope = document.getElementById('project-scope').value;
        const teamSize = document.getElementById('team-size').value;
        const timeline = document.getElementById('project-timeline').value;

        if (!serviceType || !projectScope || !teamSize || !timeline) {
            this.showMessage('pricing-results', 'Please complete all fields', 'error');
            return;
        }

        const basePrices = {
            'ai-agents': { min: 15000, max: 150000 },
            'digital-marketing': { min: 2000, max: 25000 },
            'ai-consulting': { min: 5000, max: 50000 },
            'business-consulting': { min: 8000, max: 75000 },
            'custom-software': { min: 25000, max: 250000 }
        };

        const scopeMultipliers = {
            0: 0.4, 1: 0.7, 2: 1.0, 3: 1.5
        };

        const teamMultipliers = {
            '1-10': 1.0, '11-50': 1.3, '51-200': 1.6, '200+': 2.0
        };

        const timelineMultipliers = {
            '1-3': 1.2, '3-6': 1.0, '6-12': 0.9, '12+': 0.85
        };

        const base = basePrices[serviceType];
        const scopeIndex = document.getElementById('project-scope').selectedIndex - 1;
        const scopeMult = scopeMultipliers[scopeIndex] || 1.0;
        const teamMult = teamMultipliers[teamSize] || 1.0;
        const timeMult = timelineMultipliers[timeline] || 1.0;

        const estimatedMin = Math.round((base.min * scopeMult * teamMult * timeMult) / 1000) * 1000;
        const estimatedMax = Math.round((base.max * scopeMult * teamMult * timeMult) / 1000) * 1000;

        const resultsDiv = document.getElementById('pricing-results');
        resultsDiv.innerHTML = `
            <div class="pricing-results-content">
                <h3>Estimated Investment Range</h3>
                <div class="price-range">
                    <span class="price-amount">$${estimatedMin.toLocaleString()} - $${estimatedMax.toLocaleString()}</span>
                </div>
                <div class="pricing-details">
                    <p><strong>Service:</strong> ${this.formatServiceName(serviceType)}</p>
                    <p><strong>Scope:</strong> ${projectScope}</p>
                    <p><strong>Team Size:</strong> ${teamSize} employees</p>
                    <p><strong>Timeline:</strong> ${timeline} months</p>
                </div>
                <div class="pricing-note">
                    <p>This is a preliminary estimate. Actual pricing depends on specific requirements, complexity, and customization needs.</p>
                </div>
                <button class="btn btn-primary" onclick="document.getElementById('consultation-modal').style.display='flex'">
                    Get Detailed Quote
                </button>
            </div>
        `;
        resultsDiv.classList.add('visible');
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    formatServiceName(service) {
        const names = {
            'ai-agents': 'AI Agents',
            'digital-marketing': 'Digital Marketing',
            'ai-consulting': 'AI Consulting',
            'business-consulting': 'Business Consulting',
            'custom-software': 'Custom Software Development'
        };
        return names[service] || service;
    }

    initializeConsultationForm() {
        const form = document.getElementById('consultation-form');
        if (!form) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.submitConsultation();
        });

        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('blur', () => this.validateConsultationField(input));
            input.addEventListener('input', () => {
                if (input.classList.contains('error')) {
                    this.validateConsultationField(input);
                }
            });
        });
    }

    validateConsultationField(field) {
        const errorSpan = field.parentElement.querySelector('.error-message');
        let isValid = true;
        let errorMessage = '';

        if (field.hasAttribute('required') && !field.value.trim()) {
            isValid = false;
            errorMessage = 'This field is required';
        } else if (field.type === 'email' && field.value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(field.value)) {
                isValid = false;
                errorMessage = 'Please enter a valid email address';
            }
        } else if (field.id === 'phone' && field.value) {
            const phoneRegex = /^[\d\s\-\+\(\)]+$/;
            if (!phoneRegex.test(field.value) || field.value.replace(/\D/g, '').length < 10) {
                isValid = false;
                errorMessage = 'Please enter a valid phone number';
            }
        }

        if (errorSpan) {
            errorSpan.textContent = errorMessage;
        }

        if (isValid) {
            field.classList.remove('error');
            field.classList.add('valid');
        } else {
            field.classList.add('error');
            field.classList.remove('valid');
        }

        return isValid;
    }

    submitConsultation() {
        const form = document.getElementById('consultation-form');
        const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
        let isValid = true;

        inputs.forEach(input => {
            if (!this.validateConsultationField(input)) {
                isValid = false;
            }
        });

        if (!isValid) {
            this.showMessage('consultation-feedback', 'Please correct the errors above', 'error');
            return;
        }

        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner"></span> Submitting...';

        setTimeout(() => {
            const formData = {
                name: document.getElementById('consultation-name').value,
                email: document.getElementById('consultation-email').value,
                company: document.getElementById('consultation-company').value,
                phone: document.getElementById('phone').value,
                industry: document.getElementById('industry').value,
                challenge: document.getElementById('challenge').value,
                contactMethod: document.getElementById('contact-method').value,
                timestamp: new Date().toISOString()
            };

            

            this.showMessage('consultation-feedback', 
                'Thank you! We\'ll contact you within 24 hours to schedule your consultation.', 
                'success');
            
            form.reset();
            inputs.forEach(input => input.classList.remove('valid', 'error'));
            submitBtn.disabled = false;
            submitBtn.innerHTML = 'Request Consultation';

            setTimeout(() => {
                const modal = document.getElementById('consultation-modal');
                if (modal) modal.style.display = 'none';
            }, 3000);
        }, 1500);
    }

    initializeServiceSelector() {
        const form = document.getElementById('service-selector-form');
        if (!form) return;

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.findServices();
        });
    }

    findServices() {
        const industry = document.getElementById('selector-industry').value;
        const useCase = document.getElementById('use-case').value;
        const budget = document.getElementById('budget-range').value;

        if (!industry || !useCase) {
            this.showMessage('service-results', 'Please select both industry and use case', 'error');
            return;
        }

        const serviceRecommendations = this.getServiceRecommendations(industry, useCase, budget);
        
        const resultsDiv = document.getElementById('service-results');
        resultsDiv.innerHTML = `
            <div class="service-results-content">
                <h3>Recommended Solutions for ${this.formatIndustryName(industry)}</h3>
                <div class="recommended-services">
                    ${serviceRecommendations.map(service => `
                        <div class="service-card">
                            <h4>${service.name}</h4>
                            <p class="service-description">${service.description}</p>
                            <div class="service-benefits">
                                <strong>Key Benefits:</strong>
                                <ul>
                                    ${service.benefits.map(b => `<li>${b}</li>`).join('')}
                                </ul>
                            </div>
                            <div class="service-fit">
                                <span class="fit-score">Match: ${service.fitScore}%</span>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <button class="btn btn-primary" onclick="document.getElementById('consultation-modal').style.display='flex'">
                    Discuss Your Project
                </button>
            </div>
        `;
        resultsDiv.classList.add('visible');
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    getServiceRecommendations(industry, useCase, budget) {
        const recommendations = {
            'finance': {
                'automation': [
                    { name: 'AI Agents for Financial Processing', description: 'Automate invoice processing, expense tracking, and financial reporting with intelligent agents.', benefits: ['Reduce processing time by 80%', 'Minimize human error', '24/7 automated operations'], fitScore: 95 },
                    { name: 'Custom Financial Software', description: 'Tailored solutions for your specific financial workflows and compliance needs.', benefits: ['Industry-specific compliance', 'Seamless integration', 'Scalable architecture'], fitScore: 85 }
                ],
                'analysis': [
                    { name: 'AI Consulting for Financial Analytics', description: 'Implement AI-driven analytics for better financial insights and forecasting.', benefits: ['Predictive analytics', 'Risk assessment', 'Market trend analysis'], fitScore: 90 },
                    { name: 'Business Intelligence Solutions', description: 'Custom dashboards and reporting for financial decision-making.', benefits: ['Real-time insights', 'Custom metrics', 'Executive reporting'], fitScore: 85 }
                ],
                'customer-service': [
                    { name: 'AI Chatbots for Financial Services', description: 'Intelligent customer service agents handling account queries and transactions.', benefits: ['24/7 availability', 'Multi-language support', 'Secure transactions'], fitScore: 88 }
                ]
            },
            'technology': {
                'automation': [
                    { name: 'DevOps AI Agents', description: 'Automate deployment, monitoring, and incident response with AI-powered agents.', benefits: ['Faster deployments', 'Proactive monitoring', 'Reduced downtime'], fitScore: 92 },
                    { name: 'Custom Development Tools', description: 'Build internal tools and automation for your engineering team.', benefits: ['Increased productivity', 'Reduced manual work', 'Better code quality'], fitScore: 87 }
                ],
                'product-development': [
                    { name: 'AI-Enhanced Product Features', description: 'Integrate AI capabilities into your existing products.', benefits: ['Competitive advantage', 'Enhanced user experience', 'Data-driven insights'], fitScore: 90 },
                    { name: 'MVP Development Services', description: 'Rapidly build and test AI-powered product concepts.', benefits: ['Fast time-to-market', 'Validated learning', 'Scalable foundation'], fitScore: 85 }
                ]
            },
            'hospitality': {
                'customer-service': [
                    { name: 'AI Concierge Services', description: 'Intelligent booking and customer service automation for hotels and restaurants.', benefits: ['Improved guest experience', 'Reduced staff workload', 'Multi-channel support'], fitScore: 93 },
                    { name: 'Digital Marketing for Hospitality', description: 'Targeted campaigns to attract and retain customers.', benefits: ['Increased bookings', 'Better customer insights', 'ROI tracking'], fitScore: 88 }
                ],
                'operations': [
                    { name: 'Operations Management AI', description: 'Optimize staffing, inventory, and resource allocation with AI.', benefits: ['Cost reduction', 'Better forecasting', 'Operational efficiency'], fitScore: 86 }
                ]
            },
            'retail': {
                'customer-service': [
                    { name: 'E-commerce AI Assistants', description: 'Personalized shopping experiences and customer support automation.', benefits: ['Higher conversion rates', 'Reduced cart abandonment', 'Better recommendations'], fitScore: 91 }
                ],
                'marketing': [
                    { name: 'Digital Marketing Solutions', description: 'AI-driven campaigns for customer acquisition and retention.', benefits: ['Targeted advertising', 'Customer segmentation', 'Performance analytics'], fitScore: 89 }
                ]
            },
            'healthcare': {
                'automation': [
                    { name: 'Healthcare Administration AI', description: 'Automate scheduling, billing, and patient communications.', benefits: ['HIPAA compliant', 'Reduced admin burden', 'Better patient experience'], fitScore: 87 }
                ],
                'analysis': [
                    { name: 'Healthcare Analytics Consulting', description: 'Data-driven insights for operational and clinical improvements.', benefits: ['Quality improvement', 'Cost optimization', 'Compliance reporting'], fitScore: 85 }
                ]
            }
        };

        const industryRecs = recommendations[industry] || {};
        const useCaseRecs = industryRecs[useCase] || [];
        
        if (useCaseRecs.length === 0) {
            return [
                { name: 'Custom AI Solution', description: 'We\'ll design a tailored solution for your specific needs.', benefits: ['Personalized approach', 'Industry expertise', 'Scalable implementation'], fitScore: 80 },
                { name: 'Consultation Session', description: 'Explore possibilities with our AI experts.', benefits: ['Expert guidance', 'Strategic planning', 'Technology recommendations'], fitScore: 75 }
            ];
        }

        return useCaseRecs;
    }

    formatIndustryName(industry) {
        const names = {
            'finance': 'Finance',
            'technology': 'Technology',
            'hospitality': 'Hospitality',
            'retail': 'Retail',
            'healthcare': 'Healthcare',
            'manufacturing': 'Manufacturing',
            'education': 'Education',
            'other': 'Your Industry'
        };
        return names[industry] || industry;
    }

    showMessage(elementId, message, type) {
        const element = document.getElementById(elementId);
        if (!element) return;

        element.innerHTML = `<div class="message ${type}">${message}</div>`;
        element.classList.add('visible');

        if (type === 'success') {
            setTimeout(() => {
                element.classList.remove('visible');
            }, 5000);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new InteractiveTools();

    const modal = document.getElementById('consultation-modal');
    if (modal) {
        const closeBtn = modal.querySelector('.modal-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                modal.style.display = 'none';
            });
        }

        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });
    }
});