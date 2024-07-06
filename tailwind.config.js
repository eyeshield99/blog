/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
const plugin = require('tailwindcss/plugin');

module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#1E3A5F",
        secondary: "#2A2A2A",
        accent: "#7FA7B8",
        "base-100": "#0A0A0B",
        "base-content": "#F6F6F6",
      },
      transitionProperty: {
        height: "height",
      },
      fontFamily: {
        sans: ['"Roboto"', ...defaultTheme.fontFamily.sans],
        serif: ['"Merriweather"', ...defaultTheme.fontFamily.serif],
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        fadeUp: {
          '0%': { opacity: 0, transform: 'translateY(100%)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
        fadeRight: {
          '0%': { opacity: 0, transform: 'translateX(-50%)' },
          '100%': { opacity: 1, transform: 'translateX(0)' },
        },
        fadeLeft: {
          '0%': { opacity: 0, transform: 'translateX(50%)' },
          '100%': { opacity: 1, transform: 'translateX(0)' },
        },
        scaleUp: {
          '0%': { opacity: 0, transform: 'scale(0)' },
          '100%': { opacity: 1, transform: 'scale(1)' },
        },
      },
      animation: {
        fadeIn: 'fadeIn 2s forwards',
        fadeUp: 'fadeUp 1s forwards',
        fadeRight: 'fadeRight 1.5s forwards',
        fadeLeft: 'fadeLeft 1.5s forwards',
        scaleUp: 'scaleUp 1.5s forwards',
      },
      animationDuration: {
        default: '2s',
      },
    },
  },
  plugins: [
    plugin(({ matchUtilities, theme }) => {
      matchUtilities(
        {
          "animation-delay": (value) => {
            return {
              "animation-delay": value,
            };
          },
        },
        {
          values: theme("transitionDelay"),
        }
      );
    }),
  ],
};
