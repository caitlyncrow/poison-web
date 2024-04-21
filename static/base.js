//The below 2 lines of code locate all the tabs in the navigation bar by the data-tab-target tag in HTML.
//For example, consider the following line of HTML code: <div id="home" class="section1 active" data-tab-content>.
//Notice, the Home tab has a tag with it called data-tab-content.
const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')


//The below function makes a given tab active when it is clicked on.
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


//The below function first gets the tag from a given link that gets clicked on.
//For instance, consdier the following line of code in HTML: <a data-tab-target="#weaknesses" class = "link">Weaknesses</a>.
//In this case, the tag a[data-tab-target] corresponds to the Weaknesses tab.
//Once the link gets clicked on, the corresponding tab gets located by its tag (i.e. [data-tab-target="tabName"])
//and gets set to active.
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



