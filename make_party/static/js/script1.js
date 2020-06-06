const sender_button = document.querySelector('#submiter');

function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
}


sender_button.addEventListener('click',
function(ev){

  ev.preventDefault();
  let photo = document.getElementById("photo");
  console.log('shmyak');
  let scrf_token = getCookie('csrftoken');

  let file = photo.files[0];

  let url = 'change_photo';

  let req = new XMLHttpRequest();
  req.open('POST',url,true);
  req.setRequestHeader("X-CSRFToken", scrf_token);

    if (window.FormData !== undefined){
      let data = new FormData();
      data.append("image" , file, 'kek.jpg');

      console.log(data);

      req.send(data);
      req.onreadystatechange = function(){
          if (req.readyState != 4){
              return false;
          };
          if (req.status !=200){
            }
          else{
            console.log(req.responseText);
            return false;
          }
      }

    }

})
