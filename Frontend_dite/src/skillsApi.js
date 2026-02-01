const API_URL = process.env.REACT_APP_API_URL;

export const getSkillsAndNutrition = (age) => {
  return fetch(`${API_URL}/skills/?age=${age}`)
    .then((res) => res.json());
};