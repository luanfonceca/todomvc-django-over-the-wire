Array.from(document.querySelectorAll('.toggle')).forEach((todo) => {
  todo.addEventListener('click', (e) => {
    const pk = e.target.dataset.pk;
    const isChecked = e.target.checked;

    fetch(`/api/todo/${pk}/`, {
      headers: {'Content-Type': 'application/json;'},
      method: 'PUT',
      body: JSON.stringify({
        is_completed: isChecked,
      })
    }).then(res => Turbo.visit(window.location));
  });
});

Array.from(document.querySelectorAll('.view label')).forEach((todo) => {
  todo.addEventListener('dblclick', (e) => {
    e.target.closest('li').classList.add('editing');

    const input = document.querySelector('.editing .edit');
    input.selectionStart = input.selectionEnd = input.value.length;
    input.focus();
  });
});

document.addEventListener('keydown', (e) => {
  const editingToDo = document.querySelector('.editing .edit');

  if (!editingToDo) {
    return true;
  }

  if (e.key === 'Escape'){
    e.target.closest('li').classList.remove('editing');
  }
});

document.addEventListener('click', (e) => {
  const editingToDo = document.querySelector('.editing .edit');

  if (!editingToDo) {
    return true;
  }

  if (!e.composedPath().includes(editingToDo)) {
    editingToDo.closest('li').classList.remove('editing');
  } 
});
