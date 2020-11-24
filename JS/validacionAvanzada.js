window.onload = iniciar;

function iniciar() {
    document.getElementById("enviar").addEventListener("click", validar, false);

}

//Funciones de Validacion

function validarNombre() {
    var elemento = document.getElementById("nombre");
    if (!elemento.checkValidity()) {
        error(elemento);
        return false;
    }
    return true;
}

function validaEdad() {
    var elemento = document.getElementById("edad");
    if (!elemento.checkValidity()) {
        error(elemento);
        return false;
    }
    return true;
}

function validaTelefono() {
    var elemento = document.getElementById("telefono");
    if (!elemento.checkValidity()) {
        error(elemento);
        return false;
    }
    return true;
}
function validar(elemento) {
    borrarError();
    if (validarNombre() && validaEdad() && validaTelefono() && confirm("Pulsa Aceptar si quieres enviar el formulario")) {
        return true;
    } else {
        elemento.preventDefault();
        return false;
    }
}
function error(elemento) {
    document.getElementById("mensajeError").innerHTML = elemento.validationMessage;
    elemento.className = "error";
    elemento.focus();
}

function borrarError() {
    var formulario = document.forms[0];
    for (var i = 0; i < formulario.elements.length; i++){
        formulario.elements[i].className = "";
    }
}