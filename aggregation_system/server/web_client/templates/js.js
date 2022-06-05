var editor = ace.edit("editor");
editor.getSession().setMode(document.querySelector('#-mode').value);
editor.setTheme("ace/theme/eclipse");
editor.getSession().setTabSize(2);


function changeMode() {
    const editor = ace.edit("editor");
    editor.getSession().setMode(document.querySelector('#-mode').value);
}

function getCookie(name) {
    let cook = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'))
    if (cook != null) {
        return cook[2];
    }
}

function proceed(code) {
    var form = document.createElement('form');
    var button = document.getElementsByClassName("saveSolutionButton")[0];
    button.disabled = true;
    var task_id = window.location.pathname.split('/')[window.location.pathname.split('/').length - 1];

    form.setAttribute('method', 'post');
    form.setAttribute('action', '/request/check/');
    form.style.display = 'hidden';
    document.body.appendChild(form);

    form.submit();
}

function login() {
    $.ajax({
        url: "/login-user",
        type: "GET",
        headers: {
            "user-login": document.querySelector("body > main > section > div.logIn__email > input").value,
            "user-password": document.querySelector("body > main > section > div.form-group > input").value,
        },
        success: function () {
            let type = getCookie("type");
            let tasks = '/tasks';
            if (type === "teacher") {
                tasks = "/teacher" + tasks
            }
            window.location.href = tasks
        },
        error: function () {
            document.getElementById('incorrectPassword').style.visibility = 'visible';
        }
    });
}

function register() {
    $.ajax({
        url: "/sign-up/",
        type: "POST",
        data: {
            "user_name": document.querySelector("body > main > section > div:nth-child(2) > input").value,
            "user_login": document.querySelector("body > main > section > div:nth-child(3) > input").value,
            "user_mail": document.querySelector("body > main > section > div:nth-child(4) > input").value,
            "user_password": document.querySelector("body > main > section > div:nth-child(5) > input").value,
            "user_type": document.querySelector("body > main > section > div:nth-child(6) > select").value,
            "group_name": document.querySelector("body > main > section > div:nth-child(7) > select").value,
        },
        success: function () {
            window.location.href = '/login'
        },
        error: function () {
            alert("Произошла какая-то ошибка сервера ;(")
        }
    });
}

function group_change_by_type() {
    const type = document.querySelector("body > main > section > div:nth-child(6) > select").value;
    if (type === 'teacher') {
        document.querySelector("body > main > section > div:nth-child(7) > select").style.visibility = 'hidden'
    }
    else {
        document.querySelector("body > main > section > div:nth-child(7) > select").style.visibility = 'visible'
    }
}

function reset_password() {
    $.ajax({
        url: "/change-info/",
        type: "POST",
        data: {
            "user_id": getCookie('id'),
            "user_name": document.querySelector("body > section > div > form > div:nth-child(1) > input").value,
            "user_mail": document.querySelector("body > section > div > form > div:nth-child(2) > input").value,
        },
        success: function () {
            setTimeout(function () {
                    location.reload();
                }, 500)
        },
        error: function () {
            alert("Произошла какая-то ошибка сервера ;(")
        }
    });
}

function post_solution() {
    const editor = ace.edit("editor");
    $.ajax('/request/check/',
        {
            type: 'POST',
            data: {
                user_id: "123",
                task_id: window.location.pathname.split('/')[window.location.pathname.split('/').length - 1],
                program_language: editor.getSession().getMode().$id,
                testing_stage: "1",
                code: editor.getValue(),
            },
            success: function (data, status, xhr) {   // success callback function
                alert('Success ' + data.message);
                var ooa = data;
            },
            error: function (jqXhr, textStatus, errorMessage) { // error callback
                alert('Возникла непредвиденная ошибка. Пожалуйста, попробуйте позднее.');
            }
        });
    // setTimeout(5000)

}

function tryGetCheckResult() {
    $.ajax('/request/check/',
        {
            headers: {
                user_id: getCookie("id"),
                task_id: window.location.pathname.split('/')[window.location.pathname.split('/').length - 1],
            },
            success: function (data, status, xhr) {   // success callback function
                alert('Вы успешно решили задачу!');
            },
            error: function (jqXhr, textStatus, errorMessage) { // error callback
                console.log('Error: ' + errorMessage);
                setTimeout(tryGetCheckResult, 17000);
            }
        });
}

function openPopup() {
    const popup = document.querySelector('.popup');
    popup.classList.add('popup_opened');
}

function closePopup() {
    const popup = document.querySelector('.popup');
    popup.classList.remove('popup_opened');
}

function renderGroup() {
    $.ajax('/teacher/add-task',
        {
            type: 'POST',
            data: {
                group_id: document.querySelector("body > section.parts.d-flex.justify-content-start > div.popup.popup_opened > div > form > select").value,
                task_id: window.location.pathname.split('/')[window.location.pathname.split('/').length - 1],
            },
            success: function (data, status, xhr) {   // success callback function
                alert('Группа добавлена');
                setTimeout(function () {
                    location.reload();
                }, 2000)
            },
            error: function (jqXhr, textStatus, errorMessage) { // error callback
                alert('Возникла непредвиденная ошибка. Пожалуйста, попробуйте позднее.');
            }
        });
}

function addNewGroup() {
    event.preventDefault();
    $.ajax('/teacher/add-group',
        {
            type: 'POST',
            data: {
                group_name: document.querySelector("body > section > div.popup.popup_opened > div > form > input").value,
            },
            success: function (data, status, xhr) {   // success callback function
                alert('Группа добавлена');
                setTimeout(function () {
                    location.reload();
                }, 1000)
            },
            error: function (jqXhr, textStatus, errorMessage) { // error callback
                alert('Возникла непредвиденная ошибка. Пожалуйста, попробуйте позднее.');
            }
        });
}
