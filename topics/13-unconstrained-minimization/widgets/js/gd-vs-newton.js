export function initGDvsNewton(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = `
    <div style="font-family: system-ui, sans-serif; text-align: center;">
      <canvas id="${containerId}-cv" width="600" height="400" style="border: 1px solid #ccc; border-radius: 8px;"></canvas>
      <div style="margin-top: 10px;">
        <button id="${containerId}-run">Run Optimization</button>
      </div>
      <p style="font-size: 0.9em; color: #666;">
        Comparing GD (blue) vs Newton (red) on f(x,y) = x^2 + 10y^2.
        Newton jumps to the optimum in 1 step!
      </p>
    </div>
  `;

  const canvas = document.getElementById(`${containerId}-cv`);
  const ctx = canvas.getContext('2d');
  const btn = document.getElementById(`${containerId}-run`);

  // Problem: f(x) = 0.5 * (x^2 + 10y^2)
  // Gradient: [x, 10y]
  // Hessian: diag(1, 10)
  // Newton step: -H^-1 g = -[x, y] => x_new = 0.

  const x0 = [250, 150]; // Relative to center
  const center = [300, 200];
  const scale = 40;

  function toPx(x, y) {
    return [center[0] + x * scale, center[1] - y * scale];
  }

  function drawContours() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 1;
    for (let r of [0.5, 1, 2, 4, 6]) {
      ctx.beginPath();
      for (let t = 0; t <= 2 * Math.PI; t += 0.1) {
        // x^2 + 10y^2 = r^2
        // x = r cos t, y = (r/sqrt(10)) sin t
        const x = r * Math.cos(t);
        const y = (r / Math.sqrt(10)) * Math.sin(t);
        const p = toPx(x, y);
        if (t === 0) ctx.moveTo(p[0], p[1]);
        else ctx.lineTo(p[0], p[1]);
      }
      ctx.strokeStyle = '#eee';
      ctx.stroke();
    }
    // Axes
    ctx.beginPath();
    ctx.moveTo(center[0], 0); ctx.lineTo(center[0], 400);
    ctx.moveTo(0, center[1]); ctx.lineTo(600, center[1]);
    ctx.strokeStyle = '#ddd';
    ctx.stroke();
  }

  function run() {
    drawContours();

    // Gradient Descent Path (Blue)
    let x = [4, 3];
    ctx.beginPath();
    let start = toPx(x[0], x[1]);
    ctx.moveTo(start[0], start[1]);

    // GD with fixed small step
    const lr = 0.18; // 2/(L+mu) approx
    for(let i=0; i<20; i++) {
        const g = [x[0], 10*x[1]];
        x[0] -= lr * g[0];
        x[1] -= lr * g[1];
        const p = toPx(x[0], x[1]);
        ctx.lineTo(p[0], p[1]);
    }
    ctx.strokeStyle = '#007bff';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Draw dots
    x = [4, 3];
    for(let i=0; i<20; i++) {
        const p = toPx(x[0], x[1]);
        ctx.fillStyle = '#007bff';
        ctx.beginPath(); ctx.arc(p[0], p[1], 3, 0, 2*Math.PI); ctx.fill();
        const g = [x[0], 10*x[1]];
        x[0] -= lr * g[0];
        x[1] -= lr * g[1];
    }

    // Newton Path (Red)
    x = [4, 3];
    start = toPx(x[0], x[1]);
    const end = toPx(0, 0); // Newton converges in 1 step for quadratic

    ctx.beginPath();
    ctx.moveTo(start[0], start[1]);
    ctx.lineTo(end[0], end[1]);
    ctx.strokeStyle = '#dc3545';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.fillStyle = '#dc3545';
    ctx.beginPath(); ctx.arc(start[0], start[1], 4, 0, 2*Math.PI); ctx.fill();
    ctx.beginPath(); ctx.arc(end[0], end[1], 4, 0, 2*Math.PI); ctx.fill();
  }

  btn.onclick = run;
  run();
}
