const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        console.log(tab)
        const target = document.querySelector(tab.dataset.tabTarget)
        tabContents.forEach(tabContent => {
            tabContent.classList.remove('active')
        })
        tabs.forEach(tab => {
            tab.classList.remove('active')
        })
        tab.classList.add('active')
        target.classList.add('active')
    })
})


document.addEventListener('click', function(event) {
    const target = event.target;
    if (target.matches('a[data-tab-target]')) {
        event.preventDefault();

        const tabTarget = target.getAttribute('data-tab-target');

        const tab = document.querySelector(`[data-tab-target="${tabTarget}"]`);
        if (tab) {
            tab.click();
        }
    }
});



