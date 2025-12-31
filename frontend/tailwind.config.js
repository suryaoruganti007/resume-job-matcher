/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#6366f1",   // Indigo
          light: "#818cf8",
          dark: "#4f46e5"
        },
        secondary: {
          DEFAULT: "#06b6d4",   // Cyan
          light: "#67e8f9",
          dark: "#0891b2"
        },
        accent: {
          DEFAULT: "#f43f5e",   // Rose
          light: "#fb7185",
          dark: "#e11d48"
        },
        background: "#0f172a", // Slate-900
        surface: "#020617",    // Dark cards
        muted: "#94a3b8",
      },

      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui"],
      },

      boxShadow: {
        soft: "0 10px 25px -5px rgba(0,0,0,0.15)",
        glow: "0 0 20px rgba(99,102,241,0.4)",
        card: "0 15px 40px rgba(0,0,0,0.25)",
      },

      borderRadius: {
        xl: "1rem",
        "2xl": "1.25rem",
      },

      backgroundImage: {
        "gradient-primary":
          "linear-gradient(135deg, #6366f1 0%, #06b6d4 100%)",
        "gradient-accent":
          "linear-gradient(135deg, #f43f5e 0%, #f97316 100%)",
      },

      animation: {
        fade: "fadeIn 0.6s ease-out",
        float: "float 4s ease-in-out infinite",
      },

      keyframes: {
        fadeIn: {
          "0%": { opacity: "0", transform: "translateY(10px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-6px)" },
        },
      },
    },
  },
  plugins: [],
};

