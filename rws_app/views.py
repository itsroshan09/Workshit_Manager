# rws_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Work
from .forms import WorkForm, BillForm

# The main view that displays all works and their bills in an accordion.
def index(request):
    all_works = Work.objects.prefetch_related('bills').all()
    context = {'works': all_works}
    return render(request, 'rws_app/index.html', context)

# View to handle the creation of a new Work.
def add_work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WorkForm()
    
    context = {
        'form': form,
        'form_title': 'Add New Work Project',
        'button_text': 'Save Work'
    }
    return render(request, 'rws_app/form_page.html', context)

# View to handle adding a Bill to a specific Work.
def add_bill(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.work = work
            bill.save()
            return redirect('index')
    else:
        form = BillForm()

    context = {
        'form': form,
        'form_title': f'Add Bill for: "{work.name}"',
        'button_text': 'Save Bill'
    }
    return render(request, 'rws_app/form_page.html', context)