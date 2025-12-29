export function initLinearAlgebraDemos(containerId, demoType) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (demoType === 'kernel') {
        initKernelImageDemo(container);
    } else if (demoType === 'gram-schmidt') {
        initGramSchmidtDemo(container);
    }
}

function initKernelImageDemo(container) {
    // Setup 2D Canvas for simplicity and clarity
    container.innerHTML = `
        <div style="display: flex; justify-content: space-around; align-items: center; height: 100%;">
            <div style="text-align: center;">
                <h4>Domain (Input)</h4>
                <canvas id="${container.id}-input" width="300" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            </div>
            <div style="font-size: 24px;">&rarr; <br> A</div>
            <div style="text-align: center;">
                <h4>Codomain (Output)</h4>
                <canvas id="${container.id}-output" width="300" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            </div>
        </div>
        <div style="text-align: center; margin-top: 10px;">
            <p>Matrix A: [[1, 0.5], [0.5, 0.25]] (Rank 1)</p>
            <p>Drag the <b>Blue Vector</b> (x). The <b>Red Vector</b> is Ax.</p>
            <p>The <b>Green Line</b> is the Kernel (Nullspace).</p>
        </div>
    `;

    const inputCanvas = document.getElementById(`${container.id}-input`);
    const outputCanvas = document.getElementById(`${container.id}-output`);
    const ctxIn = inputCanvas.getContext('2d');
    const ctxOut = outputCanvas.getContext('2d');

    // Matrix A = [[1, 0.5], [0.5, 0.25]] (Singular, Kernel is line y = -2x)
    const A = { a: 1, b: 0.5, c: 0.5, d: 0.25 };

    let inputVector = { x: 100, y: 50 }; // Relative to center
    let isDragging = false;

    function toScreen(x, y, canvas) {
        return { x: x + canvas.width / 2, y: -y + canvas.height / 2 };
    }

    function fromScreen(x, y, canvas) {
        return { x: x - canvas.width / 2, y: -(y - canvas.height / 2) };
    }

    function drawGrid(ctx, width, height) {
        ctx.strokeStyle = '#eee';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let x = 0; x <= width; x += 20) { ctx.moveTo(x, 0); ctx.lineTo(x, height); }
        for (let y = 0; y <= height; y += 20) { ctx.moveTo(0, y); ctx.lineTo(width, y); }
        ctx.stroke();

        // Axes
        ctx.strokeStyle = '#aaa';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(width / 2, 0); ctx.lineTo(width / 2, height);
        ctx.moveTo(0, height / 2); ctx.lineTo(width, height / 2);
        ctx.stroke();
    }

    function drawVector(ctx, x, y, color, label) {
        const center = { x: ctx.canvas.width / 2, y: ctx.canvas.height / 2 };
        const screen = toScreen(x, y, ctx.canvas);

        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = 3;

        ctx.beginPath();
        ctx.moveTo(center.x, center.y);
        ctx.lineTo(screen.x, screen.y);
        ctx.stroke();

        // Arrowhead
        const angle = Math.atan2(center.y - screen.y, screen.x - center.x);
        ctx.beginPath();
        ctx.moveTo(screen.x, screen.y);
        ctx.lineTo(screen.x - 10 * Math.cos(angle - Math.PI / 6), screen.y + 10 * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(screen.x - 10 * Math.cos(angle + Math.PI / 6), screen.y + 10 * Math.sin(angle + Math.PI / 6));
        ctx.fill();
    }

    function render() {
        ctxIn.clearRect(0, 0, 300, 300);
        ctxOut.clearRect(0, 0, 300, 300);

        drawGrid(ctxIn, 300, 300);
        drawGrid(ctxOut, 300, 300);

        // Draw Kernel on Input (Line y = -2x)
        ctxIn.strokeStyle = 'green';
        ctxIn.lineWidth = 2;
        ctxIn.setLineDash([5, 5]);
        ctxIn.beginPath();
        // y = -2x. Points: (-75, 150) to (75, -150)
        const p1 = toScreen(-50, 100, inputCanvas);
        const p2 = toScreen(50, -100, inputCanvas);
        ctxIn.moveTo(p1.x, p1.y);
        ctxIn.lineTo(p2.x, p2.y);
        ctxIn.stroke();
        ctxIn.setLineDash([]);

        // Draw Image Line on Output (Range of A)
        // Col1 = (1, 0.5), Col2 = (0.5, 0.25). Span is line y = 0.5x
        ctxOut.strokeStyle = 'purple';
        ctxOut.lineWidth = 2;
        ctxOut.setLineDash([5, 5]);
        ctxOut.beginPath();
        const p3 = toScreen(-140, -70, outputCanvas);
        const p4 = toScreen(140, 70, outputCanvas);
        ctxOut.moveTo(p3.x, p3.y);
        ctxOut.lineTo(p4.x, p4.y);
        ctxOut.stroke();
        ctxOut.setLineDash([]);

        // Draw Input Vector
        drawVector(ctxIn, inputVector.x, inputVector.y, 'blue', 'x');

        // Calculate Output Vector
        const outX = A.a * inputVector.x + A.b * inputVector.y;
        const outY = A.c * inputVector.x + A.d * inputVector.y;

        drawVector(ctxOut, outX, outY, 'red', 'Ax');
    }

    inputCanvas.addEventListener('mousedown', (e) => {
        const rect = inputCanvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const vec = fromScreen(x, y, inputCanvas);
        // Simple hit test
        const dist = Math.hypot(vec.x - inputVector.x, vec.y - inputVector.y);
        if (dist < 20) isDragging = true;
        else {
            inputVector = vec; // Click to move
            render();
        }
    });

    window.addEventListener('mousemove', (e) => {
        if (isDragging) {
            const rect = inputCanvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            inputVector = fromScreen(x, y, inputCanvas);
            render();
        }
    });

    window.addEventListener('mouseup', () => {
        isDragging = false;
    });

    render();
}

