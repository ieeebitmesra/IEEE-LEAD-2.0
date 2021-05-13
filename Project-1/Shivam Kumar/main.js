function menuActivator(){
    const menubar = document.querySelector('.menubar');
    const menu = document.querySelector('.menu');
    const menuItems = document.querySelectorAll('.menu li');
    const contents = document.querySelectorAll('.content');

    menubar.addEventListener('click', () => {
        menu.classList.toggle('activate');
        menubar.classList.toggle('cross');
        menuItems.forEach(item => {
            item.classList.toggle('animatebar');
        });
    });

}

menuActivator();

function viewactive() {
    const viewbtn = document.querySelector('.view');
    const less = document.querySelector('.viewless');
    const more = document.querySelector('.viewmore');

    more.addEventListener('click', () => {
        viewbtn.classList.add('btnevent');
    });

    less.addEventListener('click', () => {
        viewbtn.classList.remove('btnevent');
    });
}

viewactive();