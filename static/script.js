document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('upload-form');
    const fileInput = document.getElementById('pdf-file');
    const fileName = document.getElementById('file-name');
    const loading = document.getElementById('loading');
    const resultSection = document.getElementById('result-section');
    const summaryContent = document.getElementById('summary-content');
    const readingTime = document.getElementById('reading-time');
    const languageInfo = document.getElementById('language-info');
    const topicsContainer = document.getElementById('topics-container');
    const keywordsContainer = document.getElementById('keywords-container');
    const qualityMetrics = document.getElementById('quality-metrics');
    const saveBtn = document.getElementById('save-btn');
    const summariesList = document.getElementById('summaries-list');
    
    // Update file name when file is selected
    fileInput.addEventListener('change', function() {
        if (this.files.length > 0) {
            fileName.textContent = this.files[0].name;
        } else {
            fileName.textContent = 'No file selected';
        }
    });
    
    // Handle form submission
    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (!fileInput.files.length) {
            alert('Please select a PDF file');
            return;
        }
        
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        
        // Get selected length
        const lengthOptions = document.getElementsByName('length');
        let selectedLength;
        for (const option of lengthOptions) {
            if (option.checked) {
                selectedLength = option.value;
                break;
            }
        }
        formData.append('length', selectedLength);
        
        // Get target language if selected
        const targetLanguage = document.getElementById('target-language').value;
        if (targetLanguage) {
            formData.append('target_language', targetLanguage);
        }
        
        // Show loading spinner
        loading.style.display = 'flex';
        
        // Add auto_save parameter (set to false)
        formData.append('auto_save', 'false');
        
        // Send request to server
        fetch('/summarize', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Hide loading spinner
            loading.style.display = 'none';
            
            // Store current summary data for later saving
            currentSummaryData = data;
            currentSummaryId = data.summary_id;
            
            // Display summary
            summaryContent.textContent = data.summary;
            readingTime.textContent = `Reading time: ${data.reading_time} min`;
            
            // Display language info
            const langName = getLanguageName(data.language);
            const confidence = data.language_confidence >= 0 ? Math.round(data.language_confidence * 100) : 80;
            languageInfo.textContent = `Language: ${langName} (${confidence}% confidence)`;
            
            // Display topics
            displayTopics(data.topics);
            
            // Display keywords
            displayKeywords(data.keywords);
            
            // Display quality metrics
            displayQualityMetrics(data.quality_metrics);
            
            // Show result section
            resultSection.style.display = 'block';
            
            // Scroll to result section
            resultSection.scrollIntoView({ behavior: 'smooth' });
            
            // Update save button text based on whether it was auto-saved
            saveBtn.textContent = data.saved ? 'Already Saved' : 'Save Summary';
            saveBtn.disabled = data.saved;
        })
        .catch(error => {
            loading.style.display = 'none';
            alert('Error generating summary: ' + error.message);
        });
    });
    
    // Display topics
    function displayTopics(topics) {
        topicsContainer.innerHTML = '';
        
        if (!topics || topics.length === 0) {
            topicsContainer.innerHTML = '<p>No topics identified</p>';
            return;
        }
        
        topics.forEach(topic => {
            const topicItem = document.createElement('div');
            topicItem.className = 'topic-item';
            
            const topicTitle = document.createElement('div');
            topicTitle.className = 'topic-title';
            topicTitle.textContent = topic.topic;
            
            const topicTerms = document.createElement('div');
            topicTerms.className = 'topic-terms';
            
            // Filter out any empty or excessively long terms
            const filteredTerms = topic.terms.filter(term => term && typeof term === 'string' && term.length < 30);
            
            filteredTerms.forEach(term => {
                const termTag = document.createElement('span');
                termTag.className = 'term-tag';
                
                // Clean up the term text
                let cleanedTerm = term;
                
                // Add spaces between lowercase and uppercase letters
                cleanedTerm = cleanedTerm.replace(/([a-z])([A-Z])/g, '$1 $2');
                
                // Remove any excessive whitespace
                cleanedTerm = cleanedTerm.replace(/\s{2,}/g, ' ').trim();
                
                termTag.textContent = cleanedTerm;
                topicTerms.appendChild(termTag);
            });
            
            topicItem.appendChild(topicTitle);
            topicItem.appendChild(topicTerms);
            topicsContainer.appendChild(topicItem);
        });
    }
    
    // Display keywords
    function displayKeywords(keywords) {
        keywordsContainer.innerHTML = '';
        
        if (!keywords || keywords.length === 0) {
            keywordsContainer.innerHTML = '<p>No keywords identified</p>';
            return;
        }
        
        // Filter out any excessively long keywords (likely errors)
        const filteredKeywords = keywords.filter(k => k.term && k.term.length < 30);
        
        // Display keywords as individual tags with proper styling
        filteredKeywords.slice(0, 20).forEach(keyword => {
            const keywordTag = document.createElement('span');
            keywordTag.className = 'keyword-tag';
            
            // Clean up the keyword text
            let term = keyword.term;
            
            // Add spaces between lowercase and uppercase letters
            term = term.replace(/([a-z])([A-Z])/g, '$1 $2');
            
            // Remove any excessive whitespace
            term = term.replace(/\s{2,}/g, ' ').trim();
            
            keywordTag.textContent = term;
            keywordsContainer.appendChild(keywordTag);
        });
    }
    
    // Display quality metrics
    function displayQualityMetrics(metrics) {
        qualityMetrics.innerHTML = '';
        
        if (!metrics) {
            qualityMetrics.innerHTML = '<p>No quality metrics available</p>';
            return;
        }
        
        const metricLabels = {
            'compression_ratio': 'Compression',
            'information_density': 'Information Density',
            'coherence_score': 'Coherence',
            'overall_quality': 'Overall Quality'
        };
        
        for (const [key, value] of Object.entries(metrics)) {
            const metricItem = document.createElement('div');
            metricItem.className = 'metric-item';
            
            const metricLabel = document.createElement('span');
            metricLabel.className = 'metric-label';
            metricLabel.textContent = metricLabels[key] || key;
            
            const metricValue = document.createElement('span');
            metricValue.className = 'metric-value';
            
            // Format the value as a percentage for better readability
            if (key === 'compression_ratio') {
                metricValue.textContent = `${Math.round(value * 100)}%`;
            } else {
                metricValue.textContent = `${Math.round(value * 100)}%`;
            }
            
            metricItem.appendChild(metricLabel);
            metricItem.appendChild(metricValue);
            qualityMetrics.appendChild(metricItem);
        }
    }
    
    // Get language name from code
    function getLanguageName(code) {
        const languages = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'nl': 'Dutch',
            'ru': 'Russian',
            'zh': 'Chinese',
            'ja': 'Japanese',
            'ko': 'Korean',
            'ar': 'Arabic',
            'hi': 'Hindi'
        };
        
        return languages[code] || code;
    }
    
    // Load saved summaries
    function loadSummaries() {
        fetch('/summaries')
            .then(response => response.json())
            .then(data => {
                summariesList.innerHTML = '';
                
                if (data.length === 0) {
                    summariesList.innerHTML = '<p>No saved summaries yet</p>';
                    return;
                }
                
                data.forEach(summary => {
                    const summaryItem = document.createElement('div');
                    summaryItem.className = 'summary-item';
                    
                    // Create summary content
                    const summaryContent = document.createElement('div');
                    summaryContent.className = 'summary-content-item';
                    summaryContent.innerHTML = `
                        <h3>${summary.title}</h3>
                        <p class="summary-meta">Reading time: ${summary.reading_time} min</p>
                    `;
                    
                    // Create delete button
                    const deleteBtn = document.createElement('button');
                    deleteBtn.className = 'delete-btn';
                    deleteBtn.textContent = 'Delete';
                    deleteBtn.addEventListener('click', function(e) {
                        e.stopPropagation(); // Prevent triggering the parent click
                        
                        if (confirm('Are you sure you want to delete this summary?')) {
                            fetch(`/summaries/${summary.id}`, {
                                method: 'DELETE'
                            })
                            .then(response => response.json())
                            .then(data => {
                                alert('Summary deleted successfully');
                                loadSummaries(); // Refresh the list
                            })
                            .catch(error => {
                                alert('Error deleting summary: ' + error.message);
                            });
                        }
                    });
                    
                    // Add click event to view the summary
                    summaryContent.addEventListener('click', function() {
                        fetch(`/summaries/${summary.id}`)
                            .then(response => response.json())
                            .then(data => {
                                // Store current summary data
                                currentSummaryData = data;
                                currentSummaryId = data.id;
                                
                                // Display summary
                                summaryContent.textContent = data.content;
                                readingTime.textContent = `Reading time: ${data.reading_time} min`;
                                
                                // Display language info
                                const langName = getLanguageName(data.language);
                                languageInfo.textContent = `Language: ${langName}`;
                                
                                // Display topics
                                displayTopics(data.topics);
                                
                                // Display keywords
                                displayKeywords(data.keywords);
                                
                                // Display quality metrics
                                displayQualityMetrics(data.quality_metrics);
                                
                                // Update save button
                                saveBtn.textContent = 'Already Saved';
                                saveBtn.disabled = true;
                                
                                // Show result section
                                resultSection.style.display = 'block';
                                resultSection.scrollIntoView({ behavior: 'smooth' });
                            });
                    });
                    
                    // Add elements to summary item
                    summaryItem.appendChild(summaryContent);
                    summaryItem.appendChild(deleteBtn);
                    summariesList.appendChild(summaryItem);
                });
            })
            .catch(error => {
                console.error('Error loading summaries:', error);
                summariesList.innerHTML = '<p>Error loading summaries</p>';
            });
    }
    
    // Load summaries on page load
    loadSummaries();
    
    // Current summary data
    let currentSummaryData = null;
    let currentSummaryId = null;
    
    // Save summary button
    saveBtn.addEventListener('click', function() {
        if (!currentSummaryData) {
            alert('No summary to save');
            return;
        }
        
        // If already saved, show message
        if (currentSummaryId) {
            alert('Summary already saved');
            return;
        }
        
        // Prepare data for saving
        const saveData = {
            title: fileName.textContent,
            summary: currentSummaryData.summary,
            reading_time: currentSummaryData.reading_time,
            language: currentSummaryData.language,
            topics: currentSummaryData.topics,
            keywords: currentSummaryData.keywords,
            quality_metrics: currentSummaryData.quality_metrics
        };
        
        // Send save request
        fetch('/summaries/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(saveData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.summary_id) {
                currentSummaryId = data.summary_id;
                alert('Summary saved successfully!');
                loadSummaries(); // Refresh the summaries list
            } else {
                alert('Error saving summary');
            }
        })
        .catch(error => {
            alert('Error saving summary: ' + error.message);
        });
    });
});