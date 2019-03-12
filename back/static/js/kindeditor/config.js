KindEditor.ready(function (k) {
    window.editor = k.create('#id_doc_content',{
        resizeType:1,
        allowPreviewEmoticons : false,
        allowImageRemote : false,
        uploadJson : '/admin/upload/kindeditor',
        width:'800px',
        height:'400px',
    });
})










// var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
// var csrftoken = "";
// var KK;
// KindEditor.ready(function(K){
//      KK = K;
// });
// function searchtoken() {
//     if (csrfitems.length > 0) {
//         csrftoken = csrfitems[0].value;
//         clearInterval(_interval);
//         console.log("csrftoken:" + csrftoken);
//         window.editor = KK.create('#id_doc_content',{
//             uploadJson: '/kin/uploadImg/',
//             extraFileUploadParams: {
//                     csrfmiddlewaretoken:csrftoken
//                 },
//             // 指定大小
//             width:'800px',
//             height:'400px',
//         });
//     }
// }
// //最重要就是下面这个函数，不然，获取不到csrftoken ,目测网上的教程都没提到这一点
// _interval = setInterval(searchtoken, 500);