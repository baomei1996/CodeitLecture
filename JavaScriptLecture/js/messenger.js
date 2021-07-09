const chatBox = document.querySelector('#chat-box');
const input = document.querySelector('#input');
const send = document.querySelector('#send');

function sendMyText () {
  const newMessege = input.value;
  if(newMessege) {
    const div = document.createElement('div');
    div.classList.add('bubble', 'my-bubble');
    div.innerText = newMessege;
    chatBox.append(div);
  } else {
    alert ('메세지를 입력하세요..');
  }

  input.value = '';
}

send.addEventListener('click', sendMyText);

function enterMyText (e) {
  if(e.key == 'Enter' && !e.shiftKey) {
    sendMyText();  
    e.preventDefault();
  }
  
}

input.addEventListener('keypress', enterMyText);