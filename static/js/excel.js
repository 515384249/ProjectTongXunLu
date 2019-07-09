$('#myModal').draggable();


 // document.getElementsByClassName('pagination').style.marginLeft= '0px'


// //删除
// $(document).ready(function () {
//     $.ajaxSetup({
//         beforeSend: function (xhr, settings) {
//             function getCookie(name) {
//                 var cookieValue = null;
//                 if (document.cookie && document.cookie !== '') {
//                     var cookies = document.cookie.split(';');
//                     for (var i = 0; i < cookies.length; i++) {
//                         var cookie = jQuery.trim(cookies[i]);
//                         // Does this cookie string begin with the name we want?
//                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                             break;
//                         }
//                     }
//                 }
//                 return cookieValue;
//             }
//
//             function csrfSafeMethod(method) {
//                 // these HTTP methods do not require CSRF protection
//                 return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//             }
//
//             if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                 var csrftoken = getCookie('csrftoken');
//                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
//             }
//         }
//     });
//
//     // 删除
//     $('#mybtn_excel').click(function () {
//
//              window.open("/fileupload/","popup_page","status=1,height:500,width:600,toolbar=0,resizeable=0")
//         // var id_array = new Array();
//         // $('input[name="subbox"]:checked').each(function () {
//         //     id_array.push($(this).attr('id'));//向数组中添加元素
//         // });
//         // var idstr = id_array.join(',');//将数组元素连接起来以构建一个字符串
//         // // alert(idstr);
//         //
//         //
//         // // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
//         // $.ajax({
//         //
//         //     type: "POST",
//         //     data: {
//         //
//         //         "type": "del",
//         //         "data": idstr,
//         //     },
//         //     url: '/comments_upload/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
//         //     cache: false,
//         //
//         //     dataType: "html",
//         //     success: function (result) {
//         //         alert(result);                                         //成功时弹出view传回来的结果
//         //         window.location.reload();
//         //     },
//         //     error: function () {
//         //         alert("false");
//         //     }
//         // });
//         // return false;
//     });
//
// });
//
