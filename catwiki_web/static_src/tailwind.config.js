// This is a minimal config.
// If you need the full config, get it from here:
// https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
module.exports = {
    content: [
        // Templates within theme app (e.g. base.html)
        '../templates/**/*.html',
        // Templates in other apps. Uncomment the following line if it matches
        // your project structure or change it to match.
        // '../../templates/**/*.html',
    ],
    theme: {
        colors: {
            primary: '#DEC68B',
            secondary: '#704b25',
            black: '#000000',
            white: '#FFFFFF',
            gray: '#dedede'
        },
        fontSize: {
            'xs': '0.75rem',
            'sm': '1rem',
            'base': '1.2rem',
            'md': '1.5rem',
            'lg': '2rem',
            'xl': '4rem',
        },
        fontFamily: {
            sans: ['Montserrat', 'sans-serif'],
        },
        container: {
          padding: {
            // DEFAULT: '1rem',
            sm: '2rem',
            lg: '4rem',
            xl: '5rem',
            '2xl': '10rem',
          },
        },
        extend: {
        }
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
