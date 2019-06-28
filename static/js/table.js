$('#myModal').on('hidden.bs.modal', function () {
    // 执行一些动作...
    document.getElementById("motaiform").reset();
    $(this).removeData('bs.modal');
})

$(function () {
    let $table = $('#ArbetTable');
    let $button = $('#mybtn_add');
    let $getTableData = $('#mybtn_save');
    let $detbnt = $('#mybtn_delete');

    $button.click(function () {
        $table.bootstrapTable('insertRow', {
            index: 0,
            row: {}
        });
    });

    $table.bootstrapTable({
        clickEdit: true,
        showToggle: true,
        showColumns: true,
        showPaginationSwitch: false,     //显示切换分页按钮
        showRefresh: true,      //显示刷新按钮
        clickToSelect: false,  //点击row选中radio或CheckBox
        sidePagination: "client",
        queryParams: function (params) {//上传服务器的参数
            var temp = {//如果是在服务器端实现分页，limit、offset这两个参数是必须的
                // limit: params.limit, // 每页显示数量
                // offset: params.offset, // SQL语句起始索引
                //page: (params.offset / params.limit) + 1,   //当前页码
                search: $('#data-search-text').val(),
            };
            return temp;
        },


        // columns: [{
        //     checkbox: true
        // },
        //     {
        //         field: 'id',
        //         title: 'Item ID'
        //     },
        //     {
        //         field: 'name',
        //         title: 'Item Name'
        //     },
        //     {
        //         field: 'price',
        //         title: 'Item Price'
        //     },],
        /**
         * @param {点击列的 field 名称} field
         * @param {点击列的 value 值} value
         * @param {点击列的整行数据} row
         * @param {td 元素} $element
         */


        onClickCell: function (field, value, row, $element) {
            console.log(row)
            console.log($element.checkbox)
            if ($element == true) {
                // alert("we get subbox")
            }
            $element.attr('contenteditable', true);
            $element.blur(function () {
                let index = $element.parent().data('index');
                let tdValue = $element.html();
                console.log(tdValue)
                saveData(index, field, tdValue);
            })
        }
    })
    ;


//保存
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


        $getTableData.click(function () {


            var myarray = new Array();
            myarray = JSON.stringify($table.bootstrapTable('getSelections'));
            // alert(myarray.length)
            if (myarray.length < 3) {
                alert("请选中一条记录，否则保存无效")
                return;
            }
            // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
            $.ajax({

                type: "POST",
                data: {
                    "type": "save",
                    "data": myarray,
                },
                url: '/kjfs_edit/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
                cache: false,

                dataType: "html",
                success: function (result) {
                    // window.location.reload()
                    window.location.href = '/ceshi/'

                },
                error: function () {
                    alert("false");
                }
            });
            return false;
        });


    });

//s刪除
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


        $detbnt.click(function () {
            var myarray = new Array();
            myarray = JSON.stringify($table.bootstrapTable('getSelections'));
            // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
            $.ajax({

                type: "POST",
                data: {
                    "type": "del",
                    "data": myarray,
                },
                url: '/kjfs_edit/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
                cache: false,

                dataType: "html",
                success: function (result) {
                    // alert("tiaozhuan-shanchu");


                    window.location.href = '/ceshi/'

                    //document.getElementById("motaiform").reset();

                },
                error: function () {
                    alert("false");
                }
            });
            return false;
        });


    });


    function saveData(index, field, value) {
        $table.bootstrapTable('updateCell', {
            index: index,       //行索引
            field: field,       //列名
            value: value        //cell值
        })
        console.log(index, field, value)
    }

});
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
    var $button = $('#mysearchbnt')
    $('#mysearchbnt').click(function () {
        let $table = $('#ArbetTable')
        var s = $('#name').val()
        console.log(s)
        $.ajax({
            type: "POST",
            data: {
                "search": s,
            },
            url: '/showtable/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,
            dataType: "json",
            success: function (result) {
                $('#ArbetTable').bootstrapTable({data: result})
                // console.log(toString.call(result));
                // console.log(result)
                // var obj = eval("(" + result + ")");
                // var rows = []
                // for (var i = 0; i <10; i++) {
                //      console.log( obj.length)
                //     rows.push({
                //         id: obj[i]["id"],
                //         yuan: obj[i]["yuan"],
                //         xi: obj[i]["xi"],
                //         xingming: obj[i]["xingming"],
                //         dianhua: obj[i]["dianhua"],
                //         dizhi: obj[i]["dizhi"],
                //
                //     })
                // }
                // $('#ArbetTable').bootstrapTable('load', rows)

            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });


});

$(function () {
    let $table = $('#ArbetTable2');
    $table.bootstrapTable({
        showToggle: false,
        showColumns: false,
        showPaginationSwitch: false,     //显示切换分页按钮
        showRefresh: true,      //显示刷新按钮
        sidePagination: "client",
        paginationDetailHAlign: 'right',
        paginationHAlign: 'left',


        queryParams
:

    function (params) {//上传服务器的参数
        var temp = {//如果是在服务器端实现分页，limit、offset这两个参数是必须的
            search: $('#data-search-text').val(),
        };
        return temp;
    }

,
})


});


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
    var $button = $('#mysearchbnt')
    $('#mysearchbnt').click(function () {
        let $table = $('#ArbetTable')
        var s = $('#name').val()
        console.log(s)
        $.ajax({
            type: "POST",
            data: {
                "search": s,
            },
            url: '/showtable/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,
            dataType: "html",
            success: function (result) {
                console.log(result)

                console.log(toString.call(result));
                console.log(result)
                var obj = eval("(" + result + ")");
                var rows = []
                if (obj.length < 1) {
                    $('#ArbetTable2').bootstrapTable("removeAll")
                } else {

                    for (var i = 0; i < 10; i++) {
                        console.log(obj.length)
                        rows.push({
                            id: obj[i]["id"],
                            yuan: obj[i]["yuan"],
                            xi: obj[i]["xi"],
                            xingming: obj[i]["xingming"],
                            dianhua: obj[i]["dianhua"],
                            dizhi: obj[i]["dizhi"],
                        })
                    }

                    $('#ArbetTable2').bootstrapTable('load', rows)
                }
            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });


});

//

// function randomData(data) {
//     var rows = []
//     for (var i = 0; i < data.length; i++) {
//         rows.push({
//             id: data[i]["id"],
//             yuan: data[i]["id"],
//             xi: data[i]["xi"],
//             zhuanye: data[i]["zhaunye"],
//             xingming: data[i]["xingming"],
//             zhiwu: data[i]["zhiwu"],
//             dianhua: data[i]["dianhua"],
//             dizhi: data[i]["dizhi"],
//         })
//     }
//     return rows
// }



document.getElementsByClassName('pagination').style.marginLeft='0px'