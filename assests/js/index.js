

$(".link-delete").on("click", function(e){
    e.preventDefault();
    window.location.reload()
    var $this = $(this);
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
            url: $this.attr("href"),
            type: "POST",
            dataType: "json",
            beforeSend: function (xhr){
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
    });
    
    return false;
});

// $(".link-update").on("click", function(e){
//     e.preventDefault();
//     var $this = $(this);
//     var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
//     let name = $("#name").val(); 
//     let email = $("#email").val();
//     let number = $("#number").val(); 
   
//     $.ajax({
//         url: $this.attr("href"),
//         type: "POST",
//         dataType: "json",
//         data: {
//             'name': JSON.stringify(name),
//             'email': JSON.stringify(email) ,
//             'number': JSON.stringify(number)
//         },
//         beforeSend: function (xhr){
//             xhr.setRequestHeader('X-CSRFToken', csrftoken);
//         }
//     });

//     return false;
// });