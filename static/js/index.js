

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

