/*function verificarPasswords() {
 
    pass1 = document.getElementById('contraseña'); 
    pass2 = document.getElementById('confirmar_contraseña'); 

    if (pass1.value != pass2.value) {
        document.getElementById("ok").classList.add("ocultar");
        document.getElementById("error").classList.add("mostrar");
        
    }else if(pass1.value=="" | pass2==""){
        document.getElementById("ok").classList.add("ocultar");
        document.getElementById("error").classList.remove("mostrar");
    }

    else{
        document.getElementById("error").classList.remove("mostrar");
        document.getElementById("ok").classList.remove("ocultar");
    }
 
}*/

formulario = document.getElementById('formularioRegistrar');

formulario.addEventListener("submit", (e) => {
    pass1 = document.getElementById('contraseña'); 
    pass2 = document.getElementById('confirmar_contraseña');

    if (pass1.value !== pass2.value) {
        e.preventDefault();
        document.getElementById("error").classList.add("mostrar");
    }else if(pass1.value=="" | pass2==""){
        document.getElementById("ok").classList.add("ocultar");
        document.getElementById("error").classList.remove("mostrar");
    }
    else{
        document.getElementById("error").classList.remove("mostrar");
        document.getElementById("ok").classList.remove("ocultar");
    }
});
