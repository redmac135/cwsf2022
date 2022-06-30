from django.shortcuts import render, redirect
import json
from .forms import DiagnoseForm
from django.views.generic import View
from django.http.response import HttpResponse
from cwsf.settings import BASE_DIR

import os
import mimetypes
from .utils import parse_file, geneNames
from .ai import predict


def getRGBA(value):
    value = float(value)
    return f"rgba({int(value*256)},{256-int(value*256)},0,0.8)"


# Create your views here.
gene_names_json = json.dumps({"gene_names": geneNames})


class DiagnoseView(View):
    template_names = ["diagnose/index.html", "diagnose/success.html"]
    form_class = DiagnoseForm

    examples = ["example1.txt", "example2.txt", "example3.txt", "example4.txt"]

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request, self.template_names[0], {"form": form, "examples": self.examples}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if not form.is_valid():
            return render(
                request,
                self.template_names[0],
                {"form": form, "examples": self.examples},
            )
        try:
            results = parse_file(request.FILES["upload"])
            preds = predict(results)
        except ValueError:
            return redirect("valueError")
        form.save()
        labels = [x[0] for x in preds]
        output = [x[1] for x in preds]
        colors = [getRGBA(x) for x in output]
        return render(
            request,
            self.template_names[1],
            {
                "labels": labels,
                "output": output,
                "colors": colors,
                "matrix_data": gene_names_json,
            },
        )


def valueError(request):
    return render(request, "diagnose/valueError.html", {})


def downloadFile(request, filename=""):
    if filename == "":
        return redirect("home")
    filepath = os.path.join(
        BASE_DIR, "diagnose", "static", "diagnose", "files", filename
    )
    path = open(filepath, "rb")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response["Content-Disposition"] = f"attachment; filename={filename}"

    return response
