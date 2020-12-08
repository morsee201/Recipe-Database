from django.shortcuts import render, redirect
from django.views import generic
from gradebook.models import Project, Assignment, Test, Submit
from gradebook.forms import ProjectAssignmentForm, NewAcceptanceTest
from gradebook.forms import NewProject, NewAssignment, NewSubmission
from django.contrib.auth.models import User


#This view displays the home page
def home(request):
	return render(request, 'gradebook/home.html')

# This view displays the project assignment page
def Assign(request):
	if request.method == 'POST':
		form = ProjectAssignmentForm(request.POST)
		if form.is_valid():
			project_name = form.cleaned_data.get('projects')
			assigned = form.cleaned_data.get('assigned_students')
			project_name.assigned_students.add(*assigned)
			return redirect('home')
	else:
		form = ProjectAssignmentForm()
	return render(request,'gradebook/Assign.html', {'form':form})


# This view displays the form for an instructor to create a new acceptance test
def newTest(request):
	if request.method == 'POST':
		form = NewAcceptanceTest(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			description = form.cleaned_data.get('description')
			assignment = form.cleaned_data.get('attached_assignment')
			view_status = form.cleaned_data.get('view_status')
			
			test = Test.objects.create(name = name,
									   description = description,
									   attached_assignment = assignment,
									   test_file = request.FILES['test_file'],
									   view = view_status)
			
			return redirect('test')
	else:
		form = NewAcceptanceTest()
	return render(request,'gradebook/newTest.html', {'form':form})

#This view displays the form for an instructor to create a project
def newProject(request):
	if request.method == 'POST':
		form = NewProject(request.POST)
		if form.is_valid():
			name_of_project = form.cleaned_data.get('name_of_project')
			full_description = form.cleaned_data.get('detailed_description')
			students = form.cleaned_data.get('assigned_students')
			assignments = form.cleaned_data.get('assignment_list')

			project = Project.objects.create(line_description = name_of_project,
									         full_description = full_description,)
			
			project.assigned_students.add(*students)
			project.assignment_list.add(*assignments)

			return redirect('projects')
	else:
		form = NewProject()
	return render(request,'gradebook/newProject.html', {'form':form})

#This view displays the form for an instructor to create a new assignment
def newAssignment(request):
	if request.method == 'POST':
		form = NewAssignment(request.POST,request.FILES)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			description = form.cleaned_data.get('description')
			due_date = form.cleaned_data.get('due_date')
			file = form.cleaned_data.get('extra_file')
			assignment = Assignment.objects.create(name = name, 
												   description = description,
												   extra_file = file,
												   due_date = due_date)
			return redirect('assignments')
	else:
		form = NewAssignment()
	return render(request,'gradebook/newAssignment.html', {'form':form})

# View that displays the submission page
def newSubmission(request):
	if request.method == 'POST':
		form = NewSubmission(request.POST, request.FILES,
							 user = request.user)
		if form.is_valid():
			name = form.cleaned_data.get('submission_name')
			file = form.cleaned_data.get('submission_file')
			student = User.objects.get(username = request.user.username)
			assignment_name = form.cleaned_data.get('assignment')
			assignment_submission = Assignment.objects.get(name = assignment_name)
			
			submission = Submit.objects.create(submission_name = name,
											   submission_file = file,
											   student = student,
											   assignment = assignment_submission)
			
			return redirect('projects')
	else:
		form = NewSubmission(user = request.user)
	return render(request, 'gradebook/newSubmission.html', {'form':form})
								

# Views for Project, Assignment, Tests, and Submission.
# They will display the List Views and Detailed Views.

class ProjectListView(generic.ListView):
	model = Project

class ProjectDetailView(generic.DetailView):
	model = Project
	
class AssignmentListView(generic.ListView):
	model = Assignment
	
class AssignmentDetailView(generic.DetailView):
	model = Assignment
	
class TestListView(generic.ListView):
	model = Test
	
class TestDetailView(generic.DetailView):
	model = Test

class SubmitListView(generic.ListView):
	model = Submit

class SubmitDetailView(generic.DetailView):
	model = Submit