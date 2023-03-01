/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      spacing: {
        104: '27rem',
      },
      colors: {
        'light-grey': '#6B6B6B',
        primary: '#2690FF',
        secondary: '#4FC3F7',
        overlay: '#B8B8B8CC',
      },
      borderRadius: {
        '4xl': 34,
        '5xl': 37,
        '6xl': 42,
      },
    },
  },

  plugins: [],
}
