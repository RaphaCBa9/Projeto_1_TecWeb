function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const corpo = document.querySelector('body');
const appbar = document.querySelector('.appbar');
const notas = document.querySelectorAll('.card');
const titulos = document.querySelectorAll('.card-title');
const detalhes = document.querySelectorAll('.card-content');
const formulario = document.querySelector('.form-card');
const titulo_formulario = document.querySelector('.form-card-title');
const formAutoresize = document.querySelector('.autoresize');
const nightmode = document.querySelector('#night-mode-toggle');


const NIGHT_MODE_KEY = 'night-mode';

function toggleNightMode() {
    corpo.classList.toggle('night-mode');
    appbar.classList.toggle('night-mode');
    notas.forEach(card => card.classList.toggle('night-mode'));
    titulos.forEach(title => title.classList.toggle('night-mode'));
    detalhes.forEach(content => content.classList.toggle('night-mode'));
    formulario.classList.toggle('night-mode');
    titulo_formulario.classList.toggle('night-mode');
    formAutoresize.classList.toggle('night-mode');
    nightmode.classList.toggle('night-mode');
}


const nightModeEnabled = localStorage.getItem(NIGHT_MODE_KEY) === 'true';

if (nightModeEnabled) {
    toggleNightMode();
}

document.querySelector('#night-mode-toggle').addEventListener('click', () => {
    toggleNightMode();
    localStorage.setItem(NIGHT_MODE_KEY, corpo.classList.contains('night-mode'));
});

document.addEventListener("DOMContentLoaded", function () {
    // Faz textarea aumentar a altura automaticamente
    let textareas = document.getElementsByClassName("autoresize");
    for (let i = 0; i < textareas.length; i++) {
        let textarea = textareas[i];
        function autoResize() {
            this.style.height = "auto";
            this.style.height = this.scrollHeight + "px";
        }

        textarea.addEventListener("input", autoResize, false);
    }

    // Sorteia classes de cores aleatoriamente para os cards
    let cards = document.getElementsByClassName("card");
    for (let i = 0; i < cards.length; i++) {
        let card = cards[i];
        card.className += ` card-color-${getRandomInt(
            1,
            5
        )} card-rotation-${getRandomInt(1, 11)}`;
    }
});
