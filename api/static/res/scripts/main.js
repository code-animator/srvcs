function initialize()
{
  var xhttp = new XMLHttpRequest();
  document.getElementById('top-text').innerHTML+='<span>And I am a Ironman!</span>';
  xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    document.getElementById('top-text').innerHTML+= this.responseText;
  }
  };
  xhttp.open("GET", "http://127.0.0.1:8001/api/", true);
  xhttp.send();
}
function tosend()
{
  console.log('send pressed');
  document.getElementById('top-loader').innerHTML='';
  document.getElementById('top-text').innerHTML+='<p style=\"font-size:0.7em; color:grey; font-style:italic\">You typed: '+document.getElementById('bottom-text-inp').value+'</p>';
  document.getElementById('bottom-text-inp').value=''
  /*xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    document.getElementById("demo").innerHTML = this.responseText;
  }
  };
  xhttp.open("POST", "demo_post2.asp", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("fname=Henry&lname=Ford");*/
  document.getElementById('top-loader').innerHTML+='<img src=\'res\\loaders\\chat.gif\' width=80em>';
  //document.getElementById('top-text').innerHTML+='<p>Session initialized</p>';
  document.getElementById('top-text').innerHTML+='<p>Analyzing the text</p>';
  document.getElementById('top-text').innerHTML+='<p>Running the model</p>';
}
function detectkey(e)
{
  e = e || window.event;
  let charCode = e.keyCode || e.which;
  //console.log(charCode);
  if(charCode==13)
  {
    tosend();
  }
  else {
    //alert('keep listening');
  }
  return(String.fromCharCode(charCode));
}
window.addEventListener('keypress', function (e) {detectkey(e);}, false);
