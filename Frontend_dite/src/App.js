import React, { useState, useEffect } from "react";
import "./App.css";
import { babyTips } from "./babyTips";

function App() {
  const [dob, setDob] = useState("");
  const [ageMonths, setAgeMonths] = useState(null);
  const [skills, setSkills] = useState([]);
  const [tipsOpen, setTipsOpen] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [nutrition, setNutrition] = useState({ warning: [], feeding: [] });
  const [nutritionOpen, setNutritionOpen] = useState(false);

  // Расчет возраста в месяцах
  const calculateAgeInMonths = (date) => {
    const today = new Date();
    const birth = new Date(date);
    let months =
      (today.getFullYear() - birth.getFullYear()) * 12 +
      (today.getMonth() - birth.getMonth());
    if (today.getDate() < birth.getDate()) months -= 1;
    return months;
  };

  // Получение навыков и питания с сервера при выборе даты
  useEffect(() => {
  if (!dob) return;

  const months = calculateAgeInMonths(dob);
  if (months < 0) {
    setAgeMonths(null);
    setSkills([]);
    setNutrition({ warning: [], feeding: [] });
    return;
  }

  setAgeMonths(months);

  const fetchData = async () => {
    try {
      const res = await fetch(`${process.env.REACT_APP_API_URL}?age=${months}`);
      if (!res.ok) throw new Error(`Ошибка: ${res.status}`);
      const data = await res.json();

      setSkills(data.skills || []);

      const grouped = { warning: [], feeding: [] };
      (data.nutrition || []).forEach((tip) => {
        if (tip.type === "warning") grouped.warning.push(tip);
        else grouped.feeding.push(tip);
      });
      setNutrition(grouped);

    } catch (err) {
      console.error("Ошибка fetch:", err);
      setSkills([]);
      setNutrition({ warning: [], feeding: [] });
    }
  };

  fetchData();
}, [dob]);
  // Группировка советов по категориям
  const tipsByCategory = babyTips.reduce((acc, tip) => {
    if (!acc[tip.category]) acc[tip.category] = [];
    acc[tip.category].push(tip);
    return acc;
  }, {});

  return (
    <div className="App">
      <h1>Vývojové normy dětí 0–5 let</h1>

      {/* Дата рождения и кнопка советов */}
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
            <div className="age-badge">🍼 {ageMonths} měsíců</div>
          )}
        </div>
      </div>

      {/* Советы по категориям */}
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
                  <p>
                    <strong>{tip.title}</strong>
                  </p>
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

      {/* Текст с возрастом */}
      {ageMonths !== null && (
        <p className="age-text">Věk dítěte: {ageMonths} měsíců</p>
      )}

      {/* 🍽️ Питание */}
      {(nutrition.warning.length > 0 || nutrition.feeding.length > 0) && (
        <div className="nutrition-wrapper">
          <button
            className="nutrition-toggle"
            onClick={() => setNutritionOpen(!nutritionOpen)}
          >
            🍽️ Výživa podle věku {nutritionOpen ? "▲" : "▼"}
          </button>

          {nutritionOpen && (
            <div className="nutrition-global">
              {nutrition.warning.length > 0 && (
                <div className="nutrition-section warning">
                  <p>⚠️ Upozornění</p>
                  <ul>
                    {nutrition.warning.map((tip, i) => (
                      <li key={i}>
                        <strong>{tip.title}:</strong> {tip.text}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {nutrition.feeding.length > 0 && (
                <div className="nutrition-section feeding">
                  <p>🍽️ Doporučení</p>
                  <ul>
                    {nutrition.feeding.map((tip, i) => (
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
        {skills.length > 0 ? (
          skills.map((skill) => {
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
                <p className="skill-age-range">
                  Věk: {skill.min_age_months}–{skill.max_age_months} měsíců
                </p>
              </div>
            );
          })
        ) : (
          <p className="no-skills">
            Žádné aktuální dovednosti pro tento věk. Zkuste zadat jiný věk
            nebo později.
          </p>
        )}
      </div>
    </div>
  );
}

export default App;