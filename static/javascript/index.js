let text1=document.querySelector("#exampleFormControlTextarea1");
let btn=document.querySelector("#data");
let gif=document.querySelector("#media")
let bad="https://giphy.com/embed/xT1R9YUaUwR49MdDLa";
let good="https://giphy.com/embed/RgfGmnVvt8Pfy";

let getData=(url)=>{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function final(res){
  if (res==true){
    gif.setAttribute('src',bad);
  }
  else{
    gif.setAttribute('src',good);
  }
}


btn.addEventListener("click",()=>{
  let url="http://127.0.0.1:8000/post/?text="+String(text1.value);
  let result=JSON.parse(getData(url)).message;
  final(result);
  //console.log(result)
  //console.log(text1.value);
  text1.value=''
})


text1.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    // Trigger the button element with a click
    btn.click();
    text1.value=''
  }
});
