document.addEventListener('DOMContentLoaded', () => {
    let img = document.querySelector('.my-dp')
    img.addEventListener('click', () => {
        window.location = window.location.origin + '/profile'
    })
})
