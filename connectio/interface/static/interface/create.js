const continue_btn = document.querySelector('section.continue-1 > button')
const create_btn = document.querySelector('section.continue-2 > button')
const side1 = document.querySelector('section.side1')
const side2 = document.querySelector('section.side2')
const title_field = document.querySelector('input#title')
const date_field = document.querySelector('input#date')
const location_field = document.querySelector('input#location')
const description_field = document.querySelector('textarea#description')
const count_field = document.querySelector('input#count')
const capacity_field = document.querySelector('input#capacity')
const cost_field = document.querySelector('input#cost')
const error_msg_container = document.querySelector('aside.error-msg')

const error_msgs = {
    empty: 'Please fill out all fields',
}

continue_btn.addEventListener('click', continueClick)
create_btn.addEventListener('click', create)

function continueClick(event) {
    if (!title_field.value || !date_field.value || !location_field.value || !description_field.value) {
        error_msg_container.textContent = error_msgs.empty
        error_msg_container.style.visibility = 'visible'
        return
    }
    error_msg_container.style.visibility = 'hidden'
    side1.classList.remove('active')
    side2.classList.add('active')
}

function create() {
    if (!count_field.value || !capacity_field.value || !cost_field.value) {
        error_msg_container.textContent = error_msgs.empty
        error_msg_container.style.visibility = 'visible'
        return
    }
    error_msg_container.style.visibility = 'hidden'

    const t = title_field.value
    const d = date_field.value
    const l = location_field.value
    const de = description_field.value
    const ct = count_field.value
    const cp = capacity_field.value
    const cs = cost_field.value
    const request_url = `${window.location.origin}/create_event/${t}&&${d}&&${l}&&${de}&&${ct}&&${cs}&&${cp}`
    fetch(request_url).then(res => res.json()).then(data => {window.location.href = data.next})
}
