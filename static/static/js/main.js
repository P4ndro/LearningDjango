console.log("Django Project JS Loaded");

// Custom Delete Confirmation Modal
document.addEventListener('DOMContentLoaded', function() {
    // Get or create modal
    let modal = document.getElementById('deleteModal');
    if (!modal) {
        modal = createDeleteModal();
        document.body.appendChild(modal);
    }

    const cancelBtn = document.getElementById('cancelDelete');
    const confirmBtn = document.getElementById('confirmDelete');
    let currentForm = null;

    // Add click handlers to all delete buttons
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            currentForm = this.closest('form');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        });
    });

   
    if (cancelBtn) {
        cancelBtn.addEventListener('click', function() {
            closeModal();
        });
    }

    
    if (confirmBtn) {
        confirmBtn.addEventListener('click', function() {
            if (currentForm) {
                currentForm.submit();
            }
        });
    }

  
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

  
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = ''; // Restore scrolling
        currentForm = null;
    }
});


function createDeleteModal() {
    const modal = document.createElement('div');
    modal.id = 'deleteModal';
    modal.className = 'delete-modal';
    modal.innerHTML = `
        <div class="delete-modal-content">
            <div class="delete-modal-icon">🗑️</div>
            <h2>Delete Post?</h2>
            <p>Are you sure you want to delete this post? This action cannot be undone.</p>
            <div class="delete-modal-actions">
                <button type="button" class="btn-cancel-delete" id="cancelDelete">Cancel</button>
                <button type="button" class="btn-confirm-delete" id="confirmDelete">Yes, Delete</button>
            </div>
        </div>
    `;
    return modal;
}