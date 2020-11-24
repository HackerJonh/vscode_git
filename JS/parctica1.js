window.onload = iniciar;

function iniciar() {
    document.getElementById("cambio").addEventListener("click", cambiarMsj, false);
}

function cambiarMsj() {
    var elemento = document.getElementById("cambio");
    elemento.innerHTML = "He Cambiado mucho";
}