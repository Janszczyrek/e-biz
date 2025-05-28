/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Include all JS, JSX, TS, and TSX files in the src folder
    "./public/index.html"       // Include your main HTML file if you use Tailwind classes there
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}