// Updating the simulated results
function runSimulation() {
    request = $.ajax({
        url : "/run",
        type : "POST",
        data : {}
    });
    request.done(function(data) {
        $("#div-group-stage").html(data.content_group_stage);
        $("#div-knockout").html(data.content_knockout);
    });
}