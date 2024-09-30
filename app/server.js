const express = require('express');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const URL = process.env.API_URL;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/config', (req, res) => {
    res.json({ apiUrl: URL });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});