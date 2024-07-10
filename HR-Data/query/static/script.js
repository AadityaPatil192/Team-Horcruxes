function fetchData() {
    const query = document.getElementById('queryDropdown').value;
    if (query) {
        fetch(`http://127.0.0.1:5000/${query}`)
            .then(response => response.json())
            .then(data => displayData(data, query))
            .catch(error => console.error('Error:', error));
    } else {
        document.getElementById('result').innerHTML = '';
    }
}

function displayData(data, query) {
    if (!data.length) {
        document.getElementById('result').innerHTML = '<p>No results found.</p>';
        return;
    }

    // Ensure 'name' is the first key, unless it's the last query
    let keys = Object.keys(data[0]);
    if (query !== 'query_e') {
        keys = ['name', ...keys.filter(key => key !== 'name')];
    } else {
        keys = keys.filter(key => key !== 'name');
    }

    let html = '<table><thead><tr>';
    keys.forEach(key => {
        html += `<th>${key}</th>`;
    });
    html += '</tr></thead><tbody>';
    
    data.forEach(item => {
        html += '<tr>';
        keys.forEach(key => {
            html += `<td>${item[key]}</td>`;
        });
        html += '</tr>';
    });

    html += '</tbody></table>';
    document.getElementById('result').innerHTML = html;
}
