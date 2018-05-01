$(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
            data: {
                corpFrom: $('#from').val(),
                corpTo: $('#to').val()
				amount: $('#amount').val()
				currency: $('#currency').val()
            },
            type: 'POST',
            url: '/table_data'
        })
    event.preventDefault();
    });
});