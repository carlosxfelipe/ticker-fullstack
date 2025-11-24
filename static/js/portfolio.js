// JS para o gráfico dinâmico do portfolio

// Paleta de cores para os gráficos
const chartColors = [
  "#36A2EB",
  "#FF6384",
  "#FFCE56",
  "#4BC0C0",
  "#9966FF",
  "#FF9F40",
  "#C9CBCF",
  "#8BC34A",
  "#E91E63",
  "#9C27B0",
  "#3F51B5",
  "#2196F3",
  "#03A9F4",
  "#00BCD4",
  "#009688",
  "#4CAF50",
  "#CDDC39",
  "#FFC107",
  "#FF9800",
  "#FF5722",
  "#795548",
  "#9E9E9E",
  "#607D8B",
  "#1ABC9C",
  "#2ECC71",
  "#3498DB",
  "#9B59B6",
  "#34495E",
  "#16A085",
  "#27AE60",
];

// Formatador de moeda brasileira
const formatBRL = new Intl.NumberFormat("pt-BR", {
  style: "currency",
  currency: "BRL",
});

function initPortfolioChart(labels, values) {
  const data = {
    labels: labels,
    datasets: [
      {
        data: values,
        backgroundColor: chartColors,
        borderColor: "transparent",
        borderWidth: 0,
      },
    ],
  };

  let chartInstance;
  function renderChart(type) {
    if (chartInstance) chartInstance.destroy();
    chartInstance = new window.Chart(document.getElementById("pieChart"), {
      type: type,
      data: data,
      options: {
        plugins: {
          legend: {
            display: type !== "bar",
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                const value = context.raw;
                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                const percent = total ? ((value / total) * 100).toFixed(2) : 0;
                return formatBRL.format(value) + " (" + percent + "%)";
              },
            },
          },
          datalabels: {
            color: "#fff",
            formatter: function (value, context) {
              return context.chart.data.labels[context.dataIndex];
            },
            font: {
              weight: "bold",
              size: 14,
            },
          },
        },
      },
      plugins: [window.ChartDataLabels],
    });
  }

  document.getElementById("chartType").addEventListener("change", function (e) {
    renderChart(e.target.value);
  });

  renderChart("doughnut");
}
