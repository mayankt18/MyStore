// mobile menu

const burger = document.querySelector('.navbar-burger')
const navbar = document.querySelector('.navbar-link')

burger.addEventListener('click', () =>{
    navbar.classList.toggle('.is-active')
})