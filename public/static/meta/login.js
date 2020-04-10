
$('#loginform').submit(function(event) {
    event.preventDefault()
    $.post($(this).attr('action'), $(this).serialize(), function (data) {
        window.location.href = '/game'
    })
})
