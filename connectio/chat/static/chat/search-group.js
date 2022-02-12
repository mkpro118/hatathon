const grps = document.querySelectorAll('div.group-tab')

document.querySelector('input[placeholder="Search..."]')
.addEventListener('keyup', function(event) {
    const val = this.value.toLowerCase()
    if (val === '') {
        grps.forEach(e => {
            e.style.display = 'flex'
        })
    }
    grps.forEach(e => {
        const grp_name_span = e.querySelector('span')
        const grp_name = grp_name_span.innerText.toLowerCase()
        if (!grp_name.includes(val)) {
            e.style.display = 'none'
        }
        else {
            e.style.display = 'flex'
        }
    })
})
