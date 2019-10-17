$(document).ready(function(){

    $('.Ir-arriba').click(function(){
        $('body, html').animate({
            scrollTop: '0px'},300);
    });

    $(window).scroll(function(){
        if($(this).scrollTop() > 0){
            $('.Ir-arriba').slideDown(300);
        } else {
            $('.Ir-arriba').slideUp(300); 
        }
    });
});