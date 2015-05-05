var item,good_update=false,eitems=[];

function cart_show_mess(obj,str,success)
{
	var dv=$("<div></div>").addClass("cart_mess").html(str);
	$(document.body).append(dv);
	if (obj.find(".info").length>0)
		dv.css({left:obj.offset().left+(obj.outerWidth()-dv.outerWidth())/2,top:obj.offset().top+50,display:"none"});	
	else
		dv.css({left:obj.offset().left+(obj.outerWidth()-dv.outerWidth())/2,top:obj.offset().top+12,display:"none"});	
	dv.fadeIn();
	setTimeout(function() {
		dv.fadeOut(function() {
			$(this).remove();
      if (success && typeof(success)=="function")
        success(obj);
		});
	},2000);
}
function cart_save_good()
{	
	if (good_update)
	{
		location.href="?action=update&id="+item.data("id")+"&eitems="+eitems.join(",");
		return;
	}
	item.find(".order").addClass("saving");
	$.getJSON("/request.php","param=1&id="+item.data("id")+"&eitems="+eitems.join(","),function(data) {
		item.find(".order").removeClass("saving");
		if (data.status=="OK")
		{
      if (item.children(".front").length>0)
      {
        cart_show_mess(item,"<span>Позиция добавлена в Ваш заказ.</span>",function() {
          item.children(".back").hide();
          item.children(".front").show();
        });
      }
      else
        cart_show_mess(item,"<span>Позиция добавлена в Ваш заказ.</span>");
			$(".cart_info .price span").html(data.sum);
			$(".cart_info").addClass("cart_info_ex");
		}
		else
		{			
			cart_show_mess(item,"<span>Не удалось добавить позицию в Ваш заказ!</span>");
		}
	});
}

function cart_add_good(obj)
{
  eitems=[];
	item=$(obj).closest(".item");
	
	if (item.data("extra")==0)
	{
		cart_save_good();
		return;
	}	
	cart_load_extra();
}
function cart_load_extra()
{  
  ImageViewer.dark_all();
  $.getJSON("/request.php","param=2&id="+item.data("id")+"&pos="+eitems.length,function(data) {    
    if (data.status=="OK")
    {      
      item.data("extra-more",data.more);
      cart_show_extra(data.text,data.items);
    }
    else
    {
      $(ImageViewer.shadow).remove();
      cart_show_mess(item,"<span>Не удалось добавить позицию в Ваш заказ!</span>");
    }
    
  });
}
function cart_show_extra(text,items)
{  
  var obj=$(".chwin");
  obj.find(".title").html(text);
  var info=obj.find(".info");
  info.html("");
  for (var k in items)
  {
    var str="";
    if (items[k].image!="")
      str+="<img src='"+items[k].image+"'>";
    str+="<span>"+items[k].title+"</span>";
    var el=$("<div></div>").addClass("item").data("id",items[k].id).html(str);
    el.click(cart_set_extra);
    info.append(el);
  }
  obj.show();
  obj.css({"marginLeft":-obj.width()/2,"marginTop":-obj.height()/2});
}
function cart_change_good(obj)
{
	item=$(obj).closest(".item");

  eitems=[];
	cart_load_extra();
	good_update=true;
}

function cart_set_extra()
{
  eitems[eitems.length]=$(this).data("id");
  cart_close_win();
  if (item.data("extra-more")==1)
    cart_load_extra();
  else
    cart_save_good();
}
function cart_close_win()
{
  $(".chwin").hide();
	$(ImageViewer.shadow).remove();
}

function cart_check_form(frm)
{
	var ok=true;
	$(frm).find("input[data-check=1],textarea[data-check=1]").each(function() {
		if ($(this).attr("value")=="") {			
      set_error($(this),"error","error-text","обязательное поле");
			ok=false;
		}
	});
	if (!ok)
		return false;
	return true;
}
function cart_delete_item(obj)
{
	var obj=$(obj).parents(".item");	
	(new _Confirm()).show("Удалить "+obj.find(".title b").html()+"?",function(yes) {
    if (yes==1)
      location.href="?action=delete&id="+obj.data("id");    
  });
}
function set_cookie(name,value)
{
  var today=new Date();
  var date=new Date(today.getTime() + 86400*10*1000);
  document.cookie=name + "=" + escape (value) + "; expires=; path=/; domain=.xn--80aaahi2bjaklrrng.xn--p1ai;";
}
function cart_confirm(btn)
{
  var frm=btn.closest("form");
  (new _Confirm()).show("Отправить заказ?",function(yes) {
    if (yes==1)
      frm.submit();
  });
}
$(document).ready(function() {
  $("#oform [data-save=1]").each(function() {
    $(this).change(function() {
      set_cookie($(this).attr("name"),escape($(this).val()));
    });
  });
  $(".items .back.add").click(function(e) {
    cart_add_good(this);
    e.stopPropagation();
  });
});

