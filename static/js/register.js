
// $(document).ready(function () {
//     $('#final').on('click', function (e) {
//         e.preventDefault()
//         const email = $(this).val();
//         var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
//         console.log(email)
//         $.ajax({
//             url:'/register/',  
//             method:'POST',
//             dataType: 'json',
//             beforeSend: function (xhr){
//                 xhr.setRequestHeader('X-CSRFToken', csrftoken);
//             },
//             success: function (data) {
//                 console.log(data)
//                 console.log("success")
              
//             },
//             error: function (data) {
//                 console.log(data)
//                 if (data.email == email) {
//                     $('#email-error').text('Email already exists').addClass('text-danger');
//                 } else {
//                     $('#email-error').text('').removeClass('text-danger');
//                 }
//             },
           
//         });
//     });
// });
