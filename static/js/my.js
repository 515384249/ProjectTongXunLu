//快捷查询
$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    // language=JQuery-CSS
    $('.list-group-item').click(function () {
        var idstr = $(this).html()
        var s = ""

        // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({

            type: "POST",
            data: {

                "type": "kjjs",
                "data": idstr,
            },
            url: '/kjfs_search/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,

            dataType: "json",
            success: function (result) {

            // var obj = eval("(" + result + ")");


                $('#ArbetTable').bootstrapTable('load', result)


            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });

});
