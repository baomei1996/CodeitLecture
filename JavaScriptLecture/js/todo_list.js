const toDoList = document.querySelector('#to-do-list');

function addNewToDo(text) {
  const li = document.createElement('li');
  li.textContent = text;
  toDoList.append(li);

}

addNewToDo('자바스크립트 공부하기');
addNewToDo('고양이 화장실 청소하기');
addNewToDo('고양이 장난감 쇼핑하기');