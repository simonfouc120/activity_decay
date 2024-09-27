async function fetchHalfLifeData() {
    const response = await fetch('http://127.0.0.1:5000/data');
    const data = await response.json();
    const select = document.getElementById('element');
    for (const [isotope, halfLife] of Object.entries(data)) {
        const option = document.createElement('option');
        option.value = isotope;
        option.textContent = `${isotope} (Half-life: ${halfLife} years)`;
        select.appendChild(option);
    }
}

async function submitForm(event) {
    event.preventDefault();
    const element = document.getElementById('element').value;
    const initialActivity = document.getElementById('initial-activity').value;
    const start = document.getElementById('start').value;
    const end = document.getElementById('end').value;
    const response = await fetch('http://127.0.0.1:5000/calculate', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ element, initialActivity, start, end })
    });
    const result = await response.json();
    if (response.ok) {
        const scientificActivity = result.current_activity > 999999 ? result.current_activity.toExponential(2) : result.current_activity.toFixed(2);
        document.getElementById('result').textContent = `Current activity: ${scientificActivity} Bq`;
    } else {
        alert(`Error: ${result.error}`);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetchHalfLifeData();
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('end').value = today;
});