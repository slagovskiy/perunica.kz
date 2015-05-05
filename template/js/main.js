/*
function _InitManager()
{
  this.execute_events = function(name)
  {
    if (!this.events[name])
      return;
    for (var k in this.events[name])
    {
      if (k == "length")
        continue;
      if (typeof(this.events[name][k]) == "function")
        this.events[name][k]();
      else if (typeof(this.events[name][k]) == "string")
        eval(this.events[name][k]);
    }
  }
  this.register_event = function(name, callback)
  {
    if (!this.events[name])
    {
      this.events[name] = new Object();
      this.events[name]["length"] = 0;
    }
    this.events[name]["length"]++;
    this.events[name][this.events[name]["length"]]=callback;
  }
  this.unregister_event = function(name, callback)
  {
    if (!this.events[name])
      return;
    for (var k in this.events[name])
    {
      if (k == "length")
        continue;
      if (this.events[name][k]==callback)
      {
        delete this.events[name][k];
        this.events[name]["length"]--;
        return;
      }
    }
  }
  this.events = new Object();
  window.onload = function() {InitManager.execute_events("onload");};
  window.onresize = function() {InitManager.execute_events("onresize");};
  window.onscroll = function() {InitManager.execute_events("onscroll");};
}
var InitManager = new _InitManager();

function _ConnectionManager()
{
  this.pool;
  this.requests;
  this.req_next=1;
  this.createHttpRequest = function()
  {
    req = null;
    if (window.XMLHttpRequest)
    {
      try
      {
        req = new XMLHttpRequest();
      } catch (e){}
    }
    else if (window.ActiveXObject)
    {
      try
      {
        req = new ActiveXObject('Msxml2.XMLHTTP');
      } catch (e)
      {
        try
        {
          req = new ActiveXObject('Microsoft.XMLHTTP');
        } catch (e){}
      }
    }
    return req;
  }
  this.checkLoad = function()
  {
    for (var k=0;k<5;k++)
    {
      if (this.pool[k]["active"])
      {
        if (this.pool[k]["obj"].readyState == 4)
        {
          if (this.pool[k]["obj"].status == 200)
            this.pool[k]["callback"](this.pool[k]["obj"].responseXML);
          delete this.requests[this.pool[k]["req_id"]];
          this.pool[k]["active"]=false;
          this.pool[k]["time"]=0;
          this.pool[k]["req_id"]=0;
        }
        else
        {
          if (((new Date).getTime()-this.pool[k]["time"])>5000)
          {
            this.pool[k]["obj"].abort();
            this.requests[this.pool[k]["req_id"]]["active"]=false;
            this.pool[k]["active"]=false;
            this.pool[k]["time"]=0;
            this.pool[k]["req_id"]=0;
            this.send();
          }
        }
      }
    }
    this.send();
    setTimeout("ConnectionManager.checkLoad()",200);
  }
  this.init = function()
  {
    this.pool = new Object();
    for (var k=0;k<5;k++)
    {
      this.pool[k]=new Object();
      this.pool[k]["obj"]=this.createHttpRequest();
      this.pool[k]["active"]=false;
      this.pool[k]["req_id"]=0;
      this.pool[k]["time"]=0;
    }
    this.requests = new Object();
    setTimeout("ConnectionManager.checkLoad()",200);
  }
  this.send = function()
  {
    for (var k in this.requests)
    {
      if (!this.requests[k]["active"])
      {
        for (var m=0;m<5;m++)
        {
          if (!this.pool[m]["active"])
          {
            this.pool[m]["active"]=true;
            this.pool[m]["req_id"]=k;
            this.pool[m]["callback"]=this.requests[k]["callback"];
            this.pool[m]["time"]=(new Date()).getTime();
            this.requests[k]["active"]=true;
            this.pool[m]["obj"].open("POST", this.requests[k]["url"], true);
            this.pool[m]["obj"].setRequestHeader("If-Modified-Since", "Sat, 1 Jan 2000 00:00:00 GMT");
            this.pool[m]["obj"].setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            this.pool[m]["obj"].setRequestHeader("Content-length", this.requests[k]["params"].length);
            this.pool[m]["obj"].setRequestHeader("Connection", "close");
            this.pool[m]["obj"].send(this.requests[k]["params"]);
            break;
          }
        }
      }
    }
  }
  this.get = function(url,params,callback)
  {
    if (!this.pool)
      this.init();
    this.requests[this.req_next]=new Object();
    this.requests[this.req_next]["url"]=url;
    this.requests[this.req_next]["params"]=params;
    this.requests[this.req_next]["callback"]=callback;
    this.requests[this.req_next++]["active"]=false;
    this.send();
  }
}
var ConnectionManager = new _ConnectionManager();

function fix_png(el)
{
  if (!/MSIE (5\.5|6\.)/.test(navigator.userAgent)) return;

  var src;
  if (el.tagName=='IMG')
  {
    if (/\.png$/.test(el.src))
    {
      src = el.src;
      el.src = "/img/high.gif";
      el.runtimeStyle.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + src + "',sizingMethod='crop')";
    }
  }
  else
  {
    src = el.currentStyle.backgroundImage.match(/url\("(.+\.png)"\)/i);
    if (src)
    {
      src = src[1];
      el.runtimeStyle.backgroundImage="none";
      if (el.currentStyle.backgroundRepeat == "no-repeat")
        el.runtimeStyle.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + src + "',sizingMethod='crop')";
      else
        el.runtimeStyle.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + src + "',sizingMethod='scale')";
    }
  }
}

function _ImageViewer()
{
  this.handle;
  this.viewarea;
  this.thumbails;
  this.shadow;
  this.loading;
  this.close_button;
  this.prev_button;
  this.next_button;
  this.sce;
  this.images = new Object();
  this.mwidth = 352;
  this.mheight = 200;
  this.tcount;
  this.is_loading = false;
  this.is_slideshow = false;
  this.prev_image = function()
  {
    this.onclick_thumbail(this.images.curr-1);
  }
  this.next_image = function()
  {
    this.onclick_thumbail(this.images.curr+1);
  }
  this.set_nav = function ()
  {
    if (this.images.curr > 1)
      this.prev_button.style.visibility="visible";
    else
      this.prev_button.style.visibility="hidden";
    if (this.images.curr < this.images.length)
      this.next_button.style.visibility="visible";
    else
      this.next_button.style.visibility="hidden";
  }
  this.pos = function()
  {
    if (!this.handle)
      return;
    var atop = 0;
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      atop = document.documentElement.scrollTop;
    this.handle.style.top = ((document.documentElement.clientHeight - this.handle.offsetHeight) / 2) + atop + "px";
    this.handle.style.left = ((document.documentElement.clientWidth - this.handle.offsetWidth) / 2) + "px";
    this.close_button.style.left = this.handle.offsetLeft + this.handle.offsetWidth + "px";
    this.close_button.style.top = this.handle.offsetTop - this.close_button.offsetHeight + "px";
    this.expand_button.style.left = this.handle.offsetLeft - this.expand_button.offsetWidth - 5 + "px";
    this.expand_button.style.top = this.handle.offsetTop + 50 + "px";
    this.slide_button.style.left = this.handle.offsetLeft - this.slide_button.offsetWidth - 5 + "px";
    this.slide_button.style.top = this.handle.offsetTop + 75 + "px";
    this.prev_button.style.left = this.handle.offsetLeft - this.prev_button.offsetWidth - 5 + "px";
    this.prev_button.style.top = this.handle.offsetTop + this.handle.offsetHeight / 2  + "px";
    this.next_button.style.left = this.handle.offsetLeft + this.handle.offsetWidth + 5 + "px";
    this.next_button.style.top = this.handle.offsetTop + this.handle.offsetHeight / 2 + "px";
    this.thumb_prev_button.style.left = this.handle.offsetLeft - this.thumb_prev_button.offsetWidth - 5 + "px";
    this.thumb_prev_button.style.top = this.handle.offsetTop + this.handle.offsetHeight - this.thumbails.offsetHeight + 5  + "px";
    this.thumb_next_button.style.left = this.handle.offsetLeft + this.handle.offsetWidth + 5 + "px";
    this.thumb_next_button.style.top = this.handle.offsetTop + this.handle.offsetHeight - this.thumbails.offsetHeight + 5  + "px";
    this.loading.style.left = this.handle.offsetLeft + (this.viewarea.offsetWidth - this.loading.offsetWidth) / 2 + "px";
    this.loading.style.top = this.handle.offsetTop + (this.viewarea.offsetHeight - this.loading.offsetHeight) / 2 +  "px";
    this.set_nav();
  }
  this.dark_all = function()
  {
    this.shadow = document.createElement("DIV");
    this.shadow.style.cssText = "z-index:1000;background:#000000;left:0px;top:0px;width:100%;height:100%;position:fixed;opacity:0.5;filter:alpha(opacity=50);";
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
    {
      this.shadow.style.position = "absolute";
      this.shadow.style.width = document.documentElement.scrollWidth;
      this.shadow.style.height = document.documentElement.scrollHeight;
    }
    document.body.appendChild(this.shadow);
  }
  this.get_text = function(obj)
  {
    if (/MSIE/.test(navigator.userAgent))
      return obj.text;
    return obj.textContent;
  }
  this.set_thumbail = function(id)
  {
    this.images[id].thumbail.src = this.images[id].thumbail_t.src;
    this.images[id].thumbail.onmouseover = function(id) {return function() {ImageViewer.onmouseover_thumbail(id)}} (id);
    this.images[id].thumbail.onmouseout = function(id) {return function() {ImageViewer.onmouseout_thumbail(id)}} (id);
    if (id == this.images.curr)
    {
      this.images[this.images.curr].thumbail.style.cssText = "margin:0;width:48px;height:48px;border:1px solid #aa0000;filter:alpha(opacity=100);opacity:1;cursor:default;";
      this.images[this.images.curr].thumbail.onclick = function() {};
      return;
    }
    var a = "";
    if (this.images[id].thumbail.style.visibility == "hidden")
      a = "visibility:hidden;";
    this.images[id].thumbail.style.cssText = "margin:5px;width:40px;height:40px;border:0;opacity:0.5;filter:alpha(opacity=50);cursor:pointer;" + a;
    this.images[id].thumbail.onclick = function(id) {return function() {ImageViewer.onclick_thumbail(id)}} (id);
  }
  this.load = function()
  {
    this.is_loading = true;
    this.prev_button.style.visibility = "hidden";
    this.next_button.style.visibility = "hidden"
    this.images[this.images.curr].image = document.createElement("IMG");
    this.images[this.images.curr].image.src = this.images[this.images.curr].src;
    if (!this.images[this.images.curr].image.complete)
    {
      this.loading.style.visibility = "visible";
      this.images[this.images.curr].image.onload = function() {ImageViewer.set_image()};
    }
    else
      this.set_image();
  }
  this.light_image = function()
  {
    if (!this.handle)
      return;
    this.images[this.images.curr].alpha += 10;
    if (/MSIE/.test(navigator.userAgent))
    {
      this.images[this.images.curr].alpha += 10;
      this.images[this.images.curr].image.style.filter = "progid:DXImageTransform.Microsoft.Alpha(opacity=" + this.images[this.images.curr].alpha + ");";
    }
    else
      this.images[this.images.curr].image.style.opacity = this.images[this.images.curr].alpha / 100;
    if (this.images[this.images.curr].alpha < 100)
      setTimeout(function() {ImageViewer.light_image()}, 50);
    else
    {
      this.is_loading = false;
      this.images[this.images.curr].image.onclick = function() {ImageViewer.close();};
    }
  }
  this.get_dims = function()
  {
    var maxw = document.documentElement.clientWidth - this.prev_button.offsetWidth - this.next_button.offsetWidth - 50;
    var maxh = document.documentElement.clientHeight - this.close_button.offsetHeight - 40 - this.thumbails.offsetHeight;
    var w = this.images[this.images.curr].w;
    var h = this.images[this.images.curr].h;
    if (h > maxh)
    {
      var old_h = h;
      h = maxh;
      w = Math.round(h / old_h * w);
    }
    if (w > maxw)
    {
      var old_w = w;
      w = maxw;
      h = Math.round(w / old_w * h);
    }
    return [w,h];
  }
  this.set_image = function()
  {
    if (!this.handle)
      return;
    this.loading.style.visibility = "hidden";
    if (this.viewarea.childNodes.length == 1)
      this.viewarea.removeChild(this.viewarea.childNodes[0]);
    if (/MSIE/.test(navigator.userAgent))
      this.images[this.images.curr].image.style.filter = "progid:DXImageTransform.Microsoft.Alpha(opacity=0);";
    else
      this.images[this.images.curr].image.style.opacity = 0;
    this.images[this.images.curr].alpha = 0;
    this.viewarea.appendChild(this.images[this.images.curr].image);
    this.images[this.images.curr].w = this.images[this.images.curr].image.offsetWidth;
    this.images[this.images.curr].h = this.images[this.images.curr].image.offsetHeight;
    this.resize();
    this.light_image();
  }
  this.load_thumbails = function()
  {
    this.thumbails.style.height = "52px";
    var dv=document.createElement("DIV");
    dv.style.cssText = "height:50px;margin-top:1px;white-space:nowrap;position:relative;left:0;top:0;";
    this.thumbails.appendChild(dv);
    this.mheight += 52;
    for (var k in this.images)
    {
      if (isNaN(k))
        continue;
      this.images[k].thumbail = document.createElement("IMG");
      this.images[k].thumbail.src = "/img/iviewer/iw_iloading.gif";
      this.images[k].thumbail.style.cssText = "width:40x;height:40px;margin:5px;";
      dv.appendChild(this.images[k].thumbail);
      this.images[k].thumbail_t = document.createElement("IMG");
      this.images[k].thumbail_t.onload = function(k) {return function() {ImageViewer.set_thumbail(k)}} (k);
      this.images[k].thumbail_t.src = this.images[k].thumb_src;
    }
    this.resize();
  }
  this.parse_data = function(obj)
  {
    if (!this.handle)
      return;
    for (var k in this.images)
      delete this.images[k];
    var els = obj.getElementsByTagName("result");
    this.images.length = els.length;
    for (var k = 0;k < els.length;k++)
    {
      this.images[k+1] = new Object();
      this.images[k+1].rpoint = 0;
      this.images[k+1].rdir = 1;
      for (var m = 0;m < els.item(k).childNodes.length;m++)
      {
        var el = els.item(k).childNodes[m];
        var val = this.get_text(el);
        if (el.tagName == "curr")
        {
          if  (val == "1")
            this.images.curr = k + 1;
          continue;
        }
        this.images[k+1][el.tagName] = val;
      }
    }
    if (this.images.length > 0)
    {
      if (this.images.length > 1)
      {
        this.load_thumbails();
        this.slide_button.style.visibility = "visible";
      }
      this.load();
    }
  }
  this.move_thumbail = function(id)
  {
    this.images[id].rtm = setTimeout(function(id) {return function() {ImageViewer.move_thumbail(id)}} (id), 20);
    if (this.images[id].rdir == 1)
      return;
    if ((this.images[id].rdir == 3) && (this.images[id].ron == 1))
      return;
    if (this.images[id].rdir == 2)
    {
      if (this.images[id].rpoint == 0)
      {
        if (/MSIE/.test(navigator.userAgent))
          this.images[id].thumbail.style.filter = "progid:DXImageTransform.Microsoft.Alpha(opacity=100);";
        else
          this.images[id].thumbail.style.opacity = 1;
      }
      this.images[id].rpoint++;
      if (this.images[id].rpoint == 6)
      {
        this.images[id].rdir = 3;
        this.images[id].rpoint = 5;
        return;
      }
    }
    if (this.images[id].rdir == 3)
    {
      if (this.images[id].rpoint == 0)
      {
        if (/MSIE/.test(navigator.userAgent))
          this.images[id].thumbail.style.filter = "progid:DXImageTransform.Microsoft.Alpha(opacity=50);";
        else
          this.images[id].thumbail.style.opacity = 0.5;
      }
      this.images[id].rpoint--;
      if (this.images[id].rpoint == -1)
      {
        this.images[id].rpoint = 0;
        if (this.images[id].rdir == 3)
          this.images[id].rdir = 1;
      }
    }
    this.images[id].thumbail.style.margin = 5 -this.images[id].rpoint + "px";
    this.images[id].thumbail.style.width = 40 + this.images[id].rpoint * 2 + "px";
    this.images[id].thumbail.style.height = 40 + this.images[id].rpoint * 2 + "px";
  }
  this.onmouseover_thumbail = function(id)
  {
    if (this.images.curr != id)
    {
      this.images[id].rdir = 2;
      this.images[id].ron = 1;
      if (!this.images[id].rtm)
        this.images[id].rtm = setTimeout(function(id) {return function() {ImageViewer.move_thumbail(id)}} (id), 20);
    }
    if ((this.images[id].name) && (!this.is_loading))
    {
      this.name.style.display = "block";
      this.name.innerHTML = this.images[id].name;
      this.name.style.width = this.viewarea.childNodes[0].offsetWidth -40 + "px";
      this.name.style.left = this.handle.offsetLeft + "px";
      this.name.style.top = this.handle.offsetTop + this.viewarea.childNodes[0].offsetHeight - this.name.offsetHeight + "px";
    }
  }
  this.onmouseout_thumbail = function(id)
  {
    if (this.images.curr != id)
      this.images[id].ron = 0;
    this.name.style.display = "none";
  }
  this.onclick_thumbail = function(id,slide)
  {
    if (this.is_loading)
      return;
    if ((this.is_slideshow) && (!slide))
      this.stop_slide_show();
    if (/MSIE/.test(navigator.userAgent))
      this.images[this.images.curr].image.style.filter = "progid:DXImageTransform.Microsoft.Alpha(opacity=50);";
    else
      this.images[this.images.curr].image.style.opacity = 0.5;
    this.images.curr = id;
    for (var k = 1;k <= this.images.length;k++)
      this.set_thumbail(k);
    this.is_loading = true;
    this.name.style.display = "none";
    this.load();
  }
  this.thumb_move_right = function()
  {
    if ((this.fthumb + this.tcount - 1) < this.images.length)
    {
      this.fthumb++;
      this.set_thumb_nav();
    }
  }
  this.thumb_move_left = function()
  {
    if (this.fthumb > 1)
    {
      this.fthumb--;
      this.set_thumb_nav();
    }
  }
  this.slide_show = function()
  {
    if (!this.handle)
      return;
    if (!this.is_slideshow)
      return;
    setTimeout(function() {ImageViewer.slide_show();},3000);
    if (this.is_loading)
      return;
    var id = this.images.curr + 1;
    if (id > this.images.length)
      id = 1;
    this.onclick_thumbail(id,true);
  }
  this.stop_slide_show = function()
  {
    this.is_slideshow = false;
    this.slide_button.src = "/img/iviewer/iw_slideshow.png";
    fix_png(this.slide_button);
  }
  this.start_slide_show = function()
  {
    if (this.is_loading)
      return;
    if (this.is_slideshow)
    {
      this.stop_slide_show();
      return;
    }
    this.slide_button.src = "/img/iviewer/iw_slideshow_sel.png";
    fix_png(this.slide_button);
    this.is_slideshow = true;
    this.slide_show();
  }
  this.expand_image = function()
  {
    window.open(this.images[this.images.curr].src);
  }
  this.set_thumb_nav = function()
  {
    for (var k = 1;k <= this.images.length;k++)
      this.images[k].thumbail.style.visibility = "hidden";
    for (var k = this.fthumb;k < (this.tcount + this.fthumb);k++)
    {
      if (k > this.images.length)
        break;
      this.images[k].thumbail.style.visibility = "visible";
    }
    this.thumbails.childNodes[0].style.left = (this.viewarea.offsetWidth - this.tcount * 50) / 2 - (this.fthumb - 1) * 50 + "px";
    if (this.fthumb > 1)
      this.thumb_prev_button.style.visibility = "visible";
    else
      this.thumb_prev_button.style.visibility = "hidden";
    if ((this.fthumb + this.tcount - 1) < this.images.length)
      this.thumb_next_button.style.visibility = "visible";
    else
      this.thumb_next_button.style.visibility = "hidden";
  }
  this.resize = function()
  {
    if (this.viewarea.childNodes.length == 1)
    {
      var dims = this.get_dims();
      this.images[this.images.curr].image.style.width = dims[0] + "px";
      this.images[this.images.curr].image.style.height = dims[1] + "px";
      this.viewarea.style.width = this.viewarea.childNodes[0].offsetWidth + "px";
      this.viewarea.style.height = this.viewarea.childNodes[0].offsetHeight + "px";
    }
    this.thumbails.style.width = this.viewarea.offsetWidth + "px";
    this.handle.style.width = this.viewarea.offsetWidth + "px";
    this.handle.style.height = this.viewarea.offsetHeight + this.thumbails.offsetHeight + "px";
    if (this.images.length > 1)
    {
      var w = this.viewarea.offsetWidth - 2;
      this.tcount = Math.floor(w / 50);
      this.fthumb = 1;
      if (this.tcount < this.images.length)
      {
        this.fthumb = this.images.curr - Math.floor(this.tcount / 2);
        if (this.fthumb < 1)
          this.fthumb = 1;
        if ((this.fthumb + this.tcount - 1) > this.images.length)
          this.fthumb = this.images.length - this.tcount + 1;
      }
      else
        this.tcount = this.images.length;
      this.set_thumb_nav();
    }
    this.pos();
  }
  this.create_self = function()
  {
    this.dark_all();
    this.handle = document.createElement("DIV");
    this.handle.style.cssText = "position:fixed;z-index:1001;background:#ffffff;width:" + this.mwidth + "px;height:" + this.mheight + "px;-webkit-box-shadow:2px 2px 10px #000000;-moz-box-shadow:2px 2px 10px #000000;box-shadow:2px 2px 10px #000000;filter:progid:DXImageTransform.Microsoft.Shadow(color='#000000',Direction=135,Strength=6);";
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.handle.style.position = "absolute";
    document.body.appendChild(this.handle);
    this.viewarea = document.createElement("DIV");
    this.viewarea.style.cssText = "width:" + this.mwidth + "px;height:" + this.mheight + "px;";
    this.handle.appendChild(this.viewarea);
    this.thumbails = document.createElement("DIV");
    this.thumbails.style.cssText = "width:" + this.mwidth + "px;height:0px;overflow:hidden;";
    this.handle.appendChild(this.thumbails);
    this.close_button = document.createElement("IMG");
    this.close_button.src = "/img/iviewer/iw_close.png";
    this.close_button.style.cssText = "position:fixed;z-index:1002;cursor:pointer;width:15px;height:15px;";
    this.close_button.onclick = function() {ImageViewer.close();};
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.close_button.style.position = "absolute";
    document.body.appendChild(this.close_button);
    this.prev_button = document.createElement("IMG");
    this.prev_button.src = "/img/iviewer/iw_nav_prev.png";
    this.prev_button.style.cssText = "position:fixed;z-index:1002;width:20px;height:19px;cursor:pointer;visibility:hidden;";
    this.prev_button.onclick = function() {ImageViewer.prev_image();};
    this.prev_button.onmouseover = function() {this.src = "/img/iviewer/iw_nav_prev_sel.png";fix_png(this);};
    this.prev_button.onmouseout = function() {this.src = "/img/iviewer/iw_nav_prev.png";fix_png(this);};
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.prev_button.style.position = "absolute";
    document.body.appendChild(this.prev_button);
    this.next_button = document.createElement("IMG");
    this.next_button.src = "/img/iviewer/iw_nav_next.png";
    this.next_button.style.cssText = "position:fixed;z-index:1003;width:20px;height:19px;cursor:pointer;visibility:hidden;";
    this.next_button.onclick = function() {ImageViewer.next_image();};
    this.next_button.onmouseover = function() {this.src = "/img/iviewer/iw_nav_next_sel.png";fix_png(this);};
    this.next_button.onmouseout = function() {this.src = "/img/iviewer/iw_nav_next.png";fix_png(this);};
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.next_button.style.position = "absolute";
    document.body.appendChild(this.next_button);
    this.thumb_next_button = document.createElement("IMG");
    this.thumb_next_button.src = "/img/iviewer/iw_tnav_next.png";
    this.thumb_next_button.style.cssText = "position:fixed;z-index:1003;width:20px;height:40px;cursor:pointer;visibility:hidden;";
    this.thumb_next_button.onclick = function() {ImageViewer.thumb_move_right();};
    this.thumb_next_button.onmouseover = function() {this.src = "/img/iviewer/iw_tnav_next_sel.png";fix_png(this);};
    this.thumb_next_button.onmouseout = function() {this.src = "/img/iviewer/iw_tnav_next.png";fix_png(this);};
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.thumb_next_button.style.position = "absolute";
    document.body.appendChild(this.thumb_next_button);
    this.thumb_prev_button = document.createElement("IMG");
    this.thumb_prev_button.src = "/img/iviewer/iw_tnav_prev.png";
    this.thumb_prev_button.style.cssText = "position:fixed;z-index:1003;width:20px;height:40px;cursor:pointer;visibility:hidden;";
    this.thumb_prev_button.onclick = function() {ImageViewer.thumb_move_left();};
    this.thumb_prev_button.onmouseover = function() {this.src = "/img/iviewer/iw_tnav_prev_sel.png";fix_png(this);};
    this.thumb_prev_button.onmouseout = function() {this.src = "/img/iviewer/iw_tnav_prev.png";fix_png(this);};
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.thumb_prev_button.style.position = "absolute";
    document.body.appendChild(this.thumb_prev_button);
    this.expand_button = document.createElement("IMG");
    this.expand_button.src = "/img/iviewer/iw_expand.png";
    this.expand_button.style.cssText = "position:fixed;z-index:1003;width:16px;height:18px;cursor:pointer;v";
    this.expand_button.onclick = function() {ImageViewer.expand_image();};
    this.expand_button.setAttribute("title","Открыть в новом окне");
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.expand_button.style.position = "absolute";
    document.body.appendChild(this.expand_button);
    this.slide_button = document.createElement("IMG");
    this.slide_button.src = "/img/iviewer/iw_slideshow.png";
    this.slide_button.style.cssText = "position:fixed;z-index:1003;width:22px;height:21px;cursor:pointer;visibility:hidden;";
    this.slide_button.onclick = function() {ImageViewer.start_slide_show();};
    this.slide_button.setAttribute("title","Слайдшоу");
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.slide_button.style.position = "absolute";
    document.body.appendChild(this.slide_button);
    this.loading = document.createElement("IMG");
    this.loading.src = "/img/iviewer/iw_loading.gif";
    this.loading.style.cssText = "position:fixed;z-index:1020;width:208px;height:13px;";
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      this.loading.style.position = "absolute";
    document.body.appendChild(this.loading);
    this.name = document.createElement("DIV");
    this.name.style.cssText = "position:fixed;z-index:1030;display:none;background:url('/img/iviewer/iw_pix.png');color:#ffffff;font-weight:bold;font-size:14px;text-align:center;padding-bottom:5px;padding-top:5px;padding-left:20px;padding-right:20px;";
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
    {
      this.name.style.position = "absolute";
      this.name.className = "png";
    }
    document.body.appendChild(this.name);
    this.pos();
    InitManager.register_event("onresize", function() {ImageViewer.resize()});
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      InitManager.register_event("onscroll", function() {ImageViewer.pos()});
  }
  this.show = function(sce,id)
  {
    if (!this.handle)
      this.create_self();
    this.sce = sce;
    ConnectionManager.get(this.sce,"id="+id,function(txt) {ImageViewer.parse_data(txt)});
  }
  this.show_one = function(url)
  {
    if (!this.handle)
      this.create_self();
    this.expand_button.style.visibility = "hidden";
    for (var k in this.images)
      delete this.images[k];
    this.images.curr = 1;
    this.images[1] = new Object();
    this.images[1].src = url;
    this.load();
  }
  this.close = function()
  {
    InitManager.unregister_event("onresize", function() {ImageViewer.resize()});
    if (/MSIE (5\.5|6\.)/.test(navigator.userAgent))
      InitManager.unregister_event("onscroll", function() {ImageViewer.pos()});
    document.body.removeChild(this.handle);
    document.body.removeChild(this.prev_button);
    document.body.removeChild(this.next_button);
    document.body.removeChild(this.thumb_prev_button);
    document.body.removeChild(this.thumb_next_button);
    document.body.removeChild(this.expand_button);
    document.body.removeChild(this.slide_button);
    document.body.removeChild(this.close_button);
    document.body.removeChild(this.loading);
    delete this.handle;
    document.body.removeChild(this.shadow);
  }
}
var ImageViewer = new _ImageViewer();

function _LoadManager()
{
  this.images = new Object();
  this.images_len = 0;
  this.add = function(src)
  {
    this.images[this.images_len] = new Object();
    this.images[this.images_len++]["src"] = src;
  }
  this.start = function(callback)
  {
    this.callback = callback;
    this.int = setInterval(function() {LoadManager.check_complete()},20);
    for (var k in this.images)
    {
      this.images[k]["complete"] = false;
      this.images[k]["img"] = document.createElement("IMG");
      this.images[k]["img"].onload = function(k1) {return function() {LoadManager.set_loaded(k1)}} (k);
      this.images[k]["img"].src = this.images[k]["src"];
    }
  }
  this.set_loaded = function(id)
  {
    this.images[id]["complete"] = true;
    this.check_complete();
  }
  this.check_complete = function()
  {
    for (var k in this.images)
    {
      if (!this.images[k]["complete"])
      return;
    }
    clearInterval(this.int);
    for (var k in this.images)
    delete this.images[k];
    this.images_len = 0;
    this.callback();
  }
}
var LoadManager = new _LoadManager();

function _LoadManager()
{
  this.images = new Object();
  this.images_len = 0;
  this.add = function(src)
  {
    this.images[this.images_len] = new Object();
    this.images[this.images_len++]["src"] = src;
  }
  this.start = function(callback)
  {
    this.callback = callback;
    this.int = setInterval(function() {LoadManager.check_complete()},20);
    for (var k in this.images)
    {
      this.images[k]["complete"] = false;
      this.images[k]["img"] = document.createElement("IMG");
      this.images[k]["img"].onload = function(k1) {return function() {LoadManager.set_loaded(k1)}} (k);
      this.images[k]["img"].src = this.images[k]["src"];
    }
  }
  this.set_loaded = function(id)
  {
    this.images[id]["complete"] = true;
    this.check_complete();
  }
  this.check_complete = function()
  {
    for (var k in this.images)
    {
      if (!this.images[k]["complete"])
      return;
    }
    clearInterval(this.int);
    for (var k in this.images)
    delete this.images[k];
    this.images_len = 0;
    this.callback();
  }
}
var LoadManager = new _LoadManager();

function _Fader()
{
	this.items = new Object();
	this.items_len = 0;
	this.start = function(obj, callback)
	{
		this.items[this.items_len] = new Object();
		this.items[this.items_len]["obj"] = obj;
		this.items[this.items_len]["callback"] = callback;
		this.items[this.items_len]["opacity"] = 100;
		this.items[this.items_len]["int"] = setInterval(function(id) {return function() {Fader.fade(id)}} (this.items_len), 50);
		this.items_len++;
	}
	this.fade = function(id)
	{
		this.items[id]["opacity"] -= 10;
		if (this.items[id]["opacity"] >= 0)
		{
			if (/MSIE/.test(navigator.userAgent))
				this.items[id]["obj"].childNodes[0].style.filter = "progid:DXImageTransform.Microsoft.Alpha(opacity=" + this.items[id]["opacity"] + ");";
			else
				this.items[id]["obj"].childNodes[0].style.opacity = this.items[id]["opacity"] / 100;
		}
		else
		{
			clearInterval(this.items[id]["int"]);
      var src=this.items[id]["obj"].style.backgroundImage.substr(4,this.items[id]["obj"].style.backgroundImage.length-5);
      if (src.substr(0,1)=="\"")
        src=src.substr(1,src.length-2);
      this.items[id]["obj"].childNodes[0].src = src;
			if (/MSIE/.test(navigator.userAgent))
				this.items[id]["obj"].childNodes[0].style.filter = "progid:DXImageTransform.Microsoft.Alpha(opacity=100);";
			else
				this.items[id]["obj"].childNodes[0].style.opacity = 1;
			this.items[id]["callback"]();
			delete this.items[id];
		}
	}
}
var Fader = new _Fader();

function _Lister()
{
  this.items = new Object();
  this.items_len = 0;
  this.start = function(obj, callback, dir)
  {
    this.items[this.items_len] = new Object();
    this.items[this.items_len]["obj"] = obj;
    obj.childNodes[0].style.left="0px";
    obj.childNodes[1].style.left=obj.childNodes[0].offsetWidth+"px";
    this.items[this.items_len]["callback"] = callback;
    this.items[this.items_len]["dir"] = dir;
    this.items[this.items_len]["int"] = setInterval(function(id) {return function() {Lister.move(id)}} (this.items_len), 50);
    this.items_len++;
  }
  this.get_left = function(el)
  {
    var left=el.style.left.substr(0,el.style.left.length-2);
    left=left.replace(/,/,'.')*1;
    return left;
  }
  this.move = function(id)
  {
    var obj=this.items[id]["obj"];
    var dir=this.items[id]["dir"];
    if (dir==1)
      var x=-obj.childNodes[0].offsetWidth;
    else
      var x=obj.childNodes[0].offsetWidth;
    var left=this.get_left(obj.childNodes[0]);
    var step=(x-left)/3;
    if (Math.abs(step)<1)
    {
      obj.childNodes[0].style.left="0px";
      obj.childNodes[1].style.left=-x+"px";
      obj.childNodes[0].innerHTML=obj.childNodes[1].innerHTML;
      clearInterval(this.items[id]["int"]);
      this.items[id]["callback"]();
      delete this.items[id];
    }
    else
    {
      obj.childNodes[0].style.left=left+step+"px";
      obj.childNodes[1].style.left=left+step-x+"px";
    }
  }
}
var Lister = new _Lister();

$(window.document).ready(function() {
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
	$("div.numcount").each(function() {
		var obj=$(this);		
		var inp=obj.find("input");
		obj.find("a:eq(1)").click(function() {
			inp.val(parseInt(inp.val())+1);
		});
		obj.find("a:eq(0)").click(function() {
			var val=parseInt(inp.val());
			val--;
			inp.val(val>1?val:1);
		});
		inp.keydown(function(e) {
			if ((e.which==8) || (e.which==46))
				return;
			if ((e.which>=48) && (e.which<=57))
				return;
			return false;
		}).change(function(e) {
			if ((inp.val()=="") || (inp.val()=="0"))
				inp.val("1");
		});		
	});
  if ($(".echoose1").length>0) {
    var a=$(".echoose a");
    $(".echoose1").css({"margin-left":-($(".echoose1").width()-a.width())/2});
    a.click(function() {
      $(".echoose1").toggleClass("echoose1-show");
    });
  }
});

var images_loaded=new Object();
var images_obj=new Object();
var images_x,images_y;
function good_create_image(e,id)
{
  var el=document.createElement("div");
  el.className="gimage";
  el.id="image_"+id;
  document.body.appendChild(el);  
  images_x=e.clientX;
  images_y=e.clientY+$(document).scrollTop();
}
function good_set_image(id)
{ 
  if (!document.getElementById("image_"+id))
    return;
  $("#image_"+id).addClass("shadow");
  document.body.appendChild(images_obj[id]);
  $("#image_"+id).css("width",images_obj[id].offsetWidth);
  $("#image_"+id).css("height",images_obj[id].offsetHeight);
  document.body.removeChild(images_obj[id]);
  $("#image_"+id).css("background","url('"+images_obj[id].src+"') no-repeat");
  good_pos_image(id);
}
function good_show_image(e,id,src)
{
  good_create_image(e,id);
  if (!images_loaded[id])
  {
    images_obj[id] = document.createElement("IMG");
    images_obj[id].className="gimage1";
    images_obj[id].onload = function(id1) {return function() {images_loaded[id1]=1;good_set_image(id1)}} (id);
    images_obj[id].src = src;
  }
  else
    good_set_image(id);  
}
function good_pos_image(id)
{ 
  var left=0;
  var top=0;
  if ((images_x+$("#image_"+id).width())>document.body.clientWidth)  
    left=images_x-$("#image_"+id).width()-20;
  else
    left=images_x+20;
  if ((images_y+$("#image_"+id).height())>document.body.clientHeight)  
    top=images_y-$("#image_"+id).height()-20;
  else
    top=images_y+20;
  $("#image_"+id).css("left",left+"px");
  $("#image_"+id).css("top",top+"px");
}
function good_hide_image(id)
{  
  $("#image_"+id).remove();  
}
function good_move_image(e,id)
{  
  if (!document.getElementById("image_"+id))
    return;
  images_x=e.clientX;
  images_y=e.clientY+$(document).scrollTop();  
  good_pos_image(id);
}
function set_error(obj,cl1,cl2,str) {
   if (obj.hasClass(cl1)) {
     if (typeof(obj.data("error-text")) == "object")
        obj.data("error-text").remove();
   }
   obj.addClass(cl1);
   var el=$("<div></div>").addClass(cl2).html(str);
   obj.parent().append(el);
   el.css({top:obj.position().top-el.outerHeight()-3,left:obj.position().left+obj.outerWidth()-el.outerWidth()});
   obj.data("error-text",el);
}
function _ErrorBlock(obj,title,dx)
{
  this.obj=obj;
  this.title=title;
  this.dx=dx;
  this.create = function()
  {
    var el=$("<div></div>");
    el.html("<div></div><span>"+this.title+"</span><b></b>");
    el.addClass("error_block");
    $(document.body).append(el);
    if (isNaN(this.dx))
      this.dx=0;
    el.css("left",obj.offset().left+obj.outerWidth()+10+this.dx);
    el.css("top",obj.offset().top+(obj.outerHeight()-el.height())/2);
    el.css("visibility","visible");
    el.css("display","none");
    this.el=el;
  }
  this.show = function()
  {
    this.el.fadeIn();
    setTimeout(function(obj) {return function() {obj.fadeOut(function() {obj.remove()});}} (this.el),2000);
  }
  this.create();
}

function uban_move(dx)
{
  var bn=$(".uban");  
  if (bn.data("moving")==1)
    return;
  bn.data("moving",1);
  var cur=parseInt(bn.data("cur"),10);
  var max=bn.children().length-1;
  var next=cur+dx;
  if (next<0)
    next=max;
  if (next>max)
    next=0;
  bn.data("cur",next);
  bn.children().eq(cur).addClass("up").show();
  bn.children().eq(next).addClass("down").show();
  bn.children().eq(cur).fadeOut(function() {
    bn.children().eq(cur).removeClass("up").hide();
    bn.children().eq(next).removeClass("down");
    bn.data("moving",0);
  });
}
function uban_auto()
{
  var bn=$(".uban");  
  if (bn.data("auto")==0)
    return;
  uban_move(1);
  setTimeout("uban_auto()",4000);
}

$(window).load(function() {
  var bn=$(".uban");
  var nav=$(".uban_nav");  
  var h=bn.children().eq(0).height();
  bn.height(h);
  nav.children().height(h);  
  if (bn.children().length>1)
  {
    bn.children().addClass("ready");
    nav.show();
    bn.data("cur",0);
    bn.data("moving",0);
    bn.data("auto",1);
    nav.children(".next").click(function() {
      bn.data("auto",0);
      uban_move(1);
    });
    nav.children(".prev").click(function() {
      bn.data("auto",0);
      uban_move(-1);
    });
    setTimeout("uban_auto()",4000);
  }  
});

$(document).ready(function() {
  var shadow;
  $(".section-header .menu").click(function() {
    shadow=$("<div></div>").addClass("shadow").appendTo($(document.body));
    $(document.body).css({"overflow":"hidden"});
    $(".section-menu").css({"overflow-y":"scroll"});
    $(".section-menu").fadeIn();
    $(".section-menu ul").css({height:$(".section-menu").prop('scrollHeight')});    
  });
  $(".section-menu a").click(function(e) {
    e.stopPropagation();
  });
  $(".section-menu").click(function() {    
    shadow.fadeOut(function() {$(this).remove()});
    $(this).fadeOut(function() {$(document.body).css({"overflow":"auto"})});
    
  });
  $(".items .item .front").click(function() {
    $(this).hide();
    $(this).parent().children(".back").css({"display":"table-cell"});
  });
  $(".items .item .back").click(function() {
    return;
    if ($(this).parent().children(".front").length>0)
    {
      $(this).hide();
      $(this).parent().children(".front").show();
    }
  });
  $(document).on("click",".main-actions .front",function() {
      var el=$(this);
      el.parent().children(".back").show();
      el.hide();
      setTimeout(function() {
        el.parent().children(".back").hide();
        el.show();
      },4000);
    });
});

function _Confirm() {
  this.show = function(title, callback) {
    var _this = this;
    this.callback = callback;
    this.shadow = $("<div></div>").addClass("shadow").appendTo($(document.body));
    this.instance = $("<div></div>").html("<b>"+title+"</b><span><button data-yes='1'>Да</button><button data-yes='0'>Нет</button></span>").addClass("confirm-win").appendTo($(document.body));    
    this.instance.css({"margin-left":-this.instance.outerWidth()/2,"margin-top":-this.instance.outerHeight()/2});
    this.instance.find("button").click(function() {
      _this.shadow.remove();
      _this.instance.remove();
      _this.callback($(this).data("yes"));
    });
  }
}

*/
/*
function uban_move(dx)
{
	var bn=$(".uban");  
	if (bn.data("moving")==1)
		return;
	bn.data("moving",1);
	var cur=parseInt(bn.data("cur"),10);
	var max=bn.children().length-1;
	var next=cur+dx;
	if (next<0)
		next=max;
	if (next>max)
		next=0;
	bn.data("cur",next);
	bn.children().eq(cur).addClass("up").show();
	bn.children().eq(next).addClass("down").show();
	bn.children().eq(cur).fadeOut(function() {
		bn.children().eq(cur).removeClass("up").hide();
		bn.children().eq(next).removeClass("down");
		bn.data("moving",0);
	});
}

function uban_auto()
{
	var bn=$(".uban");  
	if (bn.data("auto")==0)
		return;
	uban_move(1);
	setTimeout("uban_auto()",4000);
}
*/
$(window.document).ready(function() {
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


/*
$(window).load(function() {
	var bn=$(".uban");
	var nav=$(".uban_nav");  
	var h=bn.children().eq(0).height();
	bn.height(h);
	nav.children().height(h);  
	if (bn.children().length>1)
	{
		bn.children().addClass("ready");
		nav.show();
		bn.data("cur",0);
		bn.data("moving",0);
		bn.data("auto",1);
		nav.children(".next").click(function() {
			bn.data("auto",0);
			uban_move(1);
		});
		nav.children(".prev").click(function() {
			bn.data("auto",0);
			uban_move(-1);
		});
		setTimeout("uban_auto()",4000);
	}  
});
*/


