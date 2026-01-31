// Strong convexity vs. convexity (educational widget)
// This script is loaded as a module, but uses global `d3` injected in the HTML.

function fStrong(x) {
  // Strongly convex example
  return x * x;
}

function fConvexOnly(x) {
  // Convex but not strongly convex on R (curvature vanishes at 0)
  return Math.pow(x, 4);
}

function plot(container) {
  const width = 620;
  const height = 360;
  const margin = { top: 24, right: 20, bottom: 40, left: 50 };

  container.innerHTML = `
    <div style="display:flex; align-items:center; justify-content:space-between; gap:12px; margin-bottom: 10px;">
      <div style="font-weight:600;">Convex vs. Strongly Convex</div>
      <label style="display:flex; align-items:center; gap:8px; font-size: 0.9em;">
        <span>Show:</span>
        <select id="sc-mode">
          <option value="strong">Strongly convex (x²)</option>
          <option value="convex">Convex only (x⁴)</option>
          <option value="both">Both</option>
        </select>
      </label>
    </div>
    <div style="opacity:0.85; font-size:0.9em; margin-bottom: 10px;">
      Strong convexity means \(f(x) - \\tfrac{m}{2}\\|x\\|^2\) is convex for some \(m>0\).
      The curve \(x^4\) is convex, but not strongly convex on \(\mathbb{R}\) (curvature vanishes at 0).
    </div>
    <div id="sc-plot"></div>
  `;

  const sel = container.querySelector("#sc-mode");
  const plotEl = container.querySelector("#sc-plot");

  const svg = d3
    .select(plotEl)
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  const x = d3.scaleLinear().domain([-2.5, 2.5]).range([margin.left, width - margin.right]);
  const y = d3.scaleLinear().domain([0, 7]).range([height - margin.bottom, margin.top]);

  const axisColor = "rgba(255,255,255,0.45)";

  svg
    .append("g")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(6))
    .call((g) => g.selectAll("text").attr("fill", axisColor))
    .call((g) => g.selectAll("path,line").attr("stroke", axisColor));

  svg
    .append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(6))
    .call((g) => g.selectAll("text").attr("fill", axisColor))
    .call((g) => g.selectAll("path,line").attr("stroke", axisColor));

  const line = d3
    .line()
    .x((d) => x(d[0]))
    .y((d) => y(d[1]));

  const xs = d3.range(-2.5, 2.5001, 0.02);
  const dataStrong = xs.map((v) => [v, fStrong(v)]);
  const dataConvex = xs.map((v) => [v, fConvexOnly(v)]);

  const pStrong = svg
    .append("path")
    .attr("fill", "none")
    .attr("stroke", "rgba(59,130,246,0.95)")
    .attr("stroke-width", 2)
    .attr("d", line(dataStrong));

  const pConvex = svg
    .append("path")
    .attr("fill", "none")
    .attr("stroke", "rgba(16,185,129,0.95)")
    .attr("stroke-width", 2)
    .attr("d", line(dataConvex));

  const legend = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);
  const legItems = [
    { key: "strong", label: "x² (strongly convex)", color: "rgba(59,130,246,0.95)" },
    { key: "convex", label: "x⁴ (convex only)", color: "rgba(16,185,129,0.95)" },
  ];

  function renderLegend(mode) {
    legend.selectAll("*").remove();
    const showStrong = mode === "strong" || mode === "both";
    const showConvex = mode === "convex" || mode === "both";
    const items = legItems.filter((it) => (it.key === "strong" ? showStrong : showConvex));

    const row = legend
      .selectAll("g")
      .data(items)
      .enter()
      .append("g")
      .attr("transform", (_, i) => `translate(0, ${i * 18})`);

    row
      .append("rect")
      .attr("x", 0)
      .attr("y", -10)
      .attr("width", 12)
      .attr("height", 12)
      .attr("fill", (d) => d.color)
      .attr("rx", 2);

    row
      .append("text")
      .attr("x", 18)
      .attr("y", 0)
      .attr("fill", "rgba(255,255,255,0.85)")
      .attr("font-size", 12)
      .text((d) => d.label);
  }

  function setMode(mode) {
    const showStrong = mode === "strong" || mode === "both";
    const showConvex = mode === "convex" || mode === "both";
    pStrong.style("display", showStrong ? null : "none");
    pConvex.style("display", showConvex ? null : "none");
    renderLegend(mode);
  }

  sel.addEventListener("change", () => setMode(sel.value));
  setMode(sel.value);
}

const container = document.getElementById("strong-convexity-container");
if (container && typeof d3 !== "undefined") {
  plot(container);
} else {
  // eslint-disable-next-line no-console
  console.error("Strong convexity widget failed to initialize (missing container or d3).");
}


