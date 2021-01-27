window.onload = initall;

function initall() {
	$(".result_content").hide();
	setTimeout(function () {
        $(".loading").fadeOut(400);
        // document.getElementById('loading').style.display = "none";
        // results.style.display = "block";
        $(".result_content").fadeIn(4000);
    }, 2500);
}
