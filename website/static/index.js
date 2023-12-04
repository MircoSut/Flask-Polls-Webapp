// Delete Polls
function deletePoll(pollId) {
    fetch("/delete-poll", {
        method: "POST",
        body: JSON.stringify({ pollId: pollId }),
    }).then((_res) => {
        window.location.href = "/";
    });
  }
  
// Search Bar
document.addEventListener("DOMContentLoaded", function () {
  // Event listener for pressing Enter in the search input field
  const searchInput = document.getElementById("pollSearch");
  searchInput.addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
      searchPolls();
    }
  });

  // Event listener for the "Search" button
  const searchButton = document.querySelector(".search__btn");
  searchButton.addEventListener("click", searchPolls);

  // Event listener for the "Clear Filter" button
  const clearFilterButton = document.querySelector(".clear-filter__btn");
  clearFilterButton.addEventListener("click", clearFilter);

  // Function to search and filter polls
  function searchPolls() {
    const searchTerm = searchInput.value.toLowerCase();
    const pollElements = document.querySelectorAll(".whole-poll");

    pollElements.forEach((pollElement) => {
      const pollText = pollElement.innerText.toLowerCase();
      if (pollText.includes(searchTerm)) {
        pollElement.style.display = "block";
      } else {
        pollElement.style.display = "none";
      }
    });
  }

  // Function to clear the search filter
  function clearFilter() {
    searchInput.value = ""; // Reset the search input value

    // Show all the polls (remove any filters)
    const pollElements = document.querySelectorAll(".whole-poll");
    pollElements.forEach((pollElement) => {
      pollElement.style.display = "block";
    });
  }
});


// Add an event listener to the document to handle clicks on answer elements
document.addEventListener("click", function (event) {
  if (event.target.classList.contains("answer")) {
    // Extract the index from the id attribute
    const id = event.target.id;
    const index = id.split("-")[1]; // Assuming the id format is "answer-{index}"
    // console.log(index) debugging
    // Call the markanswer function with the index
    markanswer(index);
  }
});

function markanswer(i) {
  const selectAnswer = +i;
  const poll = event.target.closest(".poll");

  try {
    poll.querySelector(".answer.selected").classList.remove("selected");
  } catch (error) {}

  const answers = poll.querySelectorAll(".answer");
  answers[+i].classList.add("selected");

  showresults(poll);
}

function showresults(poll) {
  const answers = poll.querySelectorAll(".answer");
  const selectedAnswer = poll.querySelector(".answer.selected");

  answers.forEach((answer) => {
    let percentage = 0;

    if (answer === selectedAnswer) {
      percentage = 100;
    } else {
      percentage = 50;
    }

    answer.querySelector(".percentage_bar").style.width = percentage + "%";
    answer.querySelector(".percentage_value").innerText = percentage + "%";
  });
}


