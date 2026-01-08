export function initConvergenceRate(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = `
    <div style="font-family: system-ui, sans-serif; text-align: center;">
      <canvas id="${containerId}-cv" width="600" height="300" style="border: 1px solid #ccc; border-radius: 8px;"></canvas>
      <p style="font-size: 0.9em; color: #666;">
        Log-error plot: log(|f(x_k) - p*|).
        <br>
        <span style="color: #007bff">● Gradient Descent (Linear)</span>,
        <span style="color: #dc3545">● Newton (Quadratic)</span>
      </p>
    </div>
  `;

  const canvas = document.getElementById(`${containerId}-cv`);
  const ctx = canvas.getContext('2d');

  // GD: error_{k+1} = c * error_k  => log error linear decrease
  // Newton: error_{k+1} = c * error_k^2 => log error doubles each step

  const dataGD = [];
  let e = 1.0;
  for(let i=0; i<30; i++) {
      dataGD.push(Math.log10(e));
      e *= 0.8;
  }

  const dataNewton = [];
  e = 1.0;
  for(let i=0; i<10; i++) {
      dataNewton.push(Math.log10(e));
      e = e * e; // Quadratic convergence roughly
      if(e < 1e-15) break;
  }

  function draw() {
      const W = canvas.width;
      const H = canvas.height;
      const pad = 40;

      ctx.clearRect(0,0,W,H);

      // Axes
      ctx.beginPath();
      ctx.moveTo(pad, pad); ctx.lineTo(pad, H-pad); ctx.lineTo(W-pad, H-pad);
      ctx.strokeStyle = '#333';
      ctx.stroke();

      // Plot GD
      ctx.beginPath();
      ctx.strokeStyle = '#007bff';
      ctx.lineWidth = 2;
      for(let i=0; i<dataGD.length; i++) {
          const x = pad + (i / 30) * (W - 2*pad);
          const y = pad + ((-dataGD[i]) / 16) * (H - 2*pad); // map 0..-16 to top..bottom
          if(i===0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Plot Newton
      ctx.beginPath();
      ctx.strokeStyle = '#dc3545';
      ctx.lineWidth = 2;
      for(let i=0; i<dataNewton.length; i++) {
          const x = pad + (i / 30) * (W - 2*pad);
          const y = pad + ((-dataNewton[i]) / 16) * (H - 2*pad);
          if(i===0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
          ctx.arc(x, y, 2, 0, 2*Math.PI);
      }
      ctx.stroke();

      ctx.font = '12px sans-serif';
      ctx.fillStyle = '#666';
      ctx.fillText('Iterations', W/2, H-10);
      ctx.save();
      ctx.translate(15, H/2);
      ctx.rotate(-Math.PI/2);
      ctx.fillText('Log Error', 0, 0);
      ctx.restore();
  }

  draw();
}
