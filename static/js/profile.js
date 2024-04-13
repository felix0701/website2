document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('editOverlay').style.display = 'none';
    const editButton = document.getElementById('editButton');
  
    editButton.addEventListener('click', function() {
      document.getElementById('editOverlay').style.display = 'block';
    });
  
    const saveButton = document.getElementById('saveButton');
  
    saveButton.addEventListener('click', function() {
      const editedName = document.getElementById('editName').value;
      const editedDOB = document.getElementById('editDOB').value;
      const editedGender = document.getElementById('editGender').value;
      const editedAddress = document.getElementById('editAddress').value;
      const editedBio = document.getElementById('editBio').value;
      const editedSocialLinks = document.getElementById('editSocialLinks').value;
  
      const formData = new FormData();
      formData.append('editName', editedName);
      formData.append('editDOB', editedDOB);
      formData.append('editGender', editedGender);
      formData.append('editAddress', editedAddress);
      formData.append('editBio', editedBio);
      formData.append('editSocialLinks', editedSocialLinks);
  
      function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }
  
      const csrftoken = getCookie('csrftoken');
      if (csrftoken === null) {
        console.error('CSRF token not found');
        return;
      }
  
      fetch(window.location.href, {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrftoken,
        },
      })
      .then(response => {
        if (response.ok) {
          console.log('Form submitted successfully');
          window.location.reload(); // Reload the page after successful submission
        } else {
          console.error('Error submitting form data.');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    });
  
    // Fetch user profile data when the page loads
    fetch(window.location.href, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    })
    .then(response => response.json())
    .then(data => {
      // Update the user profile information
      document.getElementById('name').textContent = data.name;
      document.getElementById('dob').textContent = data.dob;
      document.getElementById('gender').textContent = data.gender;
      document.getElementById('address').textContent = data.address;
      document.getElementById('bio').textContent = data.bio;
      document.getElementById('socialLinks').textContent = data.social_links;
    })
    .catch(error => {
      console.error('Error fetching user profile:', error);
    });
  });
  