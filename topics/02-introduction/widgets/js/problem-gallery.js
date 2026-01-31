async function loadProblems() {
  // This widget is served from: /topics/02-introduction/widgets/problem-gallery.html
  // Repo root data lives at: /data/problems-index.json
  const url = "../../../data/problems-index.json";

  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to load problems index (${res.status}) from ${url}`);
  }
  const json = await res.json();
  return Array.isArray(json.problems) ? json.problems : [];
}

function normalizeText(s) {
  return String(s ?? "").toLowerCase().trim();
}

function render(problems, query) {
  const grid = document.getElementById("gallery-grid");
  if (!grid) return;

  const q = normalizeText(query);
  const filtered = q
    ? problems.filter((p) => {
        const hay = [
          p.id,
          p.title,
          p.lecture,
          p.difficulty,
          p.type,
          p.estimatedTime,
        ]
          .map(normalizeText)
          .join(" ");
        return hay.includes(q);
      })
    : problems;

  grid.innerHTML = "";

  if (filtered.length === 0) {
    const empty = document.createElement("div");
    empty.style.opacity = "0.85";
    empty.textContent = "No matching problems.";
    grid.appendChild(empty);
    return;
  }

  filtered.slice(0, 60).forEach((p) => {
    const card = document.createElement("div");
    card.className = "gallery-card";

    const title = document.createElement("h3");
    title.textContent = p.title ?? p.id ?? "Untitled";

    const meta = document.createElement("div");
    meta.className = "category";
    meta.textContent = [
      p.id ? `ID: ${p.id}` : null,
      p.lecture ? `Lecture: ${p.lecture}` : null,
    ]
      .filter(Boolean)
      .join(" · ");

    const details = document.createElement("div");
    details.style.fontSize = "0.9em";
    details.style.opacity = "0.9";
    details.textContent = [
      p.type ? `Type: ${p.type}` : null,
      p.difficulty ? `Difficulty: ${p.difficulty}` : null,
      typeof p.estimatedTime === "number" ? `Est: ${p.estimatedTime} min` : null,
    ]
      .filter(Boolean)
      .join(" · ");

    card.appendChild(title);
    if (meta.textContent) card.appendChild(meta);
    if (details.textContent) card.appendChild(details);

    grid.appendChild(card);
  });
}

async function main() {
  const input = document.getElementById("gallery-search");
  const grid = document.getElementById("gallery-grid");
  if (!grid) return;

  try {
    const problems = await loadProblems();
    render(problems, input?.value ?? "");
    input?.addEventListener("input", () => render(problems, input.value));
  } catch (e) {
    grid.innerHTML = "";
    const err = document.createElement("div");
    err.style.color = "var(--color-danger, #ff5c5c)";
    err.textContent = "Failed to load problem list. Run the site via a local server (see docs/SETUP.md).";
    grid.appendChild(err);
    // eslint-disable-next-line no-console
    console.error(e);
  }
}

main();


