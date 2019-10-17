$.validator.addMethod('validarCorreo', function(value, element) {
    if (!(/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,4})+$/.test(value))) {
        return false;
    } else {
        return true;
    }
}, 'Formato invalido de correo');

$(function() {
    $("#miFormulario").validate({
        rules: {
            nombre: {
                required: true
            },
            apellido: {
                required: true
            },
            mail: {
                required: true,
                validarCorreo: true
            },
            fono: {
                required: true,
                number: true
            },
            mensaje: {
                required: true
            }
        },
        messages: {
            nombre: {
                required: "Por favor ingrese su nombre",
                minlength: "Ingrese más de 3 carácteres."
            },
            apellido: {
                required: "Por favor ingrese su apellido."
            },
            mail: {
                required: "Por favor ingrese un correo",
                validarCorreo: "Formato invalido"
            },
            fono: {
                required: "Por favor ingrese un número de telefono",
                number: "Solo puede ingresar números.",
                maxlength: "No ingrese más de nueve digitos."
            },
            mensaje: {
                required: "Por favor ingrese un mensaje."
            }
        }
    })
})