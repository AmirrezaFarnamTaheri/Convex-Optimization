export function initNormSteepest(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Create canvas
    const canvas = document.createElement('canvas');
    canvas.width = 520;
    canvas.height = 520;
    canvas.style.width = '100%';
    canvas.style.height = 'auto';
    canvas.style.maxWidth = '520px';
    canvas.style.border = '1px solid #ccc';
    canvas.style.background = 'white';
    canvas.style.display = 'block';
    canvas.style.margin = '0 auto';
    container.appendChild(canvas);

    const ctx = canvas.getContext("2d");

    function drawArrow(x0,y0,x1,y1) {
      ctx.beginPath();
      ctx.moveTo(x0,y0); ctx.lineTo(x1,y1);
      ctx.stroke();
      const ang = Math.atan2(y1-y0, x1-x0);
      const L = 10;
      ctx.beginPath();
      ctx.moveTo(x1,y1);
      ctx.lineTo(x1 - L*Math.cos(ang-0.35), y1 - L*Math.sin(ang-0.35));
      ctx.lineTo(x1 - L*Math.cos(ang+0.35), y1 - L*Math.sin(ang+0.35));
      ctx.closePath();
      ctx.fill();
    }

    function worldToCanvas(p) {
      const s = 180; // scale
      return [canvas.width/2 + s*p[0], canvas.height/2 - s*p[1]];
    }

    let t = 0;

    function step() {
      t += 0.01; // Slower rotation

      // gradient rotates (slightly anisotropic to make snapping obvious)
      const g = [Math.cos(t), 0.65*Math.sin(t)];

      // L2 steepest: -g/||g||
      const ng = Math.hypot(g[0], g[1]);
      const v2 = [-g[0]/ng, -g[1]/ng];

      // L1 steepest: axis of max |g_i|
      const j = Math.abs(g[0]) >= Math.abs(g[1]) ? 0 : 1;
      const v1 = [0,0];
      v1[j] = g[j] === 0 ? -1 : -Math.sign(g[j]);

      ctx.clearRect(0,0,canvas.width,canvas.height);

      // axes
      ctx.strokeStyle = "#eee";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(canvas.width/2, 0); ctx.lineTo(canvas.width/2, canvas.height);
      ctx.moveTo(0, canvas.height/2); ctx.lineTo(canvas.width, canvas.height/2);
      ctx.stroke();

      // L2 unit ball (circle)
      ctx.strokeStyle = "#444";
      ctx.beginPath();
      for (let k=0;k<=200;k++){
        const th = 2*Math.PI*k/200;
        const p = [Math.cos(th), Math.sin(th)];
        const [x,y] = worldToCanvas(p);
        if (k===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
      }
      ctx.stroke();

      // L1 unit ball (diamond)
      ctx.beginPath();
      const diamond = [[1,0],[0,1],[-1,0],[0,-1],[1,0]];
      diamond.forEach((p,idx)=>{
        const [x,y] = worldToCanvas(p);
        if(idx===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
      });
      ctx.stroke();

      // arrows
      ctx.lineWidth = 2;

      const O = worldToCanvas([0,0]);
      const G = worldToCanvas(g);
      const V2 = worldToCanvas(v2);
      const V1 = worldToCanvas(v1);

      // draw gradient g (Blue)
      ctx.strokeStyle = "#007bff";
      ctx.fillStyle = "#007bff";
      drawArrow(O[0],O[1], G[0],G[1]);

      // draw L2 steepest (Red)
      ctx.strokeStyle = "#dc3545";
      ctx.fillStyle = "#dc3545";
      drawArrow(O[0],O[1], V2[0],V2[1]);

      // draw L1 steepest (Green)
      ctx.strokeStyle = "#28a745";
      ctx.fillStyle = "#28a745";
      drawArrow(O[0],O[1], V1[0],V1[1]);

      // Legend
      ctx.font = "14px sans-serif";
      ctx.textAlign = "left";

      ctx.fillStyle = "#007bff";
      ctx.fillText("Gradient g", 10, 20);

      ctx.fillStyle = "#dc3545";
      ctx.fillText("L2 Steepest (-g/||g||)", 10, 40);

      ctx.fillStyle = "#28a745";
      ctx.fillText("L1 Steepest (Coordinate Descent)", 10, 60);

      requestAnimationFrame(step);
    }
    step();
}
