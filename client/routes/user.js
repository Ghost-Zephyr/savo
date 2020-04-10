const router = require('express').Router()

router.get('/register', (req, res) => {
    res.render('meta/register.pug', { title: 'register' })
})
router.get('/login', (req, res) => {
    res.render('meta/login.pug', { title: 'login' })
})

module.exports = router
