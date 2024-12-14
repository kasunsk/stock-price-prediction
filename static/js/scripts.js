async function predictNext30Days() {
    const ticker = document.getElementById('ticker_select').value;
    const currentPrice = document.getElementById('current_price').value;

    if (!ticker || !currentPrice) {
        alert('Please select a ticker and enter the current price.');
        return;
    }

    try {
        const response = await fetch('/predict_30_days', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ticker, current_price: currentPrice })
        });

        const data = await response.json();
        if (response.ok) {
            showPredictionGraph(data.dates, data.prices, ticker);
        } else {
            alert('Error: Could not fetch predictions.');
        }
    } catch (error) {
        alert('Error fetching predictions. Please try again.');
    }
}

function showPredictionGraphOld(dates, prices, ticker) {
    const popup = window.open('', '_blank', 'width=800,height=600');
    popup.document.write('<html><head><title>Stock Predictions</title></head><body>');
    popup.document.write('<h2>30-Day Predictions for ' + ticker + '</h2>');
    popup.document.write('<canvas id="predictionChart" width="800" height="400"></canvas>');
    popup.document.write('<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>');
    popup.document.write(`
        const ctx = document.getElementById('predictionChart').getContext('2d');
        const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ${JSON.stringify(dates)},
            datasets: [{
        label: 'Predicted Prices',
        data: ${JSON.stringify(prices)},
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
        fill: false,
        }]
        },
        options: {
    responsive: true,
    scales: {
    x: { title: { display: true, text: 'Date' } },
    y: { title: { display: true, text: 'Price' } },
    }
    }
    });
    `);
    popup.document.write('</script></body></html>');
    popup.document.close();
}

function showPredictionGraphOld2(dates, prices, ticker) {
    const popup = window.open('', '_blank', 'width=800,height=600');

    popup.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>30-Day Predictions for ${ticker}</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
        <body>
            <h2>30-Day Predictions for ${ticker}</h2>
            <canvas id="predictionChart" width="800" height="400"></canvas>
        </body>
        </html>
    `);

    popup.document.close();

    popup.onload = function () {
        const ctx = popup.document.getElementById('predictionChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Predicted Prices',
                    data: prices,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2,
                    fill: false,
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Date'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Price'
                        }
                    }
                }
            }
        });
    };
}

function showPredictionGraph(dates, prices, ticker) {
    const popup = window.open('', '_blank', 'width=800,height=600');

    // Write the basic HTML structure with Chart.js
    popup.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>30-Day Predictions for ${ticker}</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
        <body>
            <h2>30-Day Predictions for ${ticker}</h2>
            <canvas id="predictionChart" width="800" height="400"></canvas>
            <script>
                window.onload = function () {
                    const ctx = document.getElementById('predictionChart').getContext('2d');
                    new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: ${JSON.stringify(dates)},
                            datasets: [{
                                label: 'Predicted Prices',
                                data: ${JSON.stringify(prices)},
                                borderColor: 'rgba(75, 192, 192, 1)',
                                borderWidth: 2,
                                fill: false,
                            }]
                        },
                        options: {
                            responsive: true,
                            scales: {
                                x: {
                                    title: {
                                        display: true,
                                        text: 'Date'
                                    }
                                },
                                y: {
                                    title: {
                                        display: true,
                                        text: 'Price'
                                    }
                                }
                            }
                        }
                    });
                };
            </script>
        </body>
        </html>
    `);

    popup.document.close();
}



async function fetchCurrentPrice() {
    const ticker = document.getElementById('ticker_select').value;
    const endDate = document.getElementById('end_date').value;
    if (!ticker || !endDate) {
        alert('Please select a ticker and end date first.');
        return;
    }

    try {
        const response = await fetch('/current_price', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ticker, end_date: endDate })
        });

        const data = await response.json();
        if (response.ok) {
            document.getElementById('current_price').value = data.current_price;
        } else {
            alert(data.error || 'Failed to fetch current price.');
        }
    } catch (error) {
        alert('Error fetching current price. Please try again.');
    }
}
function toggleManualTicker(select) {
    const manualTickerInput = document.getElementById('manual-ticker');
    if (select.value === 'OTHER') {
        manualTickerInput.style.display = 'block';
    } else {
        manualTickerInput.style.display = 'none';
    }
}
async function handleTrainForm(event) {
    event.preventDefault(); // Prevent the default form submission
    const form = document.getElementById('train-form');
    const formData = new FormData(form);

    try {
        const response = await fetch('/train', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        if (response.ok) {
            // Show the success message
            const messageBox = document.getElementById('message-box');
            messageBox.innerHTML = `<p style="color: green;">${data.message}</p>`;
        } else {
            alert(data.message || 'Failed to train the model.');
        }
    } catch (error) {
        alert('Error training the model. Please try again.');
    }
}
function syncTickerValue(formId) {
    const tickerSelect = document.getElementById('ticker_select').value;
    const manualTicker = document.getElementById('manual-ticker').value;
    const hiddenTickerInput = document.getElementById(formId).querySelector('.hidden-ticker');
    hiddenTickerInput.value = tickerSelect === 'OTHER' ? manualTicker : tickerSelect;
}
function toggleManualTicker(select) {
    const manualTickerInput = document.getElementById('manual-ticker');
    if (select.value === 'OTHER') {
        manualTickerInput.style.display = 'block';
    } else {
        manualTickerInput.style.display = 'none';
    }
}
function setDefaultDates() {
    const startDate = document.getElementById('start_date');
    const endDate = document.getElementById('end_date');
    const today = new Date();
    const fiveYearsAgo = new Date();
    fiveYearsAgo.setFullYear(today.getFullYear() - 5);

    startDate.value = fiveYearsAgo.toISOString().split('T')[0];
    endDate.value = today.toISOString().split('T')[0];
}
window.onload = setDefaultDates;