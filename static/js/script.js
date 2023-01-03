// let to_cart_btn = document.querySelectorAll('.to-cart');

// for (let i = 0; i = to_cart_btn.length; i++) {
//     function change() {
//         if (to_cart_btn[i].innerHTML == "Add to Cart") {
//             to_cart_btn[i].innerHTML = "Added to Cart";
//         } else {
//             to_cart_btn[i].innerHTML = "Add to Cart";
//         } 
//     }
//     to_cart_btn[i].addEventListener('click', change);
// }

$(document).ready(function(){
    $(".wish-icon i").click(function(){
        $(this).toggleClass("fa-regular fa-solid");
    });
});	

$(document).ready(function(){
    $(".add-to-cart").click(function(){
        if ($(this).text() == 'Add to Cart') {
            $(this).text('Added to Cart');
        } else {
            $(this).text('Add to Cart');
        }
    });
});	