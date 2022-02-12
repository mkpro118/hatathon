const continue_btn = document.querySelector('section.continue-1 > button')
const side1 = document.querySelector('section.side1')
const side2 = document.querySelector('section.side2')
const username_field = document.querySelector('input#username')
const email_field = document.querySelector('input#email')
const pswd_field = document.querySelector('input#password')
const pswd_again_field = document.querySelector('input#confirm-password')
const _location_field = document.querySelector('input#location')
const bio_field = document.querySelector('input#bio')
const error_msg_container = document.querySelector('aside.error-msg')

const error_msgs = {
    empty: 'Please fill out all fields',
    username: 'Sorry, that username is taken ☹️',
    password: 'The passwords do not match',
    email: 'Invalid email',
}

continue_btn.addEventListener('click', continueClick)
pswd_field.addEventListener('mouseover', showPswd)
pswd_field.addEventListener('mouseleave', hidePswd)
pswd_again_field.addEventListener('mouseover', showPswd)
pswd_again_field.addEventListener('mouseleave', hidePswd)

function showPswd(event) {this.type = 'text'}
function hidePswd(event) {this.type = 'password'}

function continueClick(event) {
    if (!username_field.value || !email_field.value || !pswd_field.value || !pswd_again_field.value) {
        error_msg_container.textContent = error_msgs.empty
        error_msg_container.style.visibility = 'visible'
        return
    }
    const validity = checkValidity1()
    if (!validity.is_valid) {
        if (!validity.valid_username) {
            error_msg_container.textContent = error_msgs.username
        }
        else if (!validity.password_match) {
            error_msg_container.textContent = error_msgs.password
        }
        else if (!validity.valid_email) {
            error_msg_container.textContent = error_msgs.email
        }
        error_msg_container.style.visibility = 'visible'
        return
    }
    side1.classList.remove('active')
    side2.classList.add('active')
}

function checkValidity1() {
    const valid_username = check_availability()
    console.log(`valid_username: ${valid_username}`)
    const password_match = check_pswd_match()
    console.log(`password_match: ${password_match}`)
    const valid_email = check_email()
    console.log(`valid_email: ${valid_email}`)
    return {
        valid_username,
        password_match,
        valid_email,
        is_valid: valid_username && password_match && valid_email,
    }
}

function check_availability() {
    const username = username_field.value
    const request_url = `${window.location.origin}/check_username_availablility/${username}`
    return fetch(request_url)
    .then(res => res.json())
    .then(data => data.taken)
}

function check_pswd_match() {return pswd_field.value === pswd_again_field.value}
function check_email() {return !!email_field && !!email_field.value.match(/^[\w]+@{1}[\w]+\.{1}[\w]+$/)}
