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
           window.location.href='/tasks'
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
           "user_name": document.querySelector("body > main > section > div:nth-child(2) > input").value,
           "user_login": document.querySelector("body > main > section > div:nth-child(3) > input").value,
           "user_mail": document.querySelector("body > main > section > div:nth-child(4) > input").value,
           "user_password": document.querySelector("body > main > section > div:nth-child(5) > input").value,
           "user_type": document.querySelector("body > main > section > div:nth-child(6) > select").value,
           "group_name": document.querySelector("body > main > section > div:nth-child(7) > select").value,
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
          code: editor.getValue(),
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

}
function tryGetCheckResult() {
  $.ajax('/request/check/',
    {
      headers: {
          user_id : document.cookie.match(new RegExp('(^| )id=([^;]+)'))[2],
          task_id : window.location.pathname.split('/')[window.location.pathname.split('/').length - 1],
      },
      success: function (data,status,xhr) {   // success callback function
         alert('Вы успешно решили задачу!');
      },
      error: function (jqXhr, textStatus, errorMessage) { // error callback
          console.log('Error: ' + errorMessage);
          setTimeout(tryGetCheckResult, 5000);
      }
    });
}
// const popup = document.querySelector('.popup');
// const popupClose = popup.querySelector('.popup__close');
// const addButton = document.querySelector('.addButton');
// const placeForm = document.forms.elementInfo;
// const cardsContainer = document.querySelector('.tasksContainer');
// const group = document.querySelector('.group');
//
// function openPopup(popup) {
//     popup.classList.add('popup_opened');
// }
// function closePopup() {
//     popup.classList.remove('popup_opened');
// }
// // function createCard(cardData) {
// //     const cardTemplate = document.querySelector('.tasksContainer').content;
// //     const cardElement = cardTemplate.cloneNode(true);
// //     cardElement.querySelector('.element__name').textContent = cardData.name;
// //     return cardElement;
// // }
//
// // function renderCard(name) {
// //     const cardData = {'name': name};
// //     cardsContainer.prepend(createCard(cardData));
// // }
//
// addButton.addEventListener('click', function () {
//     openPopup(popup);
// });
// // popupClose.addEventListener('click', function () {
// //     closePopup(popup);
// // });
// // placeForm.addEventListener('submit', function (evt) {
// //     evt.preventDefault();
// //     renderCard(name.value);
// //     closePopup(popup);
// //     placeForm.reset();
// // })
// addButton.addEventListener('click', openPopup);
// popupClose.addEventListener('click', closePopup);
