// Quiz JS
const alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
const totalQuestions = 20;

function getRandomQuestions() {
  let shuffled = [...alphabets].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, totalQuestions);
}

let questions = [];
let currentQ = 0;
let score = 0;

const quizBox = document.getElementById("quiz-box");
const nextBtn = document.getElementById("next-btn");
const restartBtn = document.getElementById("restart-btn");

function generateQuestions() {
  questions = getRandomQuestions().map(letter => {
    let options = [letter];
    while (options.length < 4) {
      let rand = alphabets[Math.floor(Math.random() * alphabets.length)];
      if (!options.includes(rand)) options.push(rand);
    }
    options.sort(() => 0.5 - Math.random());
    return {
      question: "Which alphabet is this?",
      image: `../static/images/${letter}.PNG`,
      options,
      answer: letter
    };
  });
}

function loadQuestion() {
  const q = questions[currentQ];
  quizBox.innerHTML = `
    <p><strong>Q${currentQ + 1} of ${questions.length}:</strong> ${q.question}</p>
    <img src="${q.image}" alt="${q.answer} sign">
    ${q.options.map(opt =>
      `<button class="option-btn" onclick="checkAnswer(this, '${opt}')">${opt}</button>`
    ).join("")}
  `;
}

function checkAnswer(btn, answer) {
  const q = questions[currentQ];
  const optionBtns = document.querySelectorAll(".option-btn");

  optionBtns.forEach(b => {
    b.disabled = true;
    if (b.textContent === q.answer) {
      b.classList.add("correct");
    }
  });

  if (answer === q.answer) {
    score++;
  } else {
    btn.classList.add("wrong");
  }

  nextBtn.style.display = "block";
}

nextBtn.addEventListener("click", () => {
  currentQ++;
  if (currentQ < questions.length) {
    loadQuestion();
    nextBtn.style.display = "none";
  } else {
    quizBox.innerHTML = `<h2>Quiz Finished!</h2><p>Your Score: ${score}/${questions.length}</p>`;
    nextBtn.style.display = "none";
    restartBtn.style.display = "inline-block";
  }
});

restartBtn.addEventListener("click", () => {
  score = 0;
  currentQ = 0;
  generateQuestions();
  loadQuestion();
  restartBtn.style.display = "none";
  nextBtn.style.display = "none";
});

// Start quiz
generateQuestions();
loadQuestion();
