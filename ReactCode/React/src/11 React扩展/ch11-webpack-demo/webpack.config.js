const path = require('path');

module.exports = {
    entry: './src/welcome.jsx',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    }
};