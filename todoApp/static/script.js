const taskItems = document.querySelectorAll('.task-item');

taskItems.forEach(item => {
  item.addEventListener('click', () => {
    item.classList.toggle('completed');
  });
});