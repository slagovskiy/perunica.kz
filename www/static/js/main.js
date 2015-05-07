function update_bsket(){
    $.ajax({
        url: '/shop/basket/',
        cache: false,
        success: function(data){
            $('#basket').html(data);
        },
        error: function(e, xhr){
            msg_error("", "Ошибка обновления корзины.");
        }
    });
}

function cart_add_choice(id){
    $.ajax({
        url: '/shop/choice/'+id+'/',
        cache: false,
        success: function(data){
            $( "#dialog-choice" ).html(data);
            $(function() {
                $( "#dialog-choice" ).dialog({
                    resizable: false,
                    height:440,
                    width: 600,
                    modal: true,
                    closeOnEscape: false,
                    title: "Уточните выбор"
                });
            });
        },
        error: function(e, xhr){
            msg_error("", "Ошибка загрузки данных.");
        }
    });
}

function cart_select_choice(id){
    $( "#dialog-choice" ).dialog( "close" );
    cart_add_good(id);
}

function cart_add_good(id){
    $.ajax({
        url: '/shop/basket/add/'+id+'/',
        cache: false,
        success: function(data){
            if(data=='ok')
            {
                msg_info("", "Позиция добавлена в корзину.");
                update_bsket();
            }
        },
        error: function(e, xhr){
            msg_error("", "Ошибка добавления в корзину.");
        }
    });
}



$(window.document).ready(function() {
    update_bsket();

	$(".items[data-show='1'] .item").each(function() {
		var info=$(this).find(".info");
		if (info.data("ch")!="")
		{
			info.data("th",info.find(".title").outerHeight());
			info.data("dh",info.find(".descr").outerHeight());			
		}
		$(this).mouseenter(function() {
			var ch=info.data("th");
			var h=info.data("dh");
			info.clearQueue();
			info.animate({height:ch+h},{step:function(now,fx) {
				info.css("marginTop",222-now+ch);      
			},duration:250});			
		}).mouseleave(function() {
			var ch=info.data("th");
			info.clearQueue();
			info.animate({height:ch},{step:function(now,fx) {
				info.css("marginTop",222-now+ch);      
			},duration:250,complete:function() {				
			}});
		});
	});
});



$(window).load(function() {

});


