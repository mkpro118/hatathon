window.addEventListener('load', changeChat)

function changeChat() {
    const groups_container = document.querySelector('section.chat-rooms')
    const groups = groups_container.querySelectorAll('div.group-tab')
    groups.forEach(group => {
        group.addEventListener('click', event => {
            const name = group.querySelector('span').innerText
            const new_url = `${window.location.origin}\\chat\\${name}`
            window.location.href = new_url
        })
    })
}
