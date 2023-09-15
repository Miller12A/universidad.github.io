const $formularioCurso = document.getElementById('formularioCurso');
const $txtNombre = document.getElementById('txtNombre');
const btnsEliminacion = document.querySelectorAll('.btnEliminacion');
const $numCreditos = document.getElementById('numCreditos');


(function () {

    notificacionSwal(document.title, "Cursos Listados con Exito", "success", "ok");

    $formularioCurso.addEventListener('submit', function (e) {
        let nombre = String($txtNombre.value).trim();
        if (nombre.length < 3) {
            notificacionSwal(document.title, "El nombre del curso no puede ir vacio", "warning", "ok");
            e.preventDefault();
        } else{
            let creditos = parseInt($numCreditos.value);
            if (creditos < 1 || creditos > 10) {
                notificacionSwal(document.title, "Los creditos deben ser un numero entero entre 1 y 10", "warning", "ok");
                e.preventDefault();
            }
        }
    });

    /*
    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click',function(e) {
            notificacionSwal(document.title, "¿Confirma la eliminacion del curso?", "warning", "ok");
            if(!confirmacion) {
                e.preventDefault();
            }
        })
    });
    */

    btnsEliminacion.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            Swal.fire({
                title: "¿Confirma la eliminacion del curso?",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            });
        });
    });    
})();