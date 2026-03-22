/* JavaScript Document

Tooplate 2152 Event Invitation

https://www.tooplate.com/view/2152-event-invitation

*/

// Dark Mode Toggle
const lightModeBtn = document.getElementById('lightMode');
const darkModeBtn = document.getElementById('darkMode');
const htmlElement = document.documentElement;

// Check for saved theme preference or default to dark mode
const currentTheme = localStorage.getItem('theme') || 'dark';
htmlElement.setAttribute('data-theme', currentTheme);

// Update active state
if (currentTheme === 'dark') {
   darkModeBtn.classList.add('active');
} else {
   lightModeBtn.classList.add('active');
}

lightModeBtn.addEventListener('click', () => {
   htmlElement.setAttribute('data-theme', 'light');
   localStorage.setItem('theme', 'light');
   lightModeBtn.classList.add('active');
   darkModeBtn.classList.remove('active');
});

darkModeBtn.addEventListener('click', () => {
   htmlElement.setAttribute('data-theme', 'dark');
   localStorage.setItem('theme', 'dark');
   darkModeBtn.classList.add('active');
   lightModeBtn.classList.remove('active');
});

// Countdown Timer
function updateCountdown() {
   const eventDate = new Date('2025-12-31T17:00:00').getTime();
   const now = new Date().getTime();
   const difference = eventDate - now;

   if (difference > 0) {
      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((difference % (1000 * 60)) / 1000);

      document.getElementById('days').textContent = String(days).padStart(2, '0');
      document.getElementById('hours').textContent = String(hours).padStart(2, '0');
      document.getElementById('minutes').textContent = String(minutes).padStart(2, '0');
      document.getElementById('seconds').textContent = String(seconds).padStart(2, '0');
   } else {
      document.getElementById('days').textContent = '00';
      document.getElementById('hours').textContent = '00';
      document.getElementById('minutes').textContent = '00';
      document.getElementById('seconds').textContent = '00';
   }
}

updateCountdown();
setInterval(updateCountdown, 1000);

// Form Handling
const rsvpForm = document.getElementById('rsvpForm');
const successMessage = document.getElementById('successMessage');

rsvpForm.addEventListener('submit', function (e) {
   e.preventDefault();

   const formData = new FormData(rsvpForm);
   const data = {
      firstName: formData.get('firstName'),
      lastName: formData.get('lastName'),
      email: formData.get('email'),
      phone: formData.get('phone'),
      attending: formData.get('attending'),
      guests: formData.get('guests'),
      dietary: formData.get('dietary'),
      submittedAt: new Date().toLocaleString()
   };

   // REPLACE THIS URL with your Google Apps Script URL
   const scriptURL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';

   // Send to Google Sheets
   fetch(scriptURL, {
         method: 'POST',
         body: JSON.stringify(data),
         headers: {
            'Content-Type': 'application/json'
         }
      })
      .then(response => response.json())
      .then(result => {
         console.log('Success:', result);

         // Show success message
         successMessage.classList.add('show');
         rsvpForm.reset();

         setTimeout(() => {
            successMessage.classList.remove('show');
         }, 5000);

         successMessage.scrollIntoView({
            behavior: 'smooth',
            block: 'center'
         });
      })
      .catch(error => {
         console.error('Error:', error);
         alert('There was an error submitting your RSVP. Please try again.');
      });
});