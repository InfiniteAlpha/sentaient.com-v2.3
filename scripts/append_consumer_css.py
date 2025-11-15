css_file = '/app/sentient_website_redesign_0308/styles/main.css'

consumer_css = """

/* =============================================================================
   CONSUMER TOOLS STYLING
   ============================================================================= */

.consumer-tools-section {
    padding: 4rem 0;
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
}

.consumer-tools-section h2 {
    text-align: center;
    font-size: 2.5rem;
    color: #202733;
    margin-bottom: 1rem;
}

.consumer-tools-section > p {
    text-align: center;
    font-size: 1.125rem;
    color: #5a6c7d;
    margin-bottom: 3rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.tools-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.tool-card {
    background: white;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
    border: 2px solid transparent;
}

.tool-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 24px rgba(96, 169, 255, 0.2);
    border-color: #60a9ff;
}

.tool-card h3 {
    color: #202733;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.tool-card p {
    color: #5a6c7d;
    margin-bottom: 1.5rem;
    line-height: 1.6;
}

.ai-demo-container,
.quiz-container,
.calculator-container,
.trial-signup-container {
    background: white;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.tool-title {
    font-size: 1.75rem;
    color: #202733;
    margin-bottom: 0.5rem;
}

.tool-subtitle {
    font-size: 1rem;
    color: #5a6c7d;
    margin-bottom: 2rem;
}

.demo-scenarios {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}

.scenario-card {
    background: linear-gradient(135deg, #60a9ff 0%, #4a8fd9 100%);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 1.5rem;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    text-align: left;
}

.scenario-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(96, 169, 255, 0.4);
}

.scenario-tags {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
}

.scenario-tags .tag {
    background: rgba(255, 255, 255, 0.2);
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
}

.demo-custom-input {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.demo-custom-input textarea {
    padding: 1rem;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-family: inherit;
    font-size: 1rem;
    resize: vertical;
}

.demo-custom-input textarea:focus {
    outline: none;
    border-color: #60a9ff;
}

.demo-response {
    background: #f8f9fa;
    border-left: 4px solid #60a9ff;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 2rem;
}

.response-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.ai-badge {
    background: #60a9ff;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 600;
}

.response-time {
    color: #5a6c7d;
    font-size: 0.875rem;
}

.response-content {
    color: #202733;
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

.response-actions {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.quiz-progress,
.trial-progress {
    background: #e0e0e0;
    height: 8px;
    border-radius: 4px;
    margin-bottom: 2rem;
    overflow: hidden;
}

.quiz-progress-bar,
.trial-progress-bar {
    background: linear-gradient(90deg, #60a9ff 0%, #4a8fd9 100%);
    height: 100%;
    transition: width 0.3s ease;
}

.quiz-progress-text,
.trial-progress-text {
    display: block;
    text-align: center;
    color: #5a6c7d;
    font-size: 0.875rem;
    margin-top: 0.5rem;
}

.quiz-options {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.quiz-option {
    background: white;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    padding: 1.25rem;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 1rem;
    text-align: left;
}

.quiz-option:hover {
    border-color: #60a9ff;
    background: #f8f9fa;
    transform: translateX(5px);
}

.quiz-results {
    background: white;
    border-radius: 12px;
    padding: 2rem;
}

.results-header {
    text-align: center;
    margin-bottom: 2rem;
}

.readiness-badge {
    display: inline-block;
    padding: 0.5rem 1.5rem;
    border-radius: 20px;
    font-weight: 600;
}

.readiness-badge.advanced {
    background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
    color: white;
}

.readiness-badge.intermediate {
    background: linear-gradient(135deg, #60a9ff 0%, #4a8fd9 100%);
    color: white;
}

.readiness-badge.beginner {
    background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
    color: white;
}

.score-circle {
    position: relative;
    width: 200px;
    height: 200px;
    margin: 0 auto;
}

.score-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.score-number {
    font-size: 3rem;
    font-weight: 700;
    color: #60a9ff;
    display: block;
}

.score-label {
    font-size: 1.5rem;
    color: #5a6c7d;
}

.results-recommendation,
.results-services {
    margin: 2rem 0;
    padding: 1.5rem;
    background: #f8f9fa;
    border-radius: 8px;
}

.results-actions,
.success-actions {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 2rem;
}

.calculator-form,
.trial-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-top: 2rem;
}

.form-group label {
    color: #202733;
    font-weight: 600;
    margin-bottom: 0.5rem;
    display: block;
}

.form-group input,
.form-group select {
    padding: 0.75rem;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-size: 1rem;
    width: 100%;
}

.form-group input:focus,
.form-group select:focus {
    outline: none;
    border-color: #60a9ff;
}

.help-text {
    font-size: 0.875rem;
    color: #5a6c7d;
    margin-top: 0.25rem;
    display: block;
}

.savings-highlight {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.savings-stat {
    background: linear-gradient(135deg, #60a9ff 0%, #4a8fd9 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
}

.stat-value {
    font-size: 2.5rem;
    font-weight: 700;
    display: block;
}

.stat-label {
    font-size: 1rem;
    opacity: 0.9;
}

.preview-message {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1.5rem 0;
}

.email-unlock-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.privacy-checkbox {
    display: flex;
    gap: 0.5rem;
    align-items: flex-start;
    font-size: 0.875rem;
}

.breakdown-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.breakdown-item {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
}

.breakdown-item.highlight {
    background: linear-gradient(135deg, #60a9ff 0%, #4a8fd9 100%);
    color: white;
}

.breakdown-label {
    display: block;
    font-size: 0.875rem;
    margin-bottom: 0.5rem;
}

.breakdown-value {
    display: block;
    font-size: 1.75rem;
    font-weight: 700;
}

.trial-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
}

.trial-option-card {
    background: white;
    border: 2px solid #e0e0e0;
    border-radius: 12px;
    padding: 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: center;
}

.trial-option-card:hover {
    border-color: #60a9ff;
    background: #f8f9fa;
    transform: translateY(-5px);
}

.option-icon {
    font-size: 2.5rem;
    display: block;
    margin-bottom: 0.5rem;
}

.option-desc {
    font-size: 0.875rem;
    color: #5a6c7d;
    display: block;
    margin-top: 0.5rem;
}

.trial-success {
    text-align: center;
    padding: 2rem;
}

.success-icon {
    font-size: 4rem;
    color: #4caf50;
    margin-bottom: 1rem;
}

.next-steps {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.next-step {
    display: flex;
    gap: 1rem;
    padding: 1.5rem;
    background: #f8f9fa;
    border-radius: 8px;
    text-align: left;
}

.step-number {
    background: #60a9ff;
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    flex-shrink: 0;
}

.email-capture-modal,
.share-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(32, 39, 51, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    padding: 1rem;
}

.share-modal-content {
    background: white;
    border-radius: 12px;
    padding: 2rem;
    max-width: 500px;
    width: 100%;
    position: relative;
}

.share-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin: 1.5rem 0;
}

.share-btn {
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-weight: 600;
    text-decoration: none;
    color: white;
    transition: transform 0.2s ease;
}

.share-btn:hover {
    transform: translateY(-2px);
}

.share-btn.twitter {
    background: #1DA1F2;
}

.share-btn.linkedin {
    background: #0077B5;
}

.share-btn.facebook {
    background: #1877F2;
}

.share-btn.copy {
    background: #5a6c7d;
}

@media (max-width: 768px) {
    .consumer-tools-section h2 {
        font-size: 1.75rem;
    }
    
    .tools-grid,
    .demo-scenarios,
    .savings-highlight,
    .breakdown-grid,
    .trial-options {
        grid-template-columns: 1fr;
    }
    
    .response-actions,
    .results-actions,
    .success-actions {
        flex-direction: column;
    }
    
    .response-actions button,
    .results-actions button,
    .success-actions button {
        width: 100%;
    }
}
"""

with open(css_file, 'a') as f:
    f.write(consumer_css)

print("Consumer tools CSS appended successfully!")