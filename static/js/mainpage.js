// Firebase configuration and initialization
const firebaseConfig = {
    // Your Firebase config details here
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Firebase database reference
const db = firebase.database();

// Function to load posts from Firebase and display in the all-posts div
function loadPosts() {
    // Fetch posts from Firebase and display in the all-posts div
    // You'd need to implement Firebase data retrieval here
}

// Event listener for submitting a user's post
document.getElementById('userPostForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const userPostContent = document.getElementById('userPostContent').value;

    // Store the user's post data in Firebase
    // You'd need to implement Firebase data storage here

    // After storing the data, reload all the posts
    loadPosts();
});

// Load posts when the page loads
loadPosts();
