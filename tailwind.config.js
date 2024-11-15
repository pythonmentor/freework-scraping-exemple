/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./frontend/src/**/*.{js,jsx,ts,tsx,css,scss,html}",
    "./freework/templates/**/*.{js,jsx,ts,tsx,css,scss,html}",
    "./.venv/**/crispy_tailwind/**/*.{js,jsx,ts,tsx,css,scss,html}"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

