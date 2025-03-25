// static/js/admin_user_toggle.js
document.addEventListener('DOMContentLoaded', function() {
    const isStudent = document.querySelector('#id_is_student');
    const isTeacher = document.querySelector('#id_is_teacher');

    if (isStudent && isTeacher) {
        // Función para deseleccionar el otro campo
        function toggleRoles() {
            if (this.checked) {
                if (this === isStudent) {
                    isTeacher.checked = false;
                } else {
                    isStudent.checked = false;
                }
            }
        }

        // Escuchar cambios en ambos campos
        isStudent.addEventListener('change', toggleRoles);
        isTeacher.addEventListener('change', toggleRoles);
    }
});