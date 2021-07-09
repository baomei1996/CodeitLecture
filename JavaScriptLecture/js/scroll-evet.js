let lastScrollY = 0;

function onScroll() {
  const nav = document.querySelector('#nav');
  const toTop = document.querySelector('#to-top');
  const STANDARD = 30;

  if(window.scrollY > STANDARD) {
    nav.classList.add('shadow');
    toTop.classList.add('show');

  }else {
    nav.classList.remove('shadow');
    toTop.classList.remove('show');
  }

  if(window.scrollY > lastScrollY) {
    nav.classList.add('lift-up');
  } else {
    nav.classList.remove('lift-up');
  }
  lastScrollY = window.scrollY;
}

window.addEventListener('scroll', onScroll);

