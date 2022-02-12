const username_field = document.querySelector('#username')
const password_field = document.querySelector('#password')
const login_btn = document.querySelector('.btn')
const error_msg_container = document.querySelector('aside.error-msg')

login_btn.addEventListener('click', login)

function login(event) {
    const u = username_field.value
    const p = password_field.value
    const request_url = `${window.location.origin}/login_user/${u}&${p}`
    fetch(request_url)
    .then(res => res.json())
    .then(data => {
        if (data.successful) {
            window.location = data.next
        }
        else {
            error_msg_container.style.visibility = 'visible'
        }
    })
}

