var burger = document.querySelector('.burger');
var navList = document.querySelector('#'+burger.dataset.target);

burger.addEventListener('click', () => {
    burger.classList.toggle('is-active');
    navList.classList.toggle('is-active');
})