$(function(){
    'use strict';
    $('body').css("height",$(window).height())
    var wid=$(window).width();
    var html_snow="<img src='../static/images/snow-item.png' class='snow_img'>";
    setInterval(function(){$(".snow").append(html_snow);snowFlow();},1000);
    function snowFlow(){
        $(".snow_img").each(function(index){
            var snow_time=(Math.random()*10+4)*1000;
            var wid_snow=Math.floor(Math.random()*40+5)+'px';
            var float_left=Math.random()*wid*2-wid+"px";
            var wid_left=Math.random()*wid+"px";
            if( $(this).css("margin-left")==1+"px"){
                $(this).css("margin-left",wid_left);
                }
                $(this).width(wid_snow);
            $(this).animate({top:800+"px",left:float_left,},snow_time);
            if($(this).offset().top >= 3 * $(window).height() / 5){
                $(this).remove();
            }
        })
    }
    //$('#cod_ent').attr('href', "daily" );
    $("#cod_ent").click(function(){

        var data={
            'signal': document.getElementById("coding").value
        };
        $.ajax({
            type: 'GET',
            url: 'daily',
            data: data,
            dataType: 'json',
            success: function(data){
                var permission = data.permission;
                if (permission === 1){
                    document.getElementById("enterimg").style.display='inline';
                    $("#enter").attr('href', 'main3');

                }else if(permission === 0){
                    $("#enter").attr('href', 'chopin');
                    document.getElementById("enterimg").style.display='inline';
                    console.log(document.getElementById("enter").href);
                }else{
                    console.log('fail');
                    document.getElementById("coding").value = "";
                }
            }
        });
    });
});