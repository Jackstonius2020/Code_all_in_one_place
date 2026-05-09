// =========================================
// AI Assistance: This code was developed with the help of Claude AI (Anthropic).
// Prompt used: "Help me build a cybersecurity awareness website for a university
// web development assignment based on the KnowYourCyber client brief."
// Source: Claude AI by Anthropic (claude.ai)
// =========================================

// =========================================
// main.js
// Global JavaScript used across all pages
// =========================================


// =========================================
// Highlight the Active Navigation Link
// =========================================

// Get the filename of the current page (e.g. "threats.html")
const currentPage = window.location.pathname.split('/').pop();

// Get all navigation links on the page
const navLinks = document.querySelectorAll('.nav-links a');

// Loop through each link and check if it matches the current page
navLinks.forEach(link => {
  // Get just the filename from the link's href (e.g. "threats.html")
  const linkPage = link.getAttribute('href').split('/').pop();

  // If this link matches the current page, mark it as active
  if (linkPage === currentPage) {
    link.classList.add('active');
  } else {
    // Remove active class from all other links
    link.classList.remove('active');
  }
});


// =========================================
// Smooth Scroll to Top on Page Load
// =========================================

// Scroll the page to the very top when it first loads
window.addEventListener('load', () => {
  window.scrollTo(0, 0);
});


// =========================================
// Footer Year - Always Shows Current Year
// =========================================

// Find all footer elements on the page
const footers = document.querySelectorAll('footer p');

// Update each footer to show the current year automatically
footers.forEach(footer => {
  // Replace the hardcoded 2024 year with the actual current year
  footer.innerHTML = footer.innerHTML.replace(
    '2024',
    new Date().getFullYear()
  );
});


// =========================================
// Console Welcome Message
// =========================================

// A message shown in the browser's developer console
// This is good practice and shows the site is well maintained
console.log(
  '%cKnowYourCyber',
  'color: #ff3333; font-size: 20px; font-weight: bold;'
);
console.log(
  '%cStay safe online. If you are a developer, thank you for checking our code!',
  'color: #cccccc; font-size: 12px;'
);