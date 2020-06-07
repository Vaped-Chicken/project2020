const sender_button = document.querySelector('#submiter');
const photo_img = document.querySelector('#photo_img');
const photo_frame = document.querySelector('.photo-frame');
const photo_obj = document.querySelector('#photo');
let finalFile;
const sticker_button = document.querySelector('#send-userid');
const disclaimer = document.querySelector('.disclaimer');
const sticker_name = document.querySelector('#sticker_name')
const userid = document.querySelector('#userid')


function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
}

let scrf_token = getCookie('csrftoken');

sender_button.addEventListener('click',
function(ev){

  ev.preventDefault();
  let photo = document.getElementById("photo");
  console.log('shmyak');

  let file = photo.files[0];

  let url = 'change_photo';

  let req = new XMLHttpRequest();
  req.open('POST',url,true);
  req.setRequestHeader("X-CSRFToken", scrf_token);

    if (window.FormData !== undefined){
      let data = new FormData();
      data.append("image" , finalFile);
      data.append("csrf" , scrf_token);

      photo_img.src = '/static/img/110.gif';

      photo_frame.style = 'display:block';
      req.send(data);
      req.onreadystatechange = function(){
          if (req.readyState != 4){
              return false;
          };
          if (req.status !=200){
            }
          else{
            console.log(req.responseText);
            let photo_img = document.querySelector('#photo_img');
            let photo_frame = document.querySelector('.photo-frame');
            let json = JSON.parse(req.responseText);
            photo_img.src = '/'+json.url;
            sticker_button.style = 'display:inherit';

            return false;
          }
      }

    }

})


photo_obj.addEventListener('change',
  async function (event) {
    let photo = event.target.files[0];
    console.log(photo);
    let compressedPhoto = await CompressPhoto(photo);
  }
)

function CompressPhoto(photo){
  let fileType = photo.type;
  let reader = new FileReader();
  var photo_obj
  reader.readAsDataURL(photo);
  reader.onload = function(){
    let image = new Image();
    image.src = reader.result;
    image.onload = async function () {
      let maxWidth = 720,
      maxHeight = 1280,
      imageWidth = image.width,
      imageHeight = image.height;
      if (imageWidth > imageHeight) {
        if (imageWidth > maxWidth) {
          imageHeight *= maxWidth / imageWidth;
          imageWidth = maxWidth;
        }
      }
      else {
        if (imageHeight > maxHeight) {
          imageWidth *= maxHeight / imageHeight;
          imageHeight = maxHeight;
        }
      }
      let canvas = document.createElement('canvas');
      canvas.width = imageWidth;
      canvas.height = imageHeight;
      let ctx = await canvas.getContext("2d");
      await ctx.drawImage(this, 0, 0, imageWidth, imageHeight);
      finalFile = await canvas.toDataURL('image/jpeg', 0.3);
      // element.updatePhoto(finalFile);
    }
  }
  return false;
}


sticker_button.addEventListener('click',
  function () {
    let url = 'create_stickerpack';

    let req = new XMLHttpRequest();
    req.open('POST',url,true);
    req.setRequestHeader("X-CSRFToken", scrf_token);

    if (window.FormData !== undefined){
      let data = new FormData();
      data.append("userid" , userid.value);
      data.append("csrf" , scrf_token);
      req.send(data);
      req.onreadystatechange = function(){
          if (req.readyState != 4){
              return false;
          };
          if (req.status !=200){
            }
          else{
            let json = JSON.parse(req.responseText);
            console.log(req.responseText);

            disclaimer.style = 'display:inherit';
            sticker_name.innerHTML = 'Название: ' + json.name;
            return false;
          }
      }
    }
  })