function initGramSchmidtDemo(container) {
    container.innerHTML = `
        <div style="display: flex; gap: 20px; height: 100%;">
            <canvas id="${container.id}-canvas" width="600" height="350" style="border: 1px solid #ccc; background: white; width: 100%;"></canvas>
        </div>
        <div style="text-align: center; margin-top: 10px;">
            <button id="${container.id}-step">Next Step</button>
            <button id="${container.id}-reset">Reset</button>
            <p id="${container.id}-status">Start: Two linearly independent vectors v1 (blue) and v2 (green).</p>
        </div>
    `;

    const canvas = document.getElementById(`${container.id}-canvas`);
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    let step = 0;
    const v1 = { x: 150, y: 50 };
    const v2 = { x: 100, y: 150 };
    let u1 = null;
    let proj = null;
    let u2 = null;

    function toScreen(x, y) {
        return { x: x + width / 2 - 100, y: -y + height - 50 }; // Offset origin
    }

    function drawVector(x, y, color, label, fromX = 0, fromY = 0, dashed = false) {
        const start = toScreen(fromX, fromY);
        const end = toScreen(fromX + x, fromY + y);

        ctx.strokeStyle = color;
        ctx.fillStyle = color;
        ctx.lineWidth = 3;
        if (dashed) ctx.setLineDash([5, 5]);
        else ctx.setLineDash([]);

        ctx.beginPath();
        ctx.moveTo(start.x, start.y);
        ctx.lineTo(end.x, end.y);
        ctx.stroke();

        // Label
        ctx.font = '16px sans-serif';
        ctx.fillText(label, end.x + 5, end.y - 5);
        ctx.setLineDash([]);
    }

    function render() {
        ctx.clearRect(0, 0, width, height);

        // Axes
        ctx.strokeStyle = '#ddd';
        const origin = toScreen(0, 0);
        ctx.beginPath(); ctx.moveTo(origin.x, origin.y); ctx.lineTo(origin.x + 300, origin.y); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(origin.x, origin.y); ctx.lineTo(origin.x, origin.y - 300); ctx.stroke();

        drawVector(v1.x, v1.y, 'blue', 'v1');
        drawVector(v2.x, v2.y, 'green', 'v2');

        if (step >= 1) {
            u1 = v1; // Normalize in a real app, but for visual keep scale
            drawVector(u1.x, u1.y, 'red', 'u1 = v1');
        }

        if (step >= 2) {
            // Projection of v2 onto u1
            const dot = (v2.x * u1.x + v2.y * u1.y) / (u1.x**2 + u1.y**2);
            proj = { x: dot * u1.x, y: dot * u1.y };
            drawVector(proj.x, proj.y, '#aaa', 'proj', 0, 0, true);

            // Draw projection line
            const pStart = toScreen(v2.x, v2.y);
            const pEnd = toScreen(proj.x, proj.y);
            ctx.strokeStyle = '#aaa';
            ctx.setLineDash([2, 2]);
            ctx.beginPath(); ctx.moveTo(pStart.x, pStart.y); ctx.lineTo(pEnd.x, pEnd.y); ctx.stroke();
            ctx.setLineDash([]);
        }

        if (step >= 3) {
            u2 = { x: v2.x - proj.x, y: v2.y - proj.y };
            drawVector(u2.x, u2.y, 'red', 'u2', proj.x, proj.y); // Draw from projection tip to v2 tip visually
            // Or draw from origin
            drawVector(u2.x, u2.y, 'orange', 'u2 (final)', 0, 0);
        }
    }

    document.getElementById(`${container.id}-step`).addEventListener('click', () => {
        step++;
        const status = document.getElementById(`${container.id}-status`);
        if (step === 1) status.innerText = "Step 1: Choose u1 = v1.";
        if (step === 2) status.innerText = "Step 2: Project v2 onto u1.";
        if (step === 3) status.innerText = "Step 3: Subtract projection: u2 = v2 - proj. u2 is orthogonal to u1.";
        if (step > 3) step = 3;
        render();
    });

    document.getElementById(`${container.id}-reset`).addEventListener('click', () => {
        step = 0;
        document.getElementById(`${container.id}-status`).innerText = "Start: Two linearly independent vectors.";
        render();
    });

    render();
}
