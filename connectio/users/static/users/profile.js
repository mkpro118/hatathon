const obscure = document.querySelector('.obscure')
const popupWindow = document.querySelector('aside.popus')
const list_of_events = document.querySelectorAll('table tr:not(:first-of-type)')


list_of_events.forEach(e => e.addEventListener('click', showPopup))

function showPopup(event) {
    obscure.classList.add('active')
    // const day_data = this.
    const location_data =
    const host_data =
    const other_data =
}
