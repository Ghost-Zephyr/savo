const express = require('express')
const app = express()

const userRoute = require('./routes/user')

app.set('view engine', 'pug')

app.get('/', (req, res) => {
    res.render('index.pug', { title: 'home' })
})
app.get('/game', (req, res) => {
    res.render('game.pug', { title: 'game' })
})

app.use(userRoute)

const server = app.listen(8040, () => {
    console.log(`Listening on port: ${server.address().port}`)
})
