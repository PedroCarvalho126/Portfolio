let btnMenu = document.getElementById('btn_menu');
let menuMobile = document.getElementById('menu_mobile');
let overlay = document.getElementById('overlay_menu');

btnMenu.addEventListener('click', () => {
  menuMobile.classList.add('abrir_menu');
});

menuMobile.addEventListener('click', () => {
  menuMobile.classList.remove('abrir_menu');
});

overlay.addEventListener('click', () => {
  menuMobile.classList.remove('abrir_menu');
});