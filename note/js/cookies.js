cookies
//设置cookies
expire_time=(new Date()).getTime()+100
document.cookie="mykey_name=xxx;expires=expire_time;path=/"  
//expires 
//path 如果不设置，只能在当前页面获取

//获取
cookie_lenght=document.cookie.length
document.cookie.substring(0,cookie_lenght)
