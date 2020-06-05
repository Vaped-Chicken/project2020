const sender_button = document.querySelector('#submiter');

sender_button.addEventListener('click',
function(ev){
  ev.preventDefault();
  console.log('нажал');
})





// var form_data = new FormData($upload_form[0]);
//  $choose_file.prop('disabled', true);
//  $.ajax({
//      type: 'POST',
//      data: form_data,
//      url: $upload_form.attr('action'),
//      dataType: 'json',
//      contentType: false,
//      processData: false,
//      cache: false,
//      xhr: function() {
//          var xhr = new window.XMLHttpRequest();
//          $upload_progress.show();
//          $task_progress.width(0);
//          // прогресс загрузки на сервер
//          xhr.upload.addEventListener("progress", function(event){
//              if (event.lengthComputable) {
//                  var progress = Math.round(event.loaded / event.total * 100);
//                  console.log(progress);
//                  $task_status.text('Загружается');
//                  $task_progress.width(progress + '%');
//              }
//          }, false);
//          return xhr;
//      },
//  }).done(function (data) {
//      var task_id = data.id;
//      $('.js-stop').on('click', function (event) {
//          $(this).hide();
//          $.ajax({
//              type: 'GET',
//              dataType: 'json',
//              url: '/tasks/task/' + task_id + '/stop/',
//              success: function (data) {},
//          });
//          return false;
//      });
