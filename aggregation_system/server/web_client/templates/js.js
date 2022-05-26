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
                setTimeout(tryGetCheckResult, 5000);
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
    $.ajax('add-group',
        {
            type: 'POST',
            data: {
                group_name: document.querySelector('.popup__input').value,
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
