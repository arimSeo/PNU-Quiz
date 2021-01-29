window.onload = initall;
var saveAnsButton;
var checkButton;

function initall() {
    saveAnsButton = document.getElementById('save_ans');
    saveAnsButton.onclick = save_ans;

    checkButton = document.querySelectorAll('.options');
    for (let i = 0; i < checkButton.length; i++) {
        $(checkButton).eq(i).click(function () {
            // eq(i) == [i]
            $(checkButton).removeClass('active');
            $(checkButton).eq(i).addClass('active');
        });
    }
};

// function save_ans(){
//     var ans = $("input:radio[name=name]:checked").val();
//     // ans = ans ? ans : alert("no")
//     var url = '/save_ans?ans='+ans
//     var req = new XMLHttpRequest();
//     req.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//          alert(req.responseText)
//         };
//     };
//     req.open("GET", url, true);
//     req.send();
// }