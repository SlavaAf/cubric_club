$(document).ready(function(){
    $('[data-toggle=2]').css('display','none');
    if(sessionStorage.getItem('style') == "party")
        setParty();
    else
        setConcert();
    $('#trans').click(function(){
        if (this.attributes[2].nodeValue=="concert")
            setParty();
        else
            setConcert();
    });
    //$('.item')[0].addClass('active');
    $('.item').eq(0).addClass("active");
});
function setParty(){
    sessionStorage.setItem('style', 'party');
    //console.log(sessionStorage.getItem('style'));
    $('#trans').attr('name','party');
    $("#logo").attr('src','/media/images/logo_i.png');
    $(".ticket").attr('src','/media/images/ticket_i.png');
    $('#irl').text('Вечеринки');
    $("body").addClass('invert');
    $('[data-toggle=1]').css('display','none');
    $('[data-toggle=2]').css('display','block');
};
function setConcert(){
    sessionStorage.setItem('style', 'concert');
    //console.log(sessionStorage.getItem('style'));
    $('#trans').attr('name','concert');
    $("#logo").attr('src','/media/images/logo.png');
    $(".ticket").attr('src','/media/images/ticket.png');
    $('#irl').text('Концерты');
    $("body").removeClass('invert');
    $('[data-toggle=1]').css('display','block');
    $('[data-toggle=2]').css('display','none');
};
