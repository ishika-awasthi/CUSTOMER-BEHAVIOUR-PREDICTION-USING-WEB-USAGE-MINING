document.getElementById("predictForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  // Collect input values
  const data = {
    Administrative: parseFloat(document.getElementById("administrative").value),
    Administrative_Duration: parseFloat(document.getElementById("administrative_duration").value),
    Informational: parseFloat(document.getElementById("informational").value),
    Informational_Duration: parseFloat(document.getElementById("informational_duration").value),
    ProductRelated: parseFloat(document.getElementById("product_related").value),
    ProductRelated_Duration: parseFloat(document.getElementById("product_related_duration").value),
    BounceRates: parseFloat(document.getElementById("bounce_rates").value),
    ExitRates: parseFloat(document.getElementById("exit_rates").value),
    PageValues: parseFloat(document.getElementById("page_values").value),
    SpecialDay: parseFloat(document.getElementById("special_day").value),
    Month: parseInt(document.getElementById("month").value),
    OperatingSystems: parseInt(document.getElementById("operating_system").value),
    Browser: parseInt(document.getElementById("browser").value),
    Region: parseInt(document.getElementById("region").value),
    TrafficType: parseInt(document.getElementById("traffic_type").value),
    VisitorType: parseInt(document.getElementById("visitor_type").value),
    Weekend: document.getElementById("weekend").value === "TRUE" ? 1 : 0
  };

  // Call Flask API
  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();

  // Show result
  const resultBox = document.getElementById("result");
  if (result.prediction === 1) {
    resultBox.textContent = "🟢 Likely to Purchase";
    resultBox.className = "result-box result-success";
  } else {
    resultBox.textContent = "🔴 Not Likely to Purchase";
    resultBox.className = "result-box result-failure";
  }

  // Update chart
  updateChart(result.prediction);
});

// Chart.js
let chart;
function updateChart(prediction) {
  const ctx = document.getElementById("probabilityChart").getContext("2d");
  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Purchase", "No Purchase"],
      datasets: [{
        data: prediction === 1 ? [70, 30] : [30, 70],
        backgroundColor: ["#2ecc71", "#e74c3c"]
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: "bottom" }
      }
    }
  });
}
