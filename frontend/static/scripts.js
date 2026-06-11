document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('todoForm');
    form.addEventListener('submit', function(event) {
        const taskInput = form.querySelector('input[name="task"]');
        const dateInput = form.querySelector('input[name="due_date"]');
        if (!taskInput.value || !dateInput.value) {
            event.preventDefault();
            alert('Please enter a task and select a due date.');
        }
    });

    const deleteLinks = document.querySelectorAll('a.delete');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this task?')) {
                event.preventDefault();
            }
        });
    });
});