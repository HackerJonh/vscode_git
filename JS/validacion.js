//SELECCIONAR EL FORMULARIO

//1-Conociendo el id

var formulario = document.getElementById("miFormulario");
//var formulario=document.forms["miFormulario"];

//2-Conociendo el Numero de formulario que es en la Pagina

//var formulario2 = document.getElementsByTagName("form")[0];
//var formulario3 = document.forms[0];

//SELECCIONAR ELEMENTOS DE UN FORMULARIO:

//.elements[]: Devuelve un array con todos los inputs del formulario

//getElementById(): devuelve un elemento con un id determinado

//getElementsByTagName(): devuelve un array con elementos de tipo etiqueta

//getElementsByName(): Devuelve un array con elementos que tienen el mismo nombre


window.onload = iniciar;

function iniciar() {
    document.getElementById("enviar").addEventListener("click", validar, false);
}

//Validacion de elementos

function validaNombre() {
    var elemento = document.getElementById("nombre");
    if (elemento.value == "") {
        alert("El campo nombre no puede estar Vacio");
        Error(elemento);
        return false;
    }
    return true;
}

function validaTelefono() {
    var elemento = document.getElementById("telefono");
    if (isNaN(elemento.value)) {
        alert("El campo telefono tiene que ser Numerico");
        return false;
    }
    return true;
}

function validaFecha() {
    var dia = document.getElementById("dia").value;
    var mes = document.getElementById("mes").value;
    var ano = document.getElementById("ano").value;

    var fecha = new Date(ano, mes, dia);
    if (isNaN(fecha)) {
        alert("Los Campos de fecha son incorrectos");
        return false;

    }
    return true;
}

function validaCheck() {
    var campoCheck = document.getElementById("mayor");
    if (!campoCheck.checked) {
        alert("Debes ser mayor de edad");
        return false;

    }
    return true;
}

//Funcion para unir todas las Validaciones anteriormente le he nombrado validar

function validar(e) {
    if (validaNombre() && validaTelefono() && validaFecha() && validaCheck() && confirm("Pulsa Aceptar si deseas enviar el formulario")) {
        return true;
    } else {
        e.preventDefault();
        return false;
    }
}

function Error(elemento) {
    elemento.className = "error";
    elemento.focus();
    
}

function limpiarError() {
    elemento.className = "";
}