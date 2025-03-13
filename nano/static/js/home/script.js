document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("dark-mode-toggle");
  const body = document.body;
  const searchInput = document.getElementById("search");
  const blogPosts = document.querySelectorAll(".blog-post");

  // Check if dark mode was previously enabled
  if (localStorage.getItem("dark-mode") === "enabled") {
    body.classList.add("dark-mode");
    toggleButton.textContent = "☀️";
  }

  toggleButton.addEventListener("click", function () {
    body.classList.toggle("dark-mode");

    if (body.classList.contains("dark-mode")) {
      localStorage.setItem("dark-mode", "enabled");
      toggleButton.textContent = "☀️";
    } else {
      localStorage.setItem("dark-mode", "disabled");
      toggleButton.textContent = "🌙";
    }
  });

  // Search filter
  searchInput.addEventListener("input", function () {
    const searchText = searchInput.value.toLowerCase();
    blogPosts.forEach((post) => {
      const title = post.querySelector("h2 a").textContent.toLowerCase();
      if (title.includes(searchText)) {
        post.style.display = "block";
      } else {
        post.style.display = "none";
      }
    });
  });
});
