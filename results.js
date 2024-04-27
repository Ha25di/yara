/*  For displaying results in division for finance and statistics articles */

document.addEventListener('DOMContentLoaded', function () {
    const financeListItems = document.querySelectorAll('.finance li');
    const statisticsListItems = document.querySelectorAll('.statistics li');
    const imagePlaceholder = document.getElementById('imagePlaceholder');
    const dropdownContent = document.getElementById('dropdownContent');


function loadDropdown(category, title, jsonFile) {
    fetch(jsonFile)
        .then(response => response.json())
        .then(data => {
            const matchingItems = data.filter(item => item.categories.includes(category));
            const listHtml = matchingItems.map(item => 
                `<li><b>${item.title}</b> <br> <a href="https://arxiv.org/abs/${item.id}" target="_blank">https://arxiv.org/abs/${item.id}</a></li>`
            ).join('');
            dropdownContent.innerHTML = `<div>${title} </div><ul>${listHtml}</ul>`;
            imagePlaceholder.style.display = 'none';
            dropdownContent.style.display = 'block';
        });
}


  financeListItems.forEach(item => {
      item.addEventListener('click', function () {
          loadDropdown(item.dataset.category, item.innerHTML, 'finance.json');
      });
  });

  statisticsListItems.forEach(item => {
    item.addEventListener('click', function () {
        loadDropdown(item.dataset.category, item.innerHTML, 'statistics.json');
    });
});

  document.addEventListener('click', function (e) {
      if (!dropdownContent.contains(e.target) && !imagePlaceholder.contains(e.target)) {
          dropdownContent.style.display = 'none';
          imagePlaceholder.style.display = 'block';
      }
  });
});
/****************************************************************/



/*  For displaying results in division for other articles */
document.addEventListener('DOMContentLoaded', function () {
    const mathListItems = document.querySelectorAll('.math li');
    const physicsListItems = document.querySelectorAll('.physics li');
    const csListItems = document.querySelectorAll('.cs li');
    const biologyListItems = document.querySelectorAll('.biology li');




    const imagePlaceholder2 = document.getElementById('imagePlaceholder2');
    const dropdownContent2 = document.getElementById('dropdownContent2');


function loadDropdown2(category, title, jsonFile) {
    fetch(jsonFile)
        .then(response => response.json())
        .then(data => {
            const matchingItems = data.filter(item => item.categories.includes(category));
            const listHtml = matchingItems.map(item => 
                `<li><b>${item.title}</b> <br> <a href="https://arxiv.org/abs/${item.id}" target="_blank">https://arxiv.org/abs/${item.id}</a></li>`
            ).join('');
            dropdownContent2.innerHTML = `<div>${title} </div><ul>${listHtml}</ul>`;
            imagePlaceholder2.style.display = 'none';
            dropdownContent2.style.display = 'block';
        });
}


  mathListItems.forEach(item => {
      item.addEventListener('click', function () {
          loadDropdown2(item.dataset.category, item.innerHTML, 'math.json');
      });
  });

  physicsListItems.forEach(item => {
    item.addEventListener('click', function () {
        loadDropdown2(item.dataset.category, item.innerHTML, 'physics.json');
    });
});

biologyListItems.forEach(item => {
    item.addEventListener('click', function () {
        loadDropdown2(item.dataset.category, item.innerHTML, 'biology.json');
    });
});

csListItems.forEach(item => {
    item.addEventListener('click', function () {
        loadDropdown2(item.dataset.category, item.innerHTML, 'computer_science.json');
    });
});

  document.addEventListener('click', function (e) {
      if (!dropdownContent2.contains(e.target) && !imagePlaceholder2.contains(e.target)) {
          dropdownContent2.style.display = 'none';
          imagePlaceholder2.style.display = 'block';
      }
  });
});
/****************************************************************/


/****************** For Contact Us **************************/
$(document).ready(function() {
    $('#contactForm').submit(function(event) {
      event.preventDefault(); // Prevent default form submission
      const formData = $(this).serialize(); // Serialize form data
      $.ajax({
        type: 'POST',
        url: 'http://localhost:3001/send',
        data: JSON.stringify({
          name: $('input[name="name"]').val(),
          email: $('input[name="email"]').val(),
          message: $('textarea[name="message"]').val(),
        }),
        contentType: "application/json", // Make sure to set Content-Type to 'application/json'
        success: function(response) {
          //alert('Email sent successfully');
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Your email has been sent successfully",
            showConfirmButton: false,
            timer: 1500
          });
          $('#contactForm')[0].reset(); // Clear form fields
        },
        error: function(error) {
          console.error(error);
          alert('Error sending email');
        }
      });
      
    });
  });
  /****************************************************************/