from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
# from django.http import HttpResponse

class send_the_email(forms.Form):
    contact_name = forms.CharField(
                                    max_length = 35,
                                    label = "Name")
    contact_email = forms.EmailField()
    Subject = forms.CharField(
                                max_length = 35,
                                label="Subject"
    )
    contact_Message = forms.CharField(
                                    widget=forms.Textarea(
                                        attrs = {'cols':'50', 'rows': '15'}
                                        ),
                                        label="Message")

def email(request):
    if request.method == 'GET':
        form = send_the_email()
    else:
        form = send_the_email(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Subject']
            from_email = form.cleaned_data['contact_email']
            message = 'subject: ' + subject + '\n' \
                        + 'message: ' + form.cleaned_data['contact_Message'] \
                        + '\nsent by: ' + form.cleaned_data['contact_name'] \
                        + '\ncontact email: ' + form.cleaned_data['contact_email']
            print(message)
            try:
                send_mail(subject, message, from_email, ['martineztadominic@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('resume')
    return render(request, "send_email.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')