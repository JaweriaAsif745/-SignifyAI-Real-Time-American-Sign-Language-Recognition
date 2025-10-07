const sets = document.querySelectorAll('.set');
if (!sets.length) throw new Error('No .set elements found');

// show the first set
sets[0].classList.add('active');
sets[0].style.zIndex = 100;

let lastIndex = 0;

window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  const vh = window.innerHeight;
  const index = Math.min(Math.floor(scrollY / vh), sets.length - 1);

  if (index > lastIndex) {
    // scrolling DOWN → slide UP new cards
    for (let i = lastIndex + 1; i <= index; i++) {
      sets[i].classList.add('active');
      sets[i].classList.remove('slide-down');
      sets[i].style.zIndex = 100 + i;
    }
  } else if (index < lastIndex) {
    // scrolling UP → slide DOWN cards
    for (let i = lastIndex; i > index; i--) {
      sets[i].classList.remove('active');
      sets[i].classList.add('slide-down');
      sets[i].style.zIndex = 100 + i; // keep above until animation finishes
      // optional cleanup after animation
      setTimeout(() => {
        sets[i].style.zIndex = 0;
      }, 600); // matches transition time
    }
  }

  lastIndex = index;
});
