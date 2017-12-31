$(document).ready(function () {
    alert("Hello");
});

function calc_price () {
    var sum = 0.0;
    $('#cart_table > tbody > tr').each(function () {
        var qty = $(this).find('#qty').val();
        console.log(qty)
    })
}
