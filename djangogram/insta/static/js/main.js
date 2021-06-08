let search_input = $('#search-field')
let search_results = $('#search-results')

let endpoint = '/users/'


$(search_input).on('keyup', function () {
    let search_value = $(this).val()
    $.ajax({
        url: endpoint + '?search=' + search_value
    }).done(function (data) {
        search_results.show()
        search_results.html(data['html_response'])
    })
})
$(window).click(function () {
    search_results.hide(500)
    search_results.delay(500).html('')
});

search_results.click(function (event) {
    event.stopPropagation();
});

function getCSRFTokenValue() {
    return $('input[name="csrfmiddlewaretoken"]').attr('value')
}

$(".like").on("click", function () {
    let post_id = $(this).attr('id')
    let counter = $(this).children("i")
    $.ajax(
        {
            url: '/posts/' + post_id + '/like',
            type: 'POST',
            headers: {'X-CSRFToken': getCSRFTokenValue()}
        }
    ).done(function (data) {
        counter.html(" " + data['like_count'])
    })
})

$("#subscribe").on("click", function () {
    let counter = $("#followers_count")
    let count = parseInt(counter.text())
    let profile_id = $("#profile_id").val()
    let btn = $(this)
    $.ajax(
        {
            url: '/users/' + profile_id + '/subscribe',
            type: 'POST',
            headers: {'X-CSRFToken': getCSRFTokenValue()}
        }
    ).done(function (data) {
        if (data['is_subscribed']) {
            count = parseInt(count) + 1
            btn.text("Отписаться")
        } else {
            count = parseInt(count) - 1
            btn.text("Подписаться")
        }
        counter.html(count)
    })
})
$(".add-comment").keypress(function (e) {
    let post_id = $(this).attr('name')
    let comment = $(this).val()
    let input_obj = $(this)
    let key = e.which;
    if (key === 13) {
        $.ajax({
            url: '/posts/' + post_id + '/comment',
            type: 'POST',
            headers: {'X-CSRFToken': getCSRFTokenValue()},
            data: {
                comment: comment
            }
        }).done(function (data) {
            if (data['has_error']) {
                alert(data['error_message'])
            } else {
                if ($(".post-comments-block").length > 0) {
                    $("#post-comments-" + post_id).append(data["html_response"])
                } else {
                    $("#comments-" + post_id).prepend(data["html_response"])
                }
                input_obj.val("")
            }
        })
    }
});



