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


function safe_login_user() {
    console.log('safe_login_user');
    if (user_login_field.value != '' && user_login_password_field.value != '') {
        console.log('valid');
        user_login_button.disabled = false;
    } else {
        console.log('invalid');
        user_login_button.disabled = true;
    }

}

// Login User
function validate_user() {
    let user_id = user_login_field.value;
    let user_password = user_login_password_field.value;

    if (user_id == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (user_password == '') {
        M.toast({ html: 'Campo de contrasena vacio!' });
    } if (user_id != '' && user_password != '') {
        fetch('http://localhost:8000/api/propietario/' + user_id)
            .then(response => response.json())
            .then(data => {
                if (typeof data.user_account == 'undefined') {
                    M.toast({ html: 'Usuario no registrado en la base de datos!' });
                } else if (user_id == data.user_account.patient_id && user_password == data.user_account.user_password) {
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
    let cedula = cedula_field.value;
    let nombre = nombre_field.value;
    let s_nombre = s_nombre_field.value;
    let apellido = apellido_field.value;
    let s_apellido = s_apellido_field.value;
    let f_nacimiento = f_nacimiento_field.value;

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
            fetch('http://localhost:8000/api/propietario/' + cedula, {
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
                }),
            })
                .then(response => {
                    location.href = '/propietario/' + cedula;
                })
        } else if (verificar_cedula(cedula) == true) {
            M.toast({ html: 'Cedula ya registrada en la base de datos!' });
        }
    }
}

 // Patient List
 const renderPost = (posts) => {
    posts.forEach((post) => {
        output += `
      <div class="card mt-4 col-md-6 bg-ligt ">
        <img src=${post.url} class="" alt="" width="100%" 
        height="400"">
        <div class="card-body" data-id=${post.id}>
          <h5 class="card-title name">${post.name}</h5>
          <h6 class="card-subtitle mb-2 text-muted price">${post.price}</h6>
          <p class="card-title desc">${post.description}</p>
          <p class="card-title url">${post.url}</p>
          <a href="#" class="btn btn-primary" id="edit-post">Editar</a>
          <a href="#" class="btn btn-primary" id="delete-post">Eliminar</a>
        </div>
      </div>
`;
    });
    $postList.innerHTML = output;
};

fetch('aasas')
    .then((res) => res.json())
    .then((data) => renderPost(data));
