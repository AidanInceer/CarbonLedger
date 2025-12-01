from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TransactionForm
from .models import Project, Transaction, UserProfile


@login_required
def home(request, project_id):
    """Display all transactions for a specific project."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    transactions = Transaction.objects.filter(project=project)
    form = TransactionForm()
    return render(request, 'transactions/home.html', {
        'transactions': transactions,
        'form': form,
        'project': project,
    })


@login_required
def add_transaction(request, project_id):
    """Add a new transaction to a project."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.project = project
            transaction.save()
            messages.success(request, 'Transaction added successfully!')
            return redirect('home', project_id=project.id)
    return redirect('home', project_id=project.id)


@login_required
def delete_transaction(request, project_id, pk):
    """Delete a transaction."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    transaction = get_object_or_404(Transaction, pk=pk, project=project)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transaction deleted successfully!')
    return redirect('home', project_id=project.id)


def login_view(request):
    """User login."""
    if request.user.is_authenticated:
        return redirect('projects')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Create profile if doesn't exist
            UserProfile.objects.get_or_create(user=user)
            return redirect('projects')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'transactions/login.html')


def register_view(request):
    """User registration."""
    if request.user.is_authenticated:
        return redirect('projects')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validation
        if not username or not password:
            messages.error(request, 'Username and password are required.')
        elif password != password_confirm:
            messages.error(request, 'Passwords do not match.')
        elif len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            # Create profile with light theme default
            UserProfile.objects.create(user=user, theme='light')
            # Log them in
            login(request, user)
            messages.success(request, f'Welcome to CarbonLedger, {username}!')
            return redirect('projects')
    
    return render(request, 'transactions/register.html')


@login_required
def logout_view(request):
    """User logout."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required
def settings_view(request):
    """User settings page."""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        theme = request.POST.get('theme')
        if theme in ['light', 'dark']:
            profile.theme = theme
            profile.save()
            messages.success(request, f'Theme changed to {theme} mode.')
        return redirect('settings')
    
    return render(request, 'transactions/settings.html', {'profile': profile})


@login_required
def account_view(request):
    """User account page."""
    return render(request, 'transactions/account.html')


@login_required
def projects_view(request):
    """List all projects for the user."""
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'transactions/projects.html', {'projects': projects})


@login_required
def create_project(request):
    """Create a new project."""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        if name:
            try:
                project = Project.objects.create(
                    name=name,
                    description=description,
                    owner=request.user
                )
                messages.success(request, f'Project "{name}" created successfully!')
                return redirect('home', project_id=project.id)
            except Exception as e:
                messages.error(request, 'A project with this name already exists.')
        else:
            messages.error(request, 'Project name is required.')
    return redirect('projects')


@login_required
def delete_project(request, project_id):
    """Delete a project."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        project_name = project.name
        project.delete()
        messages.success(request, f'Project "{project_name}" deleted successfully!')
    return redirect('projects')


@login_required
def project_reporting(request, project_id):
    """Project reporting page."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    return render(request, 'transactions/project_reporting.html', {'project': project})


@login_required
def project_configuration(request, project_id):
    """Project configuration page."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    return render(request, 'transactions/project_configuration.html', {'project': project})


@login_required
def project_summary(request, project_id):
    """Project summary/notes page."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    return render(request, 'transactions/project_summary.html', {'project': project})


@login_required
def project_team(request, project_id):
    """Project team members page."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    return render(request, 'transactions/project_team.html', {'project': project})
