window.onload = initall;

function initall() {
    // $(".result_content").hide();
    setTimeout(function () {
        $(".loading").fadeOut(400);
        $(".result_content").fadeIn(4000);
    }, 2500);

    // 유저 점수 bar 기능
    // 각 실제 점수
    var average_score = document.getElementById("average_score").innerText
    var user_score = document.getElementById("user_score").innerText

    // 각 bar
    var score = document.getElementById("score_bar")
    var myscore = document.getElementById("score_bar2")

    average_score_percent = average_score * 25
    user_score_percent = user_score * 25

    // 차오르는 효과 안 할 때
    // document.getElementById("content_bar").style.width = `${average_score_percent}%`;
    // document.getElementById("content_bar2").style.width = `${user_score_percent}%`;

    var first_width = 0;
    var id = setInterval(frame, 50);
    function frame() {
        if (first_width >= `${average_score_percent}`) {
            clearInterval(id);
        } else {
            first_width++;
            score.style.width = first_width + "%";
            // score.innerHTML = first_width+"%";
        }
    }
    var first_width2 = 0;
    var id2 = setInterval(frame2, 50);
    function frame2() {
        if (first_width2 >= `${user_score_percent}`) {
            clearInterval(id2);
        } else {
            first_width2++;
            myscore.style.width = first_width2 + "%";
            // myscore.innerHTML = first_width+"%";
        }
    }
};
