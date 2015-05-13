function update_basket(){
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

function load_basket_data(){
    $.ajax({
        url: '/shop/basket/data/',
        cache: false,
        success: function(data){
            $('#cart_data').html(data);
        },
        error: function(e, xhr){
            msg_error("", "Ошибка загрузки корзины.");
        }
    });
}

function load_basket_delivery(){
    $.ajax({
        url: '/shop/basket/delivery/',
        cache: false,
        success: function(data){
            $('#cart_data').html(data);
        },
        error: function(e, xhr){
            msg_error("", "Ошибка загрузки корзины.");
        }
    });
}

function cart_minus_item(uuid){
    $.ajax({
        url: '/shop/basket/item/minus/'+uuid+'/',
        cache: false,
        success: function(data){
            load_basket_data();
            update_basket();
        },
        error: function(e, xhr){
            msg_error("", "Ошибка изменения количества.");
        }
    });
}

function cart_plus_item(uuid){
    $.ajax({
        url: '/shop/basket/item/plus/'+uuid+'/',
        cache: false,
        success: function(data){
            load_basket_data();
            update_basket();
        },
        error: function(e, xhr){
            msg_error("", "Ошибка изменения количества.");
        }
    });
}

function cart_delete_item(uuid){
    $.ajax({
        url: '/shop/basket/item/delete/'+uuid+'/',
        cache: false,
        success: function(data){
            load_basket_data();
            update_basket();
        },
        error: function(e, xhr){
            msg_error("", "Ошибка удаления позиции.");
        }
    });
}

function cart_add_option(id){
    $.ajax({
        url: '/shop/option/'+id+'/',
        cache: false,
        success: function(data){
            $( "#dialog-option" ).html(data);
            $( "#dialog-option #main-val").val(id);
            if($( "#dialog-option #option1" ).html()!='') {
                $( "#dialog-option #option1").show();
            }
            $(function() {
                $( "#dialog-option" ).dialog({
                    resizable: false,
                    height:440,
                    width: 600,
                    modal: true,
                    closeOnEscape: false
                });
            });
            $( "#dialog-option" ).dialog( "option", "title", $( "#dialog-option #option1-title").val() );
        },
        error: function(e, xhr){
            msg_error("", "Ошибка загрузки данных.");
        }
    });
}

function cart_select_option1(id){
    $( "#dialog-option #option1-val").val(id);
    if($( "#dialog-option #option2" ).html().trim()!='') {
        $( "#dialog-option #option1").hide();
        $( "#dialog-option #option3").hide();
        $( "#dialog-option #option2").show();
        $( "#dialog-option" ).dialog( "option", "title", $( "#dialog-option #option2-title").val() );
    } else {
        $( "#dialog-option" ).dialog( "close" );
        cart_send_option();
    }
}

function cart_select_option2(id){
    $( "#dialog-option #option2-val").val(id);
    if($( "#dialog-option #option3" ).html().trim()!='') {
        $( "#dialog-option #option1").hide();
        $( "#dialog-option #option2").hide();
        $( "#dialog-option #option3").show();
        $( "#dialog-option" ).dialog( "option", "title", $( "#dialog-option #option3-title").val() );
    } else {
        $( "#dialog-option" ).dialog( "close" );
        cart_send_option();
    }
}

function cart_select_option3(id){
    $( "#dialog-option #option3-val").val(id);
    $( "#dialog-option" ).dialog( "close" );
    cart_send_option();
}

function cart_send_option() {
    $.ajax({
        url: '/shop/basket/add/' +
            $( "#dialog-option #main-val").val() + '-' +
            $( "#dialog-option #option1-val").val() + '-' +
            $( "#dialog-option #option2-val").val() + '-' +
            $( "#dialog-option #option3-val").val()+'/',
        cache: false,
        success: function(data){
            if(data=='ok')
            {
                msg_info("", "Позиция добавлена в корзину.");
                update_basket();
            }
        },
        error: function(e, xhr){
            msg_error("", "Ошибка добавления в корзину.");
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
                    title: $('#dialog-choice #dialog-title').val()
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
                update_basket();
            }
        },
        error: function(e, xhr){
            msg_error("", "Ошибка добавления в корзину.");
        }
    });
}



$(window.document).ready(function() {
    update_basket();

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


