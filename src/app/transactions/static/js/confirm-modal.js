// Custom Confirmation Modal
let confirmModalCallback = null;

function showConfirmModal(options) {
    return new Promise((resolve) => {
        const overlay = document.getElementById('confirmModalOverlay') || createConfirmModal();
        const modal = overlay.querySelector('.confirm-modal');

        // Set content
        modal.querySelector('.confirm-modal-icon').textContent = options.icon || '⚠️';
        modal.querySelector('.confirm-modal-title').textContent = options.title || 'Confirm Action';
        modal.querySelector('.confirm-modal-message').textContent = options.message || 'Are you sure?';

        const confirmBtn = modal.querySelector('.confirm-modal-confirm');
        const cancelBtn = modal.querySelector('.confirm-modal-cancel');

        confirmBtn.textContent = options.confirmText || 'Confirm';
        cancelBtn.textContent = options.cancelText || 'Cancel';

        // Show modal
        overlay.classList.add('active');

        // Handle confirmation
        const handleConfirm = () => {
            cleanup();
            resolve(true);
        };

        const handleCancel = () => {
            cleanup();
            resolve(false);
        };

        const cleanup = () => {
            overlay.classList.remove('active');
            confirmBtn.removeEventListener('click', handleConfirm);
            cancelBtn.removeEventListener('click', handleCancel);
            overlay.removeEventListener('click', handleOverlayClick);
            document.removeEventListener('keydown', handleEscape);
        };

        const handleOverlayClick = (e) => {
            if (e.target === overlay) {
                handleCancel();
            }
        };

        const handleEscape = (e) => {
            if (e.key === 'Escape') {
                handleCancel();
            }
        };

        confirmBtn.addEventListener('click', handleConfirm);
        cancelBtn.addEventListener('click', handleCancel);
        overlay.addEventListener('click', handleOverlayClick);
        document.addEventListener('keydown', handleEscape);

        // Focus confirm button
        confirmBtn.focus();
    });
}

function createConfirmModal() {
    const overlay = document.createElement('div');
    overlay.id = 'confirmModalOverlay';
    overlay.className = 'confirm-modal-overlay';
    overlay.innerHTML = `
        <div class="confirm-modal">
            <div class="confirm-modal-icon"></div>
            <h2 class="confirm-modal-title"></h2>
            <p class="confirm-modal-message"></p>
            <div class="confirm-modal-actions">
                <button class="confirm-modal-cancel"></button>
                <button class="confirm-modal-confirm"></button>
            </div>
        </div>
    `;
    document.body.appendChild(overlay);
    return overlay;
}

// Helper functions for common confirmations
async function confirmDelete(itemName, itemType = 'item') {
    return await showConfirmModal({
        icon: '🗑️',
        title: `Delete ${itemType}?`,
        message: `Are you sure you want to delete "${itemName}"? This action cannot be undone.`,
        confirmText: 'Delete',
        cancelText: 'Cancel'
    });
}

async function confirmDeleteProject(projectName) {
    return await showConfirmModal({
        icon: '🗑️',
        title: `Delete Project?`,
        message: `Are you sure you want to delete "${projectName}"? All transactions will be permanently lost!`,
        confirmText: 'Delete Project',
        cancelText: 'Cancel'
    });
}

async function confirmRemoveMember(username) {
    return await showConfirmModal({
        icon: '👤',
        title: 'Remove Member?',
        message: `Are you sure you want to remove "${username}" from this project?`,
        confirmText: 'Remove',
        cancelText: 'Cancel'
    });
}

// Handle form submissions with confirmation
function setupConfirmableForms() {
    document.querySelectorAll('[data-confirm]').forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const confirmType = form.dataset.confirm;
            const confirmMessage = form.dataset.confirmMessage;
            const confirmTitle = form.dataset.confirmTitle || 'Confirm Action';
            const confirmIcon = form.dataset.confirmIcon || '⚠️';

            let confirmed = false;

            if (confirmType === 'delete-project') {
                confirmed = await confirmDeleteProject(confirmMessage);
            } else if (confirmType === 'remove-member') {
                confirmed = await confirmRemoveMember(confirmMessage);
            } else if (confirmType === 'delete-transaction') {
                confirmed = await confirmDelete(confirmMessage, 'transaction');
            } else {
                confirmed = await showConfirmModal({
                    icon: confirmIcon,
                    title: confirmTitle,
                    message: confirmMessage
                });
            }

            if (confirmed) {
                form.submit();
            }
        });
    });
}

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupConfirmableForms);
} else {
    setupConfirmableForms();
}
