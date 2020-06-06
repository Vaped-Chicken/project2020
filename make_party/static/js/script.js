const sender_button = document.querySelector('#submiter');



function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
}


sender_button.addEventListener('click',
function(ev){
  console.log('click');
  let photo = document.getElementById("photo");
  ev.preventDefault();

  let scrf_token = getCookie('csrftoken');
  let api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiMDcwODQ1MjgtOWFkNy00NjViLWJjZGMtNmYxODZjMTQyZDYxIn0.XEivKJamIn8RH7-bWNdsSHGKMsnVYHVTS-jmPn4m1XM';
  let file = photo.files[0];

  let json = {
    "model" : "face-blurring",
    "image" : file,
    };

  var form_data = new FormData();
  // form_data.append("model" , "face-blurring");
  form_data.append("model" , "animal-gan");
  form_data.append("image" , file, 'kek.jpg');
  let url = 'https://www.visionhub.ru/api/v2/process/img2img/';

  $.ajax({
    type: 'POST',
    data: form_data,
    url: url,
    dataType: 'json',
    contentType: false,
    processData: false,
    cache: false,
    beforeSend: function (xhr) {
    /* Authorization header */
    xhr.setRequestHeader("Authorization", "Bearer " + api_token);
    },
    xhr: function() {
      var xhr = new window.XMLHttpRequest();
      // $upload_progress.show();
      // $task_progress.width(0);
      // прогресс загрузки на сервер
      console.log(xhr);
      xhr.upload.addEventListener("progress", function(event){
        if (event.lengthComputable) {
          var progress = Math.round(event.loaded / event.total * 100);
          console.log(progress);
          // $task_status.text('Загружается');
          // $task_progress.width(progress + '%');
        }
      }, false);
      return xhr;
    },
  }).done(function (data) {
    var task_id = data.task_id;
    console.log(task_id);

    var my_interval = setInterval(function(){
      $.ajax({
          beforeSend: function(request) {
              request.setRequestHeader("Authorization", "Bearer " + api_token);
          },
          dataType: "json",
          url: 'https://www.visionhub.ru/api/v2/task_result/' + task_id + '/',
          success: function(data) {
              console.log(data);
              if (data.status === 'DONE') {
                  clearInterval(my_interval);
                  dragsecretphoto(data.url);
              }
          }
      });

    },500);


    });

      return false;
    });
// })

function dragsecretphoto(url){
  let scrf_token = getCookie('csrftoken');
  let api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiMDcwODQ1MjgtOWFkNy00NjViLWJjZGMtNmYxODZjMTQyZDYxIn0.XEivKJamIn8RH7-bWNdsSHGKMsnVYHVTS-jmPn4m1XM';
  full_url = 'https://www.visionhub.ru' + url;
  console.log(full_url);
  $.ajax({
      beforeSend: function(request) {
          request.setRequestHeader("Authorization", "Bearer " + api_token);
      },
      dataType: "json",
      url: full_url,
      success: function(data) {
          console.log(data);

      }
  });

}





// }).fail(function (data) {
// data = JSON.parse(data.responseText);
// $errors.text(data[Object.keys(data)[0]]);
// });
// });


// console.log(file);
// let url = 'https://www.visionhub.ru/api/v2/process/img2img/';
// let req = new XMLHttpRequest();
// req.open('POST',url,true);
// req.setRequestHeader("X-CSRFToken", scrf_token);
// req.setRequestHeader("acces", "application/json");

//   console.log(json);
//   json = JSON.stringify(json);
//   console.log(json);
//
//
//   if (window.FormData !== undefined){
//     let data = new FormData();
//     data.append('',json);
//     console.log(data);
//
//     req.send(data);
//     req.onreadystatechange = function(){
//         if (req.readyState != 4){
//             return false;
//         };
//         if (req.status !=200){
//           }
//         else{
//           console.log(req.responseText());
//           return false;
//         }
//     }
//
//   }
//
// })

// push_info_button.addEventListener('click',
//   function (event) {
//     json = []
//     Array.from(all_checkbox).forEach(el => {
//       if (el.checked_status == true){
//         json.push(el);
//       }
//     })
//     json = JSON.stringify(json);
//
//     let url = 'push_porch_info_to_base';
//     let push_porch_info_request = new XMLHttpRequest();
//     push_porch_info_request.open('POST',url,true);
//     let token = getCookie('csrftoken');
//     push_porch_info_request.setRequestHeader("X-CSRFToken", token);
//
//     if (window.FormData !== undefined){
//         let data = new FormData();
//         data.append("id", document.getElementById('id_id').innerHTML );
//         data.append('json_house_info',json);
        // push_porch_info_request.send(data);
        // push_porch_info_request.onreadystatechange = function(){
        //     if (push_porch_info_request.readyState != 4){
        //         // cssload.style = 'display:block';
        //         return false;
        //     };
        //
        //     if (push_porch_info_request.status !=200){
        //       }
        //     else{
        //       location.href = "/";
        //       // location.reload();
        //       return false;
        //     }
        // }
  //   }
  // })
//
