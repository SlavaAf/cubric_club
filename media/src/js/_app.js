$(document).ready(function(){
    $('[data-toggle=2]').css('display','none');
    $('#trans').click(function(){
        if (this.attributes[2].nodeValue=="concert"){
            console.log(this.attributes[2].nodeValue);
            $(this).attr('name','party');
            $("#logo").attr('src','media/images/logo_i.png');
            $(".ticket").attr('src','media/images/ticket_i.png');
            $('#irl').text('Вечеринки');
            $("body").addClass('invert');
            $('[data-toggle=1]').css('display','none');
            $('[data-toggle=2]').css('display','block');
        }else{
            console.log(this.attributes[2].nodeValue);
            $(this).attr('name','concert');
            $("#logo").attr('src','media/images/logo.png');
            $(".ticket").attr('src','media/images/ticket.png');
            $('#irl').text('Концерты');
            $("body").removeClass('invert');
            $('[data-toggle=1]').css('display','block');
            $('[data-toggle=2]').css('display','none');
        }
        //alert('yo');
        //console.log(this.attributes[2].nodeValue);
        //$("body").css(
        //    {'background-color':'black', 'color':'#fff'},
        //)
        //$(".black_nav").addClass('w_nav');
    });
});
function invert(){
    console.log('wewe');
};
