export function initAdvancedLaDemos(containerId, demoType) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (demoType === 'svd') {
        initSvdGeometryDemo(container);
    } else if (demoType === 'schur') {
        initSchurComplementDemo(container);
    }
}

function initSvdGeometryDemo(container) {
    container.innerHTML = `
        <div style="display: flex; justify-content: space-around; align-items: center; height: 350px;">
            <div style="text-align: center;">
                <h4>Domain (V)</h4>
                <canvas id="${container.id}-domain" width="300" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            </div>
            <div style="font-size: 24px;">&rarr; <br> A = U &Sigma; V<sup>T</sup></div>
            <div style="text-align: center;">
                <h4>Codomain (U)</h4>
                <canvas id="${container.id}-codomain" width="300" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            </div>
        </div>
        <div style="text-align: center;">
            <label>Rotate Input Basis (V): <input type="range" min="0" max="360" value="0" id="${container.id}-rot"></label>
            <label>Scale (&sigma;1, &sigma;2): <input type="range" min="0.1" max="2" step="0.1" value="1.5" id="${container.id}-scale"></label>
        </div>
    `;

    const canvasIn = document.getElementById(`${container.id}-domain`);
    const canvasOut = document.getElementById(`${container.id}-codomain`);
    const ctxIn = canvasIn.getContext('2d');
    const ctxOut = canvasOut.getContext('2d');

    let angle = 0;
    let sigma1 = 1.5;
    let sigma2 = 0.8;

    function toScreen(x, y, w, h) {
        return { x: x * 50 + w / 2, y: -y * 50 + h / 2 };
    }

    function render() {
        // Clear
        ctxIn.clearRect(0, 0, 300, 300);
        ctxOut.clearRect(0, 0, 300, 300);

        // Draw Unit Circle on Domain
        ctxIn.beginPath();
        ctxIn.arc(150, 150, 50, 0, 2 * Math.PI);
        ctxIn.strokeStyle = '#ddd';
        ctxIn.stroke();

        // Draw Axes V1, V2
        const v1x = Math.cos(angle);
        const v1y = Math.sin(angle);
        const v2x = -Math.sin(angle);
        const v2y = Math.cos(angle);

        drawVector(ctxIn, v1x, v1y, 'blue', 'v1');
        drawVector(ctxIn, v2x, v2y, 'green', 'v2');

        // Codomain: Draw Ellipse (Image of Circle)
        // A maps v1 -> sigma1 * u1, v2 -> sigma2 * u2
        // We assume U is Identity for simplicity of visualization (showing alignment),
        // or we can rotate U. Let's fix U to standard axes to show sigma alignment.

        ctxOut.beginPath();
        ctxOut.ellipse(150, 150, 50 * sigma1, 50 * sigma2, 0, 0, 2 * Math.PI);
        ctxOut.strokeStyle = 'red';
        ctxOut.lineWidth = 2;
        ctxOut.stroke();

        // Draw Principal Axes
        drawVector(ctxOut, sigma1, 0, 'blue', `σ1 u1 (${sigma1})`);
        drawVector(ctxOut, 0, sigma2, 'green', `σ2 u2 (${sigma2})`);
    }

    function drawVector(ctx, x, y, color, label) {
        const s = toScreen(x, y, 300, 300);
        const c = {x: 150, y: 150};

        ctx.strokeStyle = color;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(c.x, c.y);
        ctx.lineTo(s.x, s.y);
        ctx.stroke();

        ctx.fillStyle = color;
        ctx.fillText(label, s.x + 5, s.y - 5);
    }

    document.getElementById(`${container.id}-rot`).addEventListener('input', (e) => {
        angle = (e.target.value * Math.PI) / 180;
        render();
    });

    document.getElementById(`${container.id}-scale`).addEventListener('input', (e) => {
        sigma1 = parseFloat(e.target.value);
        render();
    });

    render();
}

function initSchurComplementDemo(container) {
    container.innerHTML = `
        <div style="text-align: center; padding: 20px;">
            <p>Matrix M = [[d, b], [b, c]] (Symmetric 2x2)</p>
            <p>Schur Complement of d is $S = c - b^2/d$</p>
            <div style="display: flex; justify-content: center; gap: 20px; align-items: center;">
                <label>d (Pivot): <input type="number" id="${container.id}-d" value="2" step="0.5" style="width: 60px;"></label>
                <label>b (Off-diag): <input type="range" id="${container.id}-b" min="-5" max="5" value="1" step="0.1"></label>
                <label>c (Bottom): <input type="number" id="${container.id}-c" value="1" step="0.5" style="width: 60px;"></label>
            </div>
            <canvas id="${container.id}-canvas" width="400" height="200" style="background: #f9f9f9; border: 1px solid #ddd; margin-top: 15px;"></canvas>
            <div id="${container.id}-result" style="font-weight: bold; margin-top: 10px;"></div>
        </div>
    `;

    const canvas = document.getElementById(`${container.id}-canvas`);
    const ctx = canvas.getContext('2d');
    const resultDiv = document.getElementById(`${container.id}-result`);

    const inputs = {
        d: document.getElementById(`${container.id}-d`),
        b: document.getElementById(`${container.id}-b`),
        c: document.getElementById(`${container.id}-c`)
    };

    function update() {
        const d = parseFloat(inputs.d.value);
        const b = parseFloat(inputs.b.value);
        const c = parseFloat(inputs.c.value);

        // Schur Complement S = c - b^2/d
        // PSD Condition: d > 0 AND S >= 0

        const S = c - (b*b)/d;

        let isPSD = false;
        if (d > 0 && S >= 0) isPSD = true;

        resultDiv.innerHTML = `
            Schur Complement S = ${c} - (${b}² / ${d}) = ${S.toFixed(2)} <br>
            Matrix is ${isPSD ? '<span style="color: green">Positive Semidefinite (PSD)</span>' : '<span style="color: red">Indefinite / Not PSD</span>'}
        `;

        // Visualize: Plot f(y) = min_x (x,y) M (x,y)^T = S * y^2
        // We draw the parabola S * y^2

        ctx.clearRect(0, 0, 400, 200);

        // Draw axes
        ctx.strokeStyle = '#aaa';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, 150); ctx.lineTo(400, 150); // x-axis (y value 0 line)
        ctx.moveTo(200, 0); ctx.lineTo(200, 200); // y-axis
        ctx.stroke();

        ctx.strokeStyle = isPSD ? 'green' : 'red';
        ctx.lineWidth = 3;
        ctx.beginPath();

        for (let x = -200; x <= 200; x += 2) {
            // map x pixels to y input range -2 to 2
            const yVal = (x / 100);
            // Value of minimized quadratic form: S * y^2
            // If d < 0, the minimization isn't valid, but let's just plot S*y^2
            let z = S * yVal * yVal;

            // Map z to screen y (scale 20px per unit)
            // Screen Y = 150 - z * 20
            const screenY = 150 - z * 20;

            if (x === -200) ctx.moveTo(x + 200, screenY);
            else ctx.lineTo(x + 200, screenY);
        }
        ctx.stroke();

        ctx.fillStyle = '#333';
        ctx.fillText("Minimized Energy Profile (y -> min_x x^T M x)", 10, 20);
    }

    Object.values(inputs).forEach(input => input.addEventListener('input', update));
    update();
}
