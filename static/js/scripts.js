document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    if (data.report_id) {
        document.getElementById('reportFrame').src = `https://app.powerbi.com/reportEmbed?reportId=${data.report_id}&autoAuth=true`;
    } else {
        alert('Report not found');
    }
};

document.getElementById('dropdown').onchange = async function(event) {
    const selectedOption = event.target.value;
    const response = await fetch('/get_report_id', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ selectedOption: selectedOption })
    });

    const data = await response.json();
    if (data.report_id) {
        document.getElementById('reportFrame').src = `https://app.powerbi.com/reportEmbed?reportId=${data.report_id}&autoAuth=true`;
    } else {
        alert('Report not found');
    }
};

