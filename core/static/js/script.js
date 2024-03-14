var modalBtns = document.querySelectorAll('.delete-button');
var modals = document.querySelectorAll('.modal');
var spans = document.querySelectorAll('.close');

modalBtns.forEach(function(btn, index) {
    btn.onclick = function() {
        modals[index].style.display = "block";
    }
});

spans.forEach(function(span, index) {
    span.onclick = function() {
        modals[index].style.display = "none";
    }
});

window.onclick = function(event) {
    modals.forEach(function(modal) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
}


