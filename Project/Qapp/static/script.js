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
