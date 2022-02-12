const obscure = document.querySelector('.obscure')
const popupWindow = document.querySelector('aside.popup')
const list_of_events = document.querySelectorAll('table tr:not(:first-of-type)')


list_of_events.forEach(e => e.addEventListener('click', showPopup))
obscure.addEventListener('click', hidePopup)

function showPopup(event) {
    obscure.classList.add('active')
    const title_data = this.dataset.title
    const date_data = this.dataset.date
    const location_data = this.dataset.location
    const host_data = this.dataset.host
    const description_data = this.dataset.description
    const attendance_data = this.dataset.attendance
    const cost_data = this.dataset.cost
    const capacity_data = this.dataset.capacity

    popupWindow.querySelector('.title-info').textContent = title_data
    popupWindow.querySelector('.dt-data').textContent = date_data
    popupWindow.querySelector('.lc-data').textContent = location_data
    popupWindow.querySelector('.ht-data').textContent = host_data
    console.log(popupWindow.querySelector('.ht-data').nodeName)
    if (popupWindow.querySelector('.ht-data').nodeName.toLowerCase() === 'a') {
        popupWindow.querySelector('.ht-data').href = `${window.location.origin}/chat/${host_data}`
    }
    popupWindow.querySelector('.event-description').textContent = description_data
    popupWindow.querySelector('.event-attendance').textContent = attendance_data
    popupWindow.querySelector('.event-capacity').textContent = capacity_data
    popupWindow.querySelector('.event-cost').textContent = cost_data
    popupWindow.classList.add('display-active')
}

function hidePopup(event) {
    event.stopPropagation()
    if (event.target != this) {
        return
    }
    popupWindow.classList.remove('display-active')
    obscure.classList.remove('active')
}
