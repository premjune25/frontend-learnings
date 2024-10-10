// Get the necessary elements
const taskInput = document.getElementById('taskInput');
const addTaskButton = document.getElementById('addTaskButton');
const taskList = document.getElementById('taskList');

// Function to add a new task
function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText !== '') {
        const taskItem = document.createElement('li');
        taskItem.innerHTML = `
            <span>${taskText}</span>
            <button class="delete-btn">Delete</button>
        `;
        taskList.appendChild(taskItem);

        // Mark task as completed on click
        taskItem.addEventListener('click', function() {
            taskItem.classList.toggle('completed');
        });

        // Delete task
        taskItem.querySelector('.delete-btn').addEventListener('click', function() {
            taskList.removeChild(taskItem);
        });

        // Clear the input field
        taskInput.value = '';
    }
}

// Add task when the button is clicked
addTaskButton.addEventListener('click', addTask);

// Allow adding a task by pressing 'Enter'
taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});
