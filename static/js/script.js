// 초기 차트 저장할 변수
let myChart = null;

// 데이터를 불러오는 함수
async function fetchData(filePath, dataCount) {
    const response = await fetch(filePath);
    const text = await response.text();
    const lines = text.trim().split('\n');
    
    const labels = [];
    const dataPoints = [];
    
    lines.forEach(line => {
        const [date, time, value] = line.split(' ');
        labels.push(`${date} ${time}`);
        dataPoints.push(parseFloat(value));
    });
    
    // 최근 데이터 개수에 맞춰 자르기
    const recentLabels = labels.slice(-dataCount);
    const recentDataPoints = dataPoints.slice(-dataCount);
    
    return { labels: recentLabels, dataPoints: recentDataPoints };
}

// 차트를 생성하거나 업데이트하는 함수
function updateChart(labels, dataPoints) {
    const ctx = document.getElementById('myChart').getContext('2d');

    // 차트가 이미 있을 경우 삭제
    if (myChart) {
        myChart.destroy();
    }

    // 새로운 차트를 생성
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,  // X축 라벨 (날짜 + 시간)
            datasets: [{
                label: '',
                data: dataPoints,  // Y축 데이터 (값)
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2,
                fill: true,
                pointRadius: 5,
                pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                tension: 0.2  // 부드러운 곡선
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: false,
                        text: ''
                    }
                },
                y: {
                    title: {
                        display: false,
                        text: ''
                    },
                    beginAtZero: false,
                    ticks: {
                        callback: function(value) {
                            if (value >= 1) {
                                // 1 이상인 값은 소수점 없이 표시
                                return value.toLocaleString();  // 천 단위 콤마 추가
                            } else {
                                // 1 미만인 값은 소수점 6자리까지 표시
                                return value.toFixed(8);  // 일반 숫자 형식으로 표시
                            }
                        }
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            let value = tooltipItem.raw;
                            // 값이 1 이상일 때는 소수점 없이, 1 미만일 때는 소수점 6자리까지 표시
                            if (value >= 1) {
                                return `Value: ${value.toLocaleString()}`;
                            } else {
                                return `Value: ${value.toFixed(8)}`;
                            }
                        }
                    }
                }
            }
        }
    });
}

// 드롭다운 선택에 따라 차트를 업데이트하는 함수
document.getElementById('fileSelect').addEventListener('change', async function() {
    const selectedFile = this.value;  // 선택된 파일 경로
    const dataCount = document.getElementById('dataCountSelect').value;  // 선택된 데이터 개수
    const { labels, dataPoints } = await fetchData(selectedFile, dataCount);  // 데이터를 가져옴
    updateChart(labels, dataPoints);  // 차트 업데이트
});

// 데이터 개수 선택 드롭다운 변경 시 차트를 업데이트하는 함수
document.getElementById('dataCountSelect').addEventListener('change', async function() {
    const selectedFile = document.getElementById('fileSelect').value;  // 현재 선택된 파일
    const dataCount = this.value;  // 선택된 데이터 개수
    const { labels, dataPoints } = await fetchData(selectedFile, dataCount);  // 데이터를 가져옴
    updateChart(labels, dataPoints);  // 차트 업데이트
});

// 초기 로드 시 기본 파일과 데이터 개수로 차트 생성
window.onload = async function() {
    const defaultFile = document.getElementById('fileSelect').value;  // 기본 파일
    const dataCount = document.getElementById('dataCountSelect').value;  // 기본 데이터 개수
    const { labels, dataPoints } = await fetchData(defaultFile, dataCount);  // 데이터를 가져옴
    updateChart(labels, dataPoints);  // 차트 생성
};
