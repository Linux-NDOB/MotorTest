let d = document;

// Login Form fields and buttons
let user_login_field = d.getElementById("user_login_field");

let user_login_password_field = d.getElementById("login_password_field");

let user_login_button = d.getElementById("user_login_button");

// Register Form

let cedula_field = d.getElementById("cedula");

let nombre_field = d.getElementById("nombre");

let s_nombre_field = d.getElementById("s_nombre");

let apellido_field = d.getElementById("apellido");

let s_apellido_field = d.getElementById("s_apellido");

let f_nacimiento_field = d.getElementById("f_nacimiento");


// Login User
function validate_user() {
    let user_id = user_login_field.value;
    let user_password = user_login_password_field.value;

    if (user_id == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (user_password == '') {
        M.toast({ html: 'Campo de contrasena vacio!' });
    } if (user_id != '' && user_password != '') {
        fetch('http://localhost:8000/api/propietario/'+user_id)
            .then(response => response.json())
            .then(data => {
                if (typeof data.propietario == 'undefined') {
                    M.toast({ html: 'Usuario no registrado en la base de datos!' });
                } else if (user_id == data.propietario.cedula && user_password == data.propietario.contra) {
                    location.href = '/propietario/' + user_id;
                }
                else {
                    M.toast({ html: 'Error en usuario o contrasena!' });
                }
            });
    }
}

function volver_login() {
    location.href = '/home/';
}

function login() {
    location.href = '/login/';
}

function verificar_cedula(cedula) {
    let respuesta = false;

    fetch('http://localhost:8000/api/propietario/' + cedula)
        .then(response => response.json())
        .then(data => {
            if (typeof data.user_account == 'undefined') {
                respuesta = false;
            } else if (user_id == data.user_account.patient_id) {
                respuesta = true;
            } else if (user_id != data.user_account.patient_id) {
                respuesta = false;
            }
        });

    return respuesta;
}


// Register User
function registro() {

    let cedula = parseInt(cedula_field.value);
    let ced = cedula_field.value;
    let t_c = ced.slice(0, 3);
    let nombre = nombre_field.value;
    let t_n = nombre.slice(0, 3);
    let s_nombre = s_nombre_field.value;
    let apellido = apellido_field.value;
    let s_apellido = s_apellido_field.value;
    let f_nacimiento = f_nacimiento_field.value;
    let contra = cedula.toString();

    if (cedula == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (nombre == '') {
        M.toast({ html: 'Campo de nombre vacio!' });
    } if (s_nombre == '') {
        M.toast({ html: 'Campo de s_nombre vacio!' });
    } if (apellido == '') {
        M.toast({ html: 'Campo de apellido vacio!' });
    } if (s_apellido == '') {
        M.toast({ html: 'Campo de s_apellido vacio!' });
    } if (f_nacimiento == '') {
        M.toast({ html: 'Campo de f_nacimiento vacio!' });
    } if (cedula != '' && nombre != '' && s_nombre != '' && apellido != '' && s_apellido != '' && f_nacimiento != '') {
        
        verificar_cedula(cedula);

        if (verificar_cedula(cedula) == false) {
            fetch('http://localhost:8000/api/propietario/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    cedula: cedula,
                    nombre: nombre,
                    s_nombre: s_nombre,
                    apellido: apellido,
                    s_apellido: s_apellido,
                    f_nacimiento: f_nacimiento,
                    contra: generatePassword(),
                }),
            })
                .then(response => {
                    location.href = '/succes/' + cedula;
                })
        } else if (verificar_cedula(cedula) == true) {
            M.toast({ html: 'Cedula ya registrada en la base de datos!' });
        }
    }
}

// Random password
function generatePassword() {
    var length = 8,
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
    return retVal;
}

// Valores de registro
let r_cedula_field = d.getElementById("r_cedula");

let r_nombre_field = d.getElementById("r_nombre");

let r_s_nombre_field = d.getElementById("r_s_nombre");

let r_apellido_field = d.getElementById("r_apellido");

let r_s_apellido_field = d.getElementById("r_s_apellido");

let r_f_nacimiento_field = d.getElementById("r_f_nacimiento");

let r_contra_field = d.getElementById("r_contra");

// Register User
function actualizar() {

    let r_cedula = parseInt(r_cedula_field.value);


    let r_nombre = r_nombre_field.value;

    let r_s_nombre = r_s_nombre_field.value;
    let r_apellido = r_apellido_field.value;
    let r_s_apellido = r_s_apellido_field.value;
    let r_f_nacimiento = r_f_nacimiento_field.value;
    let r_contra = r_contra_field.value;

    if (r_cedula == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (r_nombre == '') {
        M.toast({ html: 'Campo de nombre vacio!' });
    } if (r_s_nombre == '') {
        M.toast({ html: 'Campo de s_nombre vacio!' });
    } if (r_apellido == '') {
        M.toast({ html: 'Campo de apellido vacio!' });
    } if (r_s_apellido == '') {
        M.toast({ html: 'Campo de s_apellido vacio!' });
    } if (r_f_nacimiento == '') {
        M.toast({ html: 'Campo de f_nacimiento vacio!' });
    } if (r_cedula != '' && r_nombre != '' && r_s_nombre != '' && r_apellido != '' && r_s_apellido != '' && r_f_nacimiento != '') {

        fetch('http://localhost:8000/api/propietario/'+r_cedula, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                cedula: r_cedula,
                nombre: r_nombre,
                s_nombre: r_s_nombre,
                apellido: r_apellido,
                s_apellido: r_s_apellido,
                f_nacimiento: r_f_nacimiento,
                contra: r_contra
            }),
        })
            .then(response => {
                M.toast({html: 'Datos Actualizados!'});
                location.href = '/propietario/' + r_cedula;
            })

    }
}
