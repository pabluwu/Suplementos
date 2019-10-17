let boton = document.getElementById("icono");
let enlaces = document.getElementById("enlaces");
let contador = 0;
let carrusel = document.getElementById("carrusel");
let texto = document.getElementById("texto");
let end = document.getElementById("piePagina");

boton.addEventListener("click", function() {
    if (contador == 0) {
        enlaces.className = ('enlaces dos');
        contador++;
    } else {
        enlaces.classList.remove('dos');
        enlaces.className = ('enlaces uno');
        contador = 0;
    }
})

window.addEventListener('resize', function() {
    if (screen.width > 750) {
        contador = 0;
        enlaces.classList.remove('dos');
        enlaces.className = ('enlaces uno col-xs-12 col-sm-8 col-md-8 col-lg-8');

    }
})