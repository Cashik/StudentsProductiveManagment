$(document).ready(function () {
    var table = $('#example').DataTable({
        "paging": false,
        "select": true,
        "ajax": {
            "url": "{% url 'specialties_list' %}",
            "dataSrc": "data"
        },
        "columnDefs": [
            {
                "targets": [0],
                "visible": false,
                "searchable": false
            }],
        "columns": [
            {"name": "№", "data": "id",},
            {"name": "Название", "data": "name",},
            {"name": "Описание", "data": "description"}
        ]
    });


    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            data: {'id': table.cell('.selected', 0).data()},
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-book").modal("show");
            },
            success: function (data) {
                $("#modal-book .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    //$("#book-table tbody").html(data.html_book_list);
                    table.ajax.reload();
                    $(".js-update-spec").attr("disabled", true);
                    $(".js-delete-spec").attr("disabled", true);
                    $("#modal-book").modal("hide");
                }
                else {
                    $("#modal-book .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    $('#example tbody').on('click', 'tr', function () {
        if ($(this).hasClass('selected')) {
            $(".js-update-spec").attr("disabled", true);
            $(".js-delete-spec").attr("disabled", true);
        } else {
            $(".js-update-spec").attr("disabled", false);
            $(".js-delete-spec").attr("disabled", false);
        }

    });
    /* Binding */

    // Create
    $(".js-create-spec").click(loadForm);
    $("#modal-book").on("submit", ".js-spec-create-form", saveForm);

    // Update
    $(".js-update-spec").click(loadForm);
    $("#modal-book").on("submit", ".js-spec-update-form", saveForm);

    // Delete
    $(".js-delete-spec").click(loadForm);
    $("#modal-book").on("submit", ".js-spec-delete-form", saveForm);


});
