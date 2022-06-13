// Atualização das figuras de um lado
function runSimulation() {
    req = $.ajax({
        url : '/run',
        type : 'POST',
        data : {}
    });
    req.done(function(data) {
        document.getElementById("div-group-stage").innerHTML = data.content_group_stage;
        document.getElementById("div-knockout").innerHTML = data.content_knockout;
    });
}