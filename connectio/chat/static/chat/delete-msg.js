function delete_msg(event) {
    const pk = parseInt(this.dataset.pk)
    const request_url = `${window.location.origin}/del_msg/${pk}`
    fetch(request_url)
    .then(res => res.json())
    .then(data => {
        if (data.successful) {
            const a = document.querySelector(`div[data-pk="${pk}"]`)
            document.querySelector('section.messages').removeChild(a)
            remove_div()
        }
    })
}

function remove_div() {
    const rem_div = document.querySelector('#delete-msg-box')
    if (rem_div) {
    rem_div.parentNode.removeChild(rem_div)
    }
}

function show_div(event) {
    event.preventDefault()
    event.stopPropagation()
    remove_div()
    const which = event.target
    const a = window.innerWidth
    const div = document.createElement('div')
    // const top = event.pageY - 42
    // const left = ((event.pageX + 200 ) > a) ? (event.pageX + (a - (event.pageX+200))) : event.pageX
    const top = -40
    const right = 0
    div.id = 'delete-msg-box'
    div.style = `
        height: 40px;
        width: 200px;
        position: absolute;
        top: ${top}px;
        right: ${right}px;
        background: hsl(0, 0%, 90%);
        opacity: 0.9;
        font-size: 1.2rem;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    `
    div.addEventListener('mouseover', event => {
        div.style.background = 'hsl(0, 0%, 85%)'
        div.style.opacity = '1.0'
    })
    div.addEventListener('mouseout', event => {
        div.style.background = 'hsl(0, 0%, 90%)'
        div.style.opacity = '0.9'
    })
    div.addEventListener('click', delete_msg)
    div.innerText = 'Delete Message'
    div.dataset.pk = this.dataset.pk
    this.appendChild(div)
    // document.querySelector('.page-container').appendChild(div)

}

document.querySelectorAll('div.message.mine')
.forEach(message => {
    message.addEventListener('contextmenu', show_div, useCapture=true)
})

document.querySelector('section.chats')
.addEventListener('click', remove_div)
