const msg_field = document.querySelector('input[placeholder^="W"]')

function insert_msg(name, username, content, time, pk) {
    const div = document.createElement('div')
    const em = document.createElement('em')
    const small1 = document.createElement('small')
    const p = document.createElement('p')
    const small2 = document.createElement('small')
    div.classList.add('message')
    div.classList.add((msg_field.dataset.username === username) ? 'mine' : 'other')
    em.classList.add('author')
    small1.style = 'color:hsl(0 0% 40%);'
    p.classList.add('message-text')
    small2.classList.add('time')
    p.innerText = content
    small2.innerText = time
    if (name !== 'anonymous') {
        em.innerText = name
        small1.innerText = ` ~ @${username}`
        em.appendChild(small1)
    }
    else {
        em.innerText = `@${username}`
    }
    div.appendChild(em)
    div.appendChild(p)
    div.appendChild(small2)
    div.dataset.pk = pk
    div.addEventListener('contextmenu', show_div, useCapture=true)
    const first = document.querySelector('.messages')
    first.insertBefore(div, first.firstElementChild)
}
