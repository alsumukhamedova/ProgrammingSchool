var editor = ace.edit("editor");
editor.getSession().setMode(document.querySelector('#-mode').value);
editor.setTheme("ace/theme/eclipse");
editor.getSession().setTabSize(2);

function changeMode() {
    const editor = ace.edit("editor");
    editor.getSession().setMode(document.querySelector('#-mode').value);
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
       success: function() {
           window.location.href='/profile_edit'
       },
       error: function() {
           document.getElementById('incorrectPassword').style.visibility = 'visible';
       }
    });
}

function register() {
    $.ajax({
       url: "/sign-up/",
       type: "POST",
       data: {
           "user-name": document.querySelector("body > main > section > div:nth-child(2) > input").value,
           "user-login": document.querySelector("body > main > section > div:nth-child(3) > input").value,
           "user-password": document.querySelector("body > main > section > div:nth-child(4) > input").value,
           "teacher-link": document.querySelector("body > main > section > div:nth-child(5) > input").value,
           "user-type": document.querySelector("body > main > section > div:nth-child(6) > input").value,
       },
       success: function() {
           window.location.href='/login'
       },
       error: function() {
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
          user_id : "123",
          task_id : window.location.pathname.split('/')[window.location.pathname.split('/').length - 1],
          program_language : editor.getSession().getMode().$id,
          testing_stage : "1",
      },
      success: function (data,status,xhr) {   // success callback function
         alert('Success ' + data.message);
         var ooa = data;
      },
      error: function (jqXhr, textStatus, errorMessage) { // error callback
        alert('Возникла непредвиденная ошибка. Пожалуйста, попробуйте позднее.');
      }
    });
  // setTimeout(5000)
  // $.ajax('/request/check/',
  //   {
  //     data: {
  //         user_id : "123",
  //         task_id : window.location.pathname.split('/')[window.location.pathname.split('/').length - 1],
  //         program_language : editor.getSession().getMode().$id,
  //         testing_stage : "1",
  //     },
  //     success: function (data,status,xhr) {   // success callback function
  //        alert('Success ' + data.message);
  //        var ooa = data;
  //     },
  //     error: function (jqXhr, textStatus, errorMessage) { // error callback
  //       alert('Возникла непредвиденная ошибка. Пожалуйста, попробуйте позднее.');
  //     }
  //   });
}
