/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './questions/templates/**/*.html',
    './questions/templates/*.html',
    './questions/static/js/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

