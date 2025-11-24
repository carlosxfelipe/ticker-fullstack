// Detecta o tema atual do sistema
function getCurrentTheme() {
  return window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
}

// Paletas de cores para cada tema
const chartColorsLight = [
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

const chartColorsDark = [
  "#2B7BB9",
  "#CC4F6B",
  "#D4A843",
  "#3A9A9A",
  "#7B52CC",
  "#CC7D33",
  "#8A8C8E",
  "#6B9C3A",
  "#B81850",
  "#7B1F8C",
  "#32408C",
  "#1A75BF",
  "#0287BF",
  "#008C9E",
  "#007566",
  "#3D8C40",
  "#A3B030",
  "#CC9A06",
  "#CC7700",
  "#CC4519",
  "#5C4338",
  "#757575",
  "#4A5F6B",
  "#148C75",
  "#25A359",
  "#2B7CB3",
  "#7D479C",
  "#2A3B4F",
  "#117A6B",
  "#1F8C4F",
];

// Seleciona a paleta correta baseada no tema
const chartColors =
  getCurrentTheme() === "dark" ? chartColorsDark : chartColorsLight;

// Formatador de moeda brasileira
const formatBRL = new Intl.NumberFormat("pt-BR", {
  style: "currency",
  currency: "BRL",
});

function initPortfolioChart(labels, values, type, canvasId) {
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

  new window.Chart(document.getElementById(canvasId), {
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

// Escuta mudanças no tema do sistema e atualiza os gráficos
window
  .matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", () => {
    location.reload();
  });
