document.getElementById("predictForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const resultBox = document.getElementById("result");
  resultBox.textContent = "⏳ Predicting...";
  resultBox.className = "result-box result-waiting";

  // Collect values using the correct IDs matching index.html
  const data = {
    Administrative:          parseFloat(document.getElementById("Administrative").value),
    Administrative_Duration: parseFloat(document.getElementById("Administrative_Duration").value),
    Informational:           parseFloat(document.getElementById("Informational").value),
    Informational_Duration:  parseFloat(document.getElementById("Informational_Duration").value),
    ProductRelated:          parseFloat(document.getElementById("ProductRelated").value),
    ProductRelated_Duration: parseFloat(document.getElementById("ProductRelated_Duration").value),
    BounceRates:             parseFloat(document.getElementById("BounceRates").value),
    ExitRates:               parseFloat(document.getElementById("ExitRates").value),
    PageValues:              parseFloat(document.getElementById("PageValues").value),
    SpecialDay:              parseFloat(document.getElementById("SpecialDay").value),
    Month:                   document.getElementById("Month").value,        // string, e.g. "May"
    OperatingSystems:        parseInt(document.getElementById("OperatingSystems").value),
    Browser:                 parseInt(document.getElementById("Browser").value),
    Region:                  parseInt(document.getElementById("Region").value),
    TrafficType:             parseInt(document.getElementById("TrafficType").value),
    VisitorType:             document.getElementById("VisitorType").value,  // string, e.g. "Returning_Visitor"
    Weekend:                 parseInt(document.getElementById("Weekend").value),
  };

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    if (result.error) {
      resultBox.textContent = "⚠️ Error: " + result.error;
      resultBox.className = "result-box result-failure";
      return;
    }

    // ── Update result box ──────────────────────────────────────────────────
    if (result.prediction === 1) {
      resultBox.textContent = "🟢 " + result.label;
      resultBox.className = "result-box result-success";
    } else {
      resultBox.textContent = "🔴 " + result.label;
      resultBox.className = "result-box result-failure";
    }

    // ── Update probability bars ────────────────────────────────────────────
    const probSection = document.getElementById("probabilities");
    probSection.style.display = "block";
    document.getElementById("barPurchase").style.width   = result.probability_purchase + "%";
    document.getElementById("barNoPurchase").style.width = result.probability_no_purchase + "%";
    document.getElementById("probPurchase").textContent   = result.probability_purchase + "%";
    document.getElementById("probNoPurchase").textContent = result.probability_no_purchase + "%";

    // ── Update doughnut chart ──────────────────────────────────────────────
    updateChart(result.probability_purchase, result.probability_no_purchase);

  } catch (err) {
    resultBox.textContent = "⚠️ Request failed: " + err.message;
    resultBox.className = "result-box result-failure";
  }
});

// ── Chart.js doughnut ────────────────────────────────────────────────────────
let chart;
function updateChart(pPurchase, pNoPurchase) {
  const ctx = document.getElementById("probabilityChart").getContext("2d");
  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Will Purchase", "Won't Purchase"],
      datasets: [{
        data: [pPurchase, pNoPurchase],
        backgroundColor: ["#2ecc71", "#e74c3c"],
        borderColor: ["#27ae60", "#c0392b"],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
          labels: { color: "#ffffff", font: { size: 13 } }
        },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.label}: ${ctx.parsed}%`
          }
        }
      }
    }
  });
}
