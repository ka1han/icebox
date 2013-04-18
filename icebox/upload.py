# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from icebox.models import Document
from icebox.forms import DocumentForm

def upload(request):
    if request.user.is_authenticated():
        # Handle file upload
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile = request.FILES['docfile'])
                newdoc.save()

                # Redirect to the document list after POST
                return HttpResponseRedirect(reverse('icebox.upload.upload'))
        else:
            form = DocumentForm() # A empty, unbound form

        # Load documents for the list page
        documents = Document.objects.all()

        # Render list page with the documents and the form
        return render_to_response(
            'upload.html',
            {'documents': documents, 'form': form},
            context_instance=RequestContext(request)
        )
    else:
        return render_to_response("404.html")
