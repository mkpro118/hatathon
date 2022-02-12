const group = document.querySelector('span.group-name').innerText
const ws_start = (window.location.protocol === 'https:') ? 'wss://' : 'ws://'
const ws_end = window.location.host + '/chat/' + group

const socket = new WebSocket(ws_start+ws_end)

socket.onopen = event => {}
socket.onerror = event => {}
socket.onclose = event => {}

window.addEventListener('beforeunload', event => {
    socket.close()
})

msg_field.addEventListener('keypress', event => {
    if (event.key === 'Enter') {
        send_msg()
    }
})

const send_btn = document.querySelector('span.send')
send_btn.addEventListener('click', send_msg)

function send_msg() {
    const content = msg_field.value.trim()
        if (content === '') {
            return false
        }

        const author = msg_field.dataset.username
        const group = document.querySelector('span.group-name').innerText
        const data = {
            group,
            author,
            content,
        }

        socket.send(JSON.stringify(data))

        msg_field.value = ''
}

function formatted(time) {
    const datetime = new Date(time)
    const str_time = datetime.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true,
    })
    const formatted_time = str_time.slice(0, 3) + '.' +  str_time.slice(3, -2) + ((str_time.slice(-2) === 'AM') ? 'a.m.' : 'p.m.')
    return formatted_time
}

socket.onmessage = event => {
    const data = JSON.parse(event.data)
    const author = data['author']
    const name = data['name']
    const content = data['content']
    const time = formatted(data['time'])
    const pk = data['pk']

    insert_msg(name, author, content, time, pk)
}
