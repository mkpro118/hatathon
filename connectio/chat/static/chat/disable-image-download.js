document.querySelectorAll('body *:not(div.message):not(script)')
.forEach(e => {
    e.addEventListener('contextmenu', event => {
        event.preventDefault()
    })
})
