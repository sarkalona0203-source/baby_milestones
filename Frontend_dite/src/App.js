import React, { useState, useEffect } from "react";
import "./App.css";
import { babyTips } from "./babyTips";

function App() {
  const [dob, setDob] = useState("");
  const [ageMonths, setAgeMonths] = useState(null);
  const [skills, setSkills] = useState([]);
  const [tipsOpen, setTipsOpen] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [nutritionOpen, setNutritionOpen] = useState(false);

  // расчет возраста в месяцах
  const calculateAgeInMonths = (date) => {
    const today = new Date();
    const birth = new Date(date);
    let months =
      (today.getFullYear() - birth.getFullYear()) * 12 +
      (today.getMonth() - birth.getMonth());
    if (today.getDate() < birth.getDate()) months -= 1;
    return months;
  };

  useEffect(() => {
    if (!dob) return;

    const months = calculateAgeInMonths(dob);
    if (months < 0) {
      setAgeMonths(null);
      setSkills([]);
      return;
    }

    setAgeMonths(months);

    fetch(`http://127.0.0.1:8000/api/skills/?age=${months}`)
      .then((res) => res.json())
      .then((data) =>
        setSkills(Array.isArray(data) ? data : data.results || [])
      )
      .catch(() => setSkills([]));
  }, [dob]);

  // группировка советов
  const tipsByCategory = babyTips.reduce((acc, tip) => {
    if (!acc[tip.category]) acc[tip.category] = [];
    acc[tip.category].push(tip);
    return acc;
  }, {});

  // 🍽️ питание по возрасту (без дубликатов)
  const nutrition = skills.reduce(
    (acc, skill) => {
      skill.nutrition_tips?.forEach((tip) => {
        if (tip.type === "warning") acc.warning.push(tip);
        else acc.feeding.push(tip);
      });
      return acc;
    },
    { warning: [], feeding: [] }
  );

  const uniqueByTitle = (arr) =>
    Array.from(new Map(arr.map((t) => [t.title, t])).values());

  const warningTips = uniqueByTitle(nutrition.warning);
  const feedingTips = uniqueByTitle(nutrition.feeding);

  return (
    <div className="App">
      <h1>Vývojové normy dětí 0–5 let</h1>

      {/* Дата + советы */}
      <div className="top-controls">
        <div>
          <p>Zadejte datum narození dítěte:</p>
          <input
            type="date"
            value={dob}
            onChange={(e) => setDob(e.target.value)}
            max={new Date().toISOString().split("T")[0]}
          />
        </div>

        <div className="top-controls">
  <button
    className="primary-btn"
    onClick={() => {
      setTipsOpen(!tipsOpen);
      if (tipsOpen) setSelectedCategory(null);
    }}
  >
    💡 Rady pro rodiče
  </button>

  {ageMonths !== null && (
    <div className="age-badge">
      🍼 {ageMonths} měsíců
    </div>
  )}
</div>
      </div>

      {/* Советы */}
      {tipsOpen && (
        <div className="tips-panel">
          <div className="categories">
            {Object.keys(tipsByCategory).map((cat) => (
              <button
                key={cat}
                className={selectedCategory === cat ? "active" : ""}
                onClick={() => setSelectedCategory(cat)}
              >
                {cat}
              </button>
            ))}
          </div>

          {selectedCategory && (
            <div className="tips-list">
              {tipsByCategory[selectedCategory].map((tip) => (
                <div key={tip.id} className="tip-card">
                  <p><strong>{tip.title}</strong></p>
                  <p>{tip.description}</p>
                  {tip.youtube && (
                    <a href={tip.youtube} target="_blank" rel="noreferrer">
                      ▶ Video
                    </a>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {ageMonths !== null && (
        <p className="age-text">Věk dítěte: {ageMonths} měsíců</p>
      )}

       {/* 🍽️ Питание (один раз) */}
      {(warningTips.length > 0 || feedingTips.length > 0) && (
        <div className="nutrition-wrapper">
          <button
            className="nutrition-toggle"
            onClick={() => setNutritionOpen(!nutritionOpen)}
          >
            🍽️ Výživa podle věku {nutritionOpen ? "▲" : "▼"}
          </button>

          {nutritionOpen && (
            <div className="nutrition-global">
              {warningTips.length > 0 && (
                <div className="nutrition-section warning">
                  <p>⚠️ Upozornění</p>
                  <ul>
                    {warningTips.map((tip, i) => (
                      <li key={i}>
                        <strong>{tip.title}:</strong> {tip.text}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {feedingTips.length > 0 && (
                <div className="nutrition-section feeding">
                  <p>🍽️ Doporučení</p>
                  <ul>
                    {feedingTips.map((tip, i) => (
                      <li key={i}>
                        <strong>{tip.title}:</strong> {tip.text}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Навыки */}
      <div className="skills-container">
        {skills.map((skill) => {
          let status;
          if (ageMonths < skill.min_age_months) status = "Ještě nedošli ⬜";
          else if (ageMonths > skill.max_age_months) status = "Už prošli ✅";
          else status = "Aktuální ⚪";

          return (
            <div key={skill.id} className="skill-card">
              <img
                src={`/icons/${skill.icon}`}
                alt={skill.name}
                className="skill-icon"
                onError={(e) => (e.target.src = "/icons/default.svg")}
              />
              <p className="skill-name">
                {skill.name} — <strong>{status}</strong>
              </p>
              <p className="skill-description">{skill.description}</p>
              {skill.age_range && (
                <p className="skill-age-range">
                  Věk: {skill.age_range}
                </p>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;